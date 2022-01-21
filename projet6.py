#!/usr/bin/python3

import os
import argparse
import subprocess
import sys
import time


# List of arguments that can be passed to our script
naparser = argparse.ArgumentParser()
naparser.add_argument('-m', '--mountpoint', required=True, help='the mountpoint of the new volume')
naparser.add_argument('-n', '--name', required=True, help='the lvm name, the volume group name will be set to vg_<name>, and the logical volume will be set to lg_<name>')
naparser.add_argument('-d', '--device', required=True, help='The device to use')
naparser.add_argument('-s', '--size', required=True, help='The size of logical volume ex: -s 2G or -s 200M')
naparser.add_argument('-t', '--test', action='store_true', help='show actions do be taken but do not execute them')
naparser.add_argument('-fs', '--filesystem', default="ext4", help='show actions do be taken but do not execute them')

args = naparser.parse_args()

# Definition of a function to execute system commands
# Takes the command as a parameter and returns its result on the standard output
def runcommand(command):
  print(f"Running command: {command}")
  p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
  (output, err) = p.communicate()
  p_status = p.wait()
  print("Command output : ", output.rstrip())

  if err:
    print("Command error  : ", err)
  print("Command status : ", p_status)

  if p_status != 0:
    print("Something went wrong, exiting, please check commands")
    sys.exit(1)
  print("")
  time.sleep(2)

# Main function that will be executed when the script is launched
# allows to execute the commands for the creation of the physical volume, the volume group and the logical volume
def main():
  device = args.device
  logicalvolumesize = args.size
  volumegroup = "vg_" + args.name
  logicalvolume = "lv_" + args.name
  mountpoint = args.mountpoint

  # Verification message to confirm arguments
  yesno = input(f"""The following parameters will be used
  device              : {device}
  volume group name   : {volumegroup}
  logical volume name : {logicalvolume}
  logical volume size : {logicalvolumesize}
  mount point         : {mountpoint}
  filesystem          : {args.filesystem}
  Are these correct ? (Y/N)\n""")

  if yesno.lower() == "n":
    print("Exiting")
    sys.exit(1)

  mapperdev = f"/dev/mapper/{volumegroup}-{logicalvolume}"

  # Creation of the different physical volume, group volume, logical volume
  cmdpvcreate = f"pvcreate {device}"
  cmdvgcreate = f"vgcreate {volumegroup} {device}"
  cmdlvcreate = f"lvcreate -L {logicalvolumesize} -n {logicalvolume} {volumegroup}"

  # The partition's file system command
  cmdmkfs = f"mkfs.{args.filesystem} {mapperdev}"

  # Define the line that will be written in the /etc/fstab file
  fstabline = f"{mapperdev} {mountpoint}                 {args.filesystem}    defaults,noatime        1 2\n"

  # Mountpoint command
  print(f"mount {mountpoint}")
  mountcmd = f"mount {mountpoint}"

  # Display of the commands that will be executed
  print("The following cmds and actions will be taken")
  print(f"Command : {cmdpvcreate}")
  print(f"Command : {cmdvgcreate}")
  print(f"Command : {cmdlvcreate}")
  print(f"Command : {cmdmkfs}")
  print(f"Action  : Add line {fstabline} to /etc/fstab")
  print(f"Action  : Create directory {mountpoint}")
  print("Command : "+ mountcmd)
  print("")

# Execute those comandes if argument --test is not set
  if not args.test:
    runcommand(cmdpvcreate)
    runcommand(cmdvgcreate)
    runcommand(cmdlvcreate)
    runcommand(cmdmkfs)

    fstab = open("/etc/fstab", "a")
    fstab.write(fstabline)
    fstab.close()
    os.makedirs(mountpoint)
    runcommand(mountcmd)

if __name__ == "__main__":
  main()
