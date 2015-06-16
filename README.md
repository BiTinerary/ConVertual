# ConVertual
Uses VBoxManage Commands to convert VHDD's into different extensions. (ie: .RAW, .VDI, .VHD, .VMDK) Currently works and gets the job done but the actual code is pretty gnarly. 

For Reference:<br>
`.VDI`: VirtualBox Extension<br>
`.RAW`: Image output when using linux `dd` command<br>
`.VHD`: Windows HyperV extension<br>
`.VMDK`: VMWare WorksStation (*cough* garbage *cough*)<br>

# General Premise:
* Put Target Virtual HDD that you need converted into the same directory as the VBoxManage and .Py Script
* You currently have to change the target VHDD name to "test"
* Run .Py Script > It will prompt for 2 inputs.<br>
  ~ 1: What is the target VHDD's current extension?<br>
  ~ 2: What is the output extension you're converting to?<br>
* .Py Script will convert accordingly

# TODO
* ALOT
* Will be expanded to include GUI
* Remove **hardcoded** input file name and change to accept File Selection/Open GUI window (Line 3)
* Remove hardcoded/manual designation of input file extension, ie: prompt 2. (Line 43)
* Condense line 45-End `if/elif/else` statements (and the beginning functions while your at it.)
* Create classes for the 4 main formats (.RAW, .VDI, .VHD, .VMDK)
* Include other VBoxManage functions to accomplish tasks like:<br>
  ~ `--resize`ing<br>
  ~ Cloning full dynamic/static drives to bigger VHDD's<br>
  ~ Quick create template .VHD, .VMDK, .RAW, .VDI image using frequent/preferred settings, ie: Dynamic, 50GB, etc...<br>
  ~ Option to create virtual drive linking to external drive/USB/disk of your choice. (doesn't create a complete copy just a small ~17kb .VHDD that allows virtual booting to the drive number) >>>

`VBoxManage internalcommands createrawvmdk -filename "%USERPROFILE%"\Desktop\usb.vmdk -rawdisk \\.\PhysicalDriveZZ` where ZZ = Disk Number 

* **Batch Convert**: Convert all VHDD's (in `%CD%/BatchConvert` directory?) to a specified format. Do this by putting all applicable files into a list (`[]`), then `for loop` it with the proper, associated one liner.




