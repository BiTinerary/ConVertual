# ConVertual
<p align="center">
<img src='https://github.com/BiTinerary/ConVertual/blob/master/ProgramImage.png'><br>
</p>

Uses VBoxManage Commands to convert VHDD's into different extensions. (ie: .RAW, .VDI, .VHD, .VMDK) Currently works and gets the job done.

For Reference:<br>
`.VDI`: VirtualBox Extension<br>
`.RAW`: Image output when using linux `dd` command<br>
`.VHD`: Windows HyperV extension<br>
`.VMDK`: VMWare WorksStation (*cough* garbage *cough*)<br>
## Dependencies:
* Windows OS w/ VirtualBox installed in default path. ie: ./Oracle\Virtualbox\vboxmanage.exe<br>
or
* Python w/ Tkinter and Virtualbox installed in default path. ./Oracle\Virtualbox\vboxmanage.exe

## Directions:
* Click browse, select your target virtual HDD that you need converted. The directory will change in line.
* Click the button corresponding to the extension you want the VHDD to be converted to. Will default to the same directory as the executable unless otherwise specified.

## License Agreement:
Attribution-NonCommercial-ShareAlike 4.0 International (For Now)<br>
<a href='http://creativecommons.org/licenses/by-nc-sa/4.0/'>http://creativecommons.org/licenses/by-nc-sa/4.0/</a>

## TODO
* ALOT
* <strike>Will be expanded to include GUI</strike>
* <strike>Remove **hardcoded** input file name and change to accept File Selection/Open GUI window (Line 3)</strike>
* <strike>Remove hardcoded/manual designation of input file extension, ie: prompt 2. (Line 43)</strike>
* <strike>Condense line 45-End `if/elif/else` statements (and the beginning functions while your at it.)</strike>
* <strike>Create class/es for the 4 main formats (.RAW, .VDI, .VHD, .VMDK)</strike>
* Include other VBoxManage functions to accomplish tasks like:<br>
  ~ `--resize`ing<br>
  ~ Cloning full dynamic/static drives to bigger VHDD's<br>
  ~ Quick create template .VHD, .VMDK, .RAW, .VDI image using frequent/preferred settings, ie: Dynamic, 50GB, etc...<br>
  ~ Option to create virtual drive linking to external drive/USB/disk of your choice. (doesn't create a complete copy just a small ~17kb .VHDD that allows virtual booting to the drive number) >>>

`VBoxManage internalcommands createrawvmdk -filename "%USERPROFILE%"\Desktop\usb.vmdk -rawdisk \\.\PhysicalDriveZZ` where ZZ = Disk Number 

* **Batch Convert**: Convert all VHDD's (in `%CD%/BatchConvert` directory?) to a specified format. Do this by putting all applicable files into a list (`[]`), then `for loop` it with the proper, associated one liner.




