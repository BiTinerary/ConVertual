import os
import sys
import Tkinter as tk
from tkFileDialog import *

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

		def RAWtoVDI():
			os.system('VBoxManage convertdd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vdi --format vdi')
			sys.exit()
		def RAWtoVHD():
			os.system('VBoxManage convertdd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vhd --format vhd')
			sys.exit()
		def RAWtoVMDK():
			os.system('VBoxManage convertdd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vmdk --format vmdk')
			sys.exit()

		def RAWOutput():
			os.system('VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.raw --format raw')
			sys.exit()
		def VHDOutput():
			os.system('VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vhd --format vhd')
			sys.exit()
		def VMDKOutput():
			os.system('VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vmdk --format vmdk')
			sys.exit()
		def VDIOutput():
			os.system('VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vdi --format vdi')
			sys.exit()

		def OpenFileButton():
			InputFile = askopenfilename()

			fileName, fileExtension = os.path.splitext(InputFile)
			BaseName = os.path.basename(InputFile)
			print BaseName
			print fileName
			print fileExtension
			
			ConvertedImageName = "ConvertedImage"
			AcceptableInputs = ['.vdi', '.vhd', '.raw', '.vmdk']

			if fileExtension.lower() in AcceptableInputs:
				BrowseBorder = tk.Label(text=InputFile, relief='ridge', width=51, height=1)
				BrowseBorder.grid(row=0, column=2, padx=5, pady=5, columnspan=4)
			else:
				ErrorFile = BaseName + " doesn't have a valid extension!"
				BrowseBorder = tk.Label(text=ErrorFile, relief='ridge', width=51, height=1, fg='red')
				BrowseBorder.grid(row=0, column=2, padx=5, pady=5, columnspan=4)

		BrowseBorder = tk.Label(text="", relief='ridge', width=51, height=1)
		BrowseBorder.grid(row=0, column=2, padx=5, pady=5, columnspan=4)
		
		ButtonOpen = tk.Button(width=15, height=1, text='Browse', command=lambda: OpenFileButton())
		ButtonOpen.grid(row=0, column=1, padx=5, pady=5)

		ButtonOne = tk.Button(width=15, height=2, text='VHD', command=lambda: VHDOutput())
		ButtonOne.grid(row=1, column=1, padx=5, pady=5)

		ButtonTwo = tk.Button(width=15, height=2, text='VDI', command=lambda: VDIOutput())
		ButtonTwo.grid(row=1, column=2, padx=5, pady=5)

		ButtonThree = tk.Button(width=15, height=2, text='VMDK', command=lambda: VMDKOutput())
		ButtonThree.grid(row=1, column=3, padx=5, pady=5)

		ButtonFour = tk.Button(width=15, height=2, text='RAW', command=lambda: RAWOutput())
		ButtonFour.grid(row=1, column=4, padx=5, pady=5)

		ButtonFive = tk.Button(width=15, height=2, text='RAW to VDI', command=lambda: RAWtoVDI())
		ButtonFive.grid(row=2, column=1, padx=5, pady=5)

		ButtonSix = tk.Button(width=15, height=2, text='RAW to VHD', command=lambda: RAWtoVHD())
		ButtonSix.grid(row=2, column=2, padx=5, pady=5)

		ButtonSeven = tk.Button(width=15, height=2, text='RAW to VMDK', command=lambda: RAWtoVMDK())
		ButtonSeven.grid(row=2, column=3, padx=5, pady=5)

if __name__ == "__main__":
	root = ButtonWidgets()
	center(root)
	root.title('Virtual Image Converter')
	root.mainloop()

		#BrowseBorder = tk.Canvas(width=100, height=100)
		#BrowseBorder.grid(row=0, column=1)
		#BrowseBorder.create_line(0,0,0,0)
		#BrowseBorder.create_line(5,0,5,0, fill='blue', dash=(4,4))
		#BrowseBorder.create_rectangle(0,50,50,0, fill='blue')
		#BrowseBorder.place(x=5, y=5)

"""
VBoxManage clonehd [old-VDI] [new-VDI] --variant Standard
VBoxManage clonehd [old-VDI] [new-VDI] --variant Fixed
"""
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