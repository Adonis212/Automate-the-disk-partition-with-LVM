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


































