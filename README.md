# Automate the disk partition with LVM

## About LVM Tools.

The Logical Volume Manager (LVM) provides tools to create virtual block devices from physical devices. Virtual devices may be easier to manage than physical devices, and can have capabilities beyond what the physical devices provide themselves. A Volume Group (VG) is a collection of one or more physical devices, each called a Physical Volume (PV). A Logical Volume (LV) is a virtual block device that can be used by the system or applications. Each block of data in an LV is stored on one or more PV in the VG, according to algorithms implemented by Device Mapper (DM) in the kernel.



Exemple :


<img width="778" alt="Capture d’écran 2022-01-23 à 22 35 12" src="https://user-images.githubusercontent.com/98085590/150698830-579775a0-6c34-46a3-a867-0456de69047e.png">



About the script : 

 
 <img width="611" alt="Capture d’écran 2022-01-23 à 22 44 25" src="https://user-images.githubusercontent.com/98085590/150699096-a71a73ad-b925-4b4e-873b-88531ae53326.png">


The modules used : 

The os module -->  to open, write and create files
The argparse module --> to manage arguments passed as parameters
The subprocess module t-->  o execute system commands
The sys module  -->  used to exit with a sys.exit

The arguments to pass in parameter :

-m for mountpoint : which allows to define on which directory the volume will be mounted
-n for name : which defines the name of the volume
-d for device : which defines the disk on which the volume will be put
-s for size: which defines the size of the volume
-t for test : which allows to run in test mode without having to perform the actions
-fs for filesystem : which allows to define the file system of the volume e.g. ext4, xfs etc....

---------------------------------------------------------------------------------------------------------------------------------------------------------------


![Capture d’écran 2022-01-24 à 16 58 44](https://user-images.githubusercontent.com/98085590/150817947-508ad6a0-3ee9-4d66-8d8b-bcb3b609ec65.png)


You can see the different commands that will be executed by the script.




---------------------------------------------------------------------------------------------------------------------------------------------------------------


![Capture d’écran 2022-01-24 à 17 10 36](https://user-images.githubusercontent.com/98085590/150820095-9e239988-71e4-4c2d-9d51-32d04ce0d24a.png)


We have the main function which as its name indicates it is the main function of the script.
First define the different variables that we get according to the parameters we gave to our script ex: the device, the size, the name of the volumgroup and the logical group.



A message is displayed with all the parameters that will be used for the user to confirm with yes or no Y/N.


We define the devmapper variable with the desired location of the logical volume.


We define the different commands that will be executed:
 
  - cmdpvcreate = pvcreate /dev/sda1 command to create the physical volume on the device (disk)
  - cmdvgcreate = vgcreate {volumegroup} {device} command to create the volume group
  - cmdlvcreate = lvcreate -L {logicalvolumesize} -n {logicalvolume} {volumegroup} " Command to create the logical volume with its size, name and volume group
  - cmdmkfs = mkfs.{args.filesystem} {mapperdev} Command to define the file system of the logical volume 
  - fstabline = "{mapperdev} {mountpoint} {args.filesystem} defaults,noatime 1 2\n " We write the auto mount options in /etc/fstab
  - mountcmd = "mount {mountpoint} " mount command to mount the logical volume


---------------------------------------------------------------------------------------------------------------------------------------------------------------


Display of the actions that will be carried out.


![Capture d’écran 2022-01-24 à 17 16 27](https://user-images.githubusercontent.com/98085590/150821131-be7a78b2-f19a-449b-9169-82464225b0f8.png)


---------------------------------------------------------------------------------------------------------------------------------------------------------------



![Capture d’écran 2022-01-24 à 17 19 57](https://user-images.githubusercontent.com/98085590/150821791-7cceb0b0-f35c-4af0-8021-f2106fc6aa77.png)


1 - If the script is launched without the -t argument for test, the commands created previously are sent, one by one, as parameters to the runcommand function which will execute them.

2 - We write the location of the mount point for an auto mount at each boot of the machine.

3 - We create the directory to host the new mount point.

4 - Execute the mount command to mount the volume.


---------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to test this you need to install: mdADM, Git, Python3 and LVM2 in your computer.

And make a git clone :

git clone https://github.com/Adonis212/Automate-the-disk-partition-with-LVM


launch the command with your parameters :

python3 projet6.py -n (name)  -d /dev/(disquename)  -s (size) -fs ext4 m/mnt/name


---------------------------------------------------------------------------------------------------------------------------------------------------------------





























