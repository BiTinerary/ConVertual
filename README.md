# ConVertual
Uses VBoxManage Commands to convert VHDD's into different extensions. (ie: .RAW, .VDI, .VHD, .VMDK) Currently works and gets the job done but the actual code is horrendous.

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
* Condense line 45-End `if/elif/else` statements (and the beginning functions while you aat it.)
* Create classes for the 4 main formats (.RAW, .VDI, .VHD, .VMDK)
