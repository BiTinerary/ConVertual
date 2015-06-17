import os
import Tkinter as tk

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

QuestionOne = "\nWhat kind of Virtual HDD are we converting?\nAcceptable inputs: RAW, VDI, VHD, or VMDK.\n"
InputFile = raw_input(QuestionOne)

ButtonOneQuestionOne = tk.Button(width=15, height=2, text='buttonwork?')
ButtonOneQuestionOne.grid(row=0, column=0)

QuestionTwo = "\r\nWhat format are we converting to?\nAcceptable inputs: RAW, VDI, VHD, or VMDK.\n"
OutputFile = raw_input(QuestionTwo)

if InputFile.lower() == "raw" and OutputFile.lower() == "vdi":
	RAWtoVDI()

elif InputFile.lower() == "raw" and OutputFile.lower() == "vhd":
	RAWtoVHD()

elif InputFile.lower() == "raw" and OutputFile.lower() == "vmdk":
	RAWtoVMDK()

elif InputFile.lower() == "vdi" and OutputFile.lower() == "raw":
	VDItoRAW()

elif InputFile.lower() == "vdi" and OutputFile.lower() == "vhd":
	VDItoVHD()

elif InputFile.lower() == "vdi" and OutputFile.lower() == "vmdk":
	VDItoVMDK()

elif InputFile.lower() == "vhd" and OutputFile.lower() == "raw":
	VHDtoRAW()

elif InputFile.lower() == "vhd" and OutputFile.lower() == "vdi":
	VHDtoVDI()

elif InputFile.lower() == "vhd" and OutputFile.lower() == "vmdk":
	VHDtoVMDK()

elif InputFile.lower() == "vmdk" and OutputFile.lower() == "raw":
	VMDKtoRAW()

elif InputFile.lower() == "vmdk" and OutputFile.lower() == "vdi":
	VMDKtoVDI()

elif InputFile.lower() == "vmdk" and OutputFile.lower() == "vhd":
	VMDKtoVHD()
else:
	print("You hace not selected a proper input/output file extension\nMust be RAW, VDI, VHD, VMDK.")


"""
VBoxManage modifyhd FILENAMEHERE.vdi --resize HDDINCREASEAMOUNT # Increase the size of .VDI HDD # modifyhd --resize function only works for .VDI and .VHD extensions
VBoxManage modifyhd FILENAMEHERE.vhd --resize HDDINCREASEAMOUNT # increase the size of .VHD HDD # modifyhd --resize function only works for .VDI and .VHD extensions
"""