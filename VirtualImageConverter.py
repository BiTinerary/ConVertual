import os
import Tkinter as tk
from tkFileDialog import askopenfilename
import virtualbox
import sys

virtualbox.Session()

NameOfImageHere = 'test' # Input File Name of Virtual HDD Image
ConvertedImageName = 'convertedtest' # Output File Name of Converted Virtual HDD

def center(toplevel): # Function for centering all windows upon execution. This is first so that it is loaded before the creation of windows to minimize window 'flicker' upon execution.
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth() #function for finding resolution
    h = toplevel.winfo_screenheight() #function for finding resolution
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2 # find the middle of current resolution
    y = h/2 - size[1]/2 # find the middle of current resolution
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

class ButtonWidgets(tk.Tk): # Custom keyboard tester.
	def __init__(self):
		tk.Tk.__init__(self)

		def homedirectory():
			os.system('cd %CD%')
		homedirectory()

		def RAWtoVDI():
			os.system('VBoxManage convertdd "%CD%/' + '"' + NameOfImageHere + '.raw "%CD%/' + '"' + ConvertedImageName + '.vdi --format vdi')
			sys.exit()
		def RAWtoVHD():
			os.system('VBoxManage convertdd "%CD%/' + '"' + NameOfImageHere + '.raw "%CD%/' + '"' + ConvertedImageName + '.vhd --format vhd')
			sys.exit()
		def RAWtoVMDK():
			os.system('VBoxManage convertdd "%CD%/' + '"' + NameOfImageHere + '.raw "%CD%/' + '"' + ConvertedImageName + '.vmdk --format vmdk')
			sys.exit()

		def VDItoRAW():
			os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vdi "%CD%/' + '"' + ConvertedImageName + '.raw --format raw')
			sys.exit()
		def VDItoVHD():
			os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vdi "%CD%/' + '"' + ConvertedImageName + '.vhd --format vhd')
			sys.exit()
		def VDItoVMDK():
			os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vdi "%CD%/' + '"' + ConvertedImageName + '.vmdk --format vmdk')
			sys.exit()

		def VHDtoRAW():
			os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vhd "%CD%/' + '"' + ConvertedImageName + '.raw --format raw')
			sys.exit()
		def VHDtoVDI():
			os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vhd "%CD%/' + '"' + ConvertedImageName + '.vdi --format vdi')
			sys.exit()
		def VHDtoVMDK():
			os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vhd "%CD%/' + '"' + ConvertedImageName + '.vmdk --format vmdk')
			sys.exit()

		def VMDKtoRAW():
			os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vmdk "%CD%/' + '"' + ConvertedImageName + '.raw --format raw')
			sys.exit()
		def VMDKtoVDI():
			os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vmdk "%CD%/' + '"' + ConvertedImageName + '.vdi --format vdi')
			sys.exit()
		def VMDKToVHD():
			os.system('VBoxManage clonehd "%CD%/' + '"' + NameOfImageHere + '.vmdk "%CD%/' + '"' + ConvertedImageName + '.vhd --format vhd')
			sys.exit()

		def OpenButtonWindow():
			openwindow = askopenfilename()
		
		ButtonOpen = tk.Button(width=20, height=2, text='Select Image To Convert', command=lambda: OpenButtonWindow())
		ButtonOpen.grid(row=0, column=2, padx=5, pady=5, columnspan=2)

		ButtonOne = tk.Button(width=15, height=2, text='RAW to VDI', command=lambda: RAWtoVDI())
		ButtonOne.grid(row=1, column=1, padx=5, pady=5)

		ButtonTwo = tk.Button(width=15, height=2, text='RAW to VHD', command=lambda: RAWtoVHD())
		ButtonTwo.grid(row=2, column=1, padx=5, pady=5)

		ButtonThree = tk.Button(width=15, height=2, text='RAW to VMDK', command=lambda: RAWtoVMDK())
		ButtonThree.grid(row=3, column=1, padx=5, pady=5)

		ButtonFour = tk.Button(width=15, height=2, text='VDI to RAW', command=lambda: VDItoRAW())
		ButtonFour.grid(row=1, column=2, padx=5, pady=5)

		ButtonFive = tk.Button(width=15, height=2, text='VDI to VHD', command=lambda: VDItoVHD())
		ButtonFive.grid(row=2, column=2, padx=5, pady=5)

		ButtonSix = tk.Button(width=15, height=2, text='VDI to VMDK', command=lambda: VDItoVMDK())
		ButtonSix.grid(row=3, column=2, padx=5, pady=5)

		ButtonSeven = tk.Button(width=15, height=2, text='VHD to RAW', command=lambda: VHDtoRAW())
		ButtonSeven.grid(row=1, column=3, padx=5, pady=5)

		ButtonEight = tk.Button(width=15, height=2, text='VHD to VDI', command=lambda: VHDtoVDI())
		ButtonEight.grid(row=2, column=3, padx=5, pady=5)

		ButtonNine = tk.Button(width=15, height=2, text='VHD to VMDK', command=lambda: VHDtoVMDK())
		ButtonNine.grid(row=3, column=3, padx=5, pady=5)

		ButtonTen = tk.Button(width=15, height=2, text='VMDK to RAW', command=lambda: VMDKtoRAW())
		ButtonTen.grid(row=1, column=4, padx=5, pady=5)

		ButtonEleven = tk.Button(width=15, height=2, text='VMDK to VDI', command=lambda: VMDKtoVDI())
		ButtonEleven.grid(row=2, column=4, padx=5, pady=5)

		ButtonTwelve = tk.Button(width=15, height=2, text='VMDK to VHD', command=lambda: VMDKToVHD())
		ButtonTwelve.grid(row=3, column=4, padx=5, pady=5)

if __name__ == "__main__":
	root = ButtonWidgets()
	center(root)
	root.title('Virtual Image Converter')
	root.mainloop()

"""
QuestionOne = "\nWhat kind of Virtual HDD are we converting?\nAcceptable inputs: RAW, VDI, VHD, or VMDK.\n"
InputFile = raw_input(QuestionOne)

QuestionTwo = "\r\nWhat format are we converting to?\nAcceptable inputs: RAW, VDI, VHD, or VMDK.\n"
OutputFile = raw_input(QuestionTwo)
"""
"""
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

"""
VBoxManage modifyhd FILENAMEHERE.vdi --resize HDDINCREASEAMOUNT # Increase the size of .VDI HDD # modifyhd --resize function only works for .VDI and .VHD extensions
VBoxManage modifyhd FILENAMEHERE.vhd --resize HDDINCREASEAMOUNT # increase the size of .VHD HDD # modifyhd --resize function only works for .VDI and .VHD extensions
"""