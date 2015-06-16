import os

NameOfImageHere = 'test' # Input File Name of Virtual HDD Image
ConvertedImageName = 'convertedtest' # Output File Name of Converted Virtual HDD

#os.system(dirpath + 'VBoxManage convertdd "%CD%' + VARIABLENAMEHERE + '.raw" "%CD%' + CONVERTEDVARIABLENAME '.vdi"' + ' --format vdi') # Convert DD (.RAW) clone to VDI
def homedirectory():
	os.system('cd %CD%')
homedirectory()

def RAWtoVDI():
	os.system('VBoxManage convertdd "%CD%/' + '"' + NameOfImageHere + '.raw "%CD%/' + '"' + ConvertedImageName + '.vdi --format vdi')
def RAWtoVHD():
	os.system('VBoxManage convertdd "%CD%/' + '"' + NameOfImageHere + '.raw "%CD%/' + '"' + ConvertedImageName + '.vhd --format vhd')
def RAWtoVMDK():
	os.system('VBoxManage convertdd "%CD%/' + '"' + NameOfImageHere + '.raw "%CD%/' + '"' + ConvertedImageName + '.vmdk --format vmdk')

def VDItoRAW():
	os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vdi "%CD%/' + '"' + ConvertedImageName + '.raw --format raw')
def VDItoVHD():
	os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vdi "%CD%/' + '"' + ConvertedImageName + '.vhd --format vhd')
def VDItoVMDK():
	os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vdi "%CD%/' + '"' + ConvertedImageName + '.vmdk --format vmdk')

def VHDtoRAW():
	os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vhd "%CD%/' + '"' + ConvertedImageName + '.raw --format raw')
def VHDtoVDI():
	os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vhd "%CD%/' + '"' + ConvertedImageName + '.vdi --format vdi')
def VHDtoVMDK():
	os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vhd "%CD%/' + '"' + ConvertedImageName + '.vmdk --format vmdk')

def VMDKtoRAW():
	os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vmdk "%CD%/' + '"' + ConvertedImageName + '.raw --format raw')
def VMDKtoVDI():
	os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vmdk "%CD%/' + '"' + ConvertedImageName + '.vdi --format vdi')
def VMDKToVHD():
	os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vmdk "%CD%/' + '"' + ConvertedImageName + '.vhd --format vhd')

QUESTION1 = "\nWhat kind of Virtual HDD are we converting?\nAcceptable inputs: RAW, VDI, VHD, or VMDK.\n"
INPUTFILE = raw_input(QUESTION1)

QUESTION2 = "\r\nWhat format are we converting to?\nAcceptable inputs: RAW, VDI, VHD, or VMDK.\n"
OUTPUTFILE = raw_input(QUESTION2)

if INPUTFILE.lower() == "raw" and OUTPUTFILE.lower() == "vdi":
	RAWtoVDI()

elif INPUTFILE.lower() == "raw" and OUTPUTFILE.lower() == "vhd":
	RAWtoVHD()

elif INPUTFILE.lower() == "raw" and OUTPUTFILE.lower() == "vmdk":
	RAWtoVMDK()

elif INPUTFILE.lower() == "vdi" and OUTPUTFILE.lower() == "raw":
	VDItoRAW()

elif INPUTFILE.lower() == "vdi" and OUTPUTFILE.lower() == "vhd":
	VDItoVHD()

elif INPUTFILE.lower() == "vdi" and OUTPUTFILE.lower() == "vmdk":
	VDItoVMDK()

elif INPUTFILE.lower() == "vhd" and OUTPUTFILE.lower() == "raw":
	VHDtoRAW()

elif INPUTFILE.lower() == "vhd" and OUTPUTFILE.lower() == "vdi":
	VHDtoVDI()

elif INPUTFILE.lower() == "vhd" and OUTPUTFILE.lower() == "vmdk":
	VHDtoVMDK()

elif INPUTFILE.lower() == "vmdk" and OUTPUTFILE.lower() == "raw":
	VMDKtoRAW()

elif INPUTFILE.lower() == "vmdk" and OUTPUTFILE.lower() == "vdi":
	VMDKtoVDI()

elif INPUTFILE.lower() == "vmdk" and OUTPUTFILE.lower() == "vhd":
	VMDKtoVHD()
else:
	print("You hace not selected a proper input/output file extension\nMust be RAW, VDI, VHD, VMDK.")


"""
VBoxManage modifyhd FILENAMEHERE.vdi --resize HDDINCREASEAMOUNT # Increase the size of .VDI HDD # modifyhd --resize function only works for .VDI and .VHD extensions
VBoxManage modifyhd FILENAMEHERE.vhd --resize HDDINCREASEAMOUNT # increase the size of .VHD HDD # modifyhd --resize function only works for .VDI and .VHD extensions
"""