import os
import sys
import subprocess
import Tkinter as tk
from Tkinter import IntVar
from tkFileDialog import *

def center(toplevel): # Function for centering all windows upon execution.
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth() #Find width resolution
    h = toplevel.winfo_screenheight() #Find height resolution
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2 # find the middle of width resolution
    y = h/2 - size[1]/2 # find the middle of height resolution
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

class ButtonWidgets(tk.Tk): # Main GUI window with buttons in line.
	def __init__(self):
		tk.Tk.__init__(self)

		self.minsize(width=500, height=300)
		self.resizable(0,0)
		self.intvar = IntVar(self)

		OracleFilePath = 'cd "C:/Program Files/Oracle/VirtualBox/" &&' # Hardcoded but default path for VirtualBox, in order to use vboxmanage.exe
		AcceptableInputs = ['.raw', '.vdi', '.vhd', '.vmdk'] # sanitized input for the four main VHDD extensions
		ConvertedImageName = "ConvertedImage" # Hardcoded "defaultname" + "convertedimage"
		
		def OpenFileButton():

			global InputFile
			InputFile = askopenfilename()  # "Browse" button for selecting target image

			global fileExtension
			fileName, fileExtension = os.path.splitext(InputFile) # extension of target image

			global BaseName
			BaseName = os.path.basename(InputFile) # Path of target image

			if fileExtension.lower() in AcceptableInputs: # sanitized input for target image.
				if len(InputFile) > 60: # if file name is too long to be displayed, put leading characters off screen.
					BrowseBorder = tk.Label(text=InputFile, anchor='e', relief='ridge', width=51, height=1)
				else: # else file name is shorter, center it.
					BrowseBorder = tk.Label(text=InputFile, relief='ridge', width=51, height=1)
				BrowseBorder.grid(row=0, column=2, padx=5, pady=5, columnspan=4)
			else: # sanitized input, prompting user that they've selected an extension other than the standard options.
				ErrorFile = BaseName + " doesn't have a valid extension!"
				if len(BaseName) > 40:
					BrowseBorder = tk.Label(text=ErrorFile, anchor='e', relief='ridge', width=51, height=1, fg='red')
				else:
					BrowseBorder = tk.Label(text=ErrorFile, relief='ridge', width=51, height=1, fg='red')
				BrowseBorder.grid(row=0, column=2, padx=5, pady=5, columnspan=4)
			UpdateOutputName()

		def UpdateOutputName():
			try:
				FullNameRadioExtension = os.path.splitext(SaveAsFile)[0] + PrintConvertExtension(self.intvar.get())
			except:
				FullNameRadioExtension = os.path.splitext(InputFile)[0] + PrintConvertExtension(self.intvar.get())

			FullConvertName = os.path.splitext(InputFile)[0] + fileExtension

			if fileExtension.lower() in AcceptableInputs:
				if len(FullConvertName) > 60:
					try:
						TargetBorder = tk.Label(text=FullNameRadioExtension, anchor='e', relief='ridge', width=51, height=1)	
					except:
						TargetBorder = tk.Label(text=FullConvertName, anchor='e', relief='ridge', width=51, height=1)
				else:
					try:
						TargetBorder = tk.Label(text=FullNameRadioExtension, relief='ridge', width=51, height=1)
					except:
						TargetBorder = tk.Label(text=FullConvertName, relief='ridge', width=51, height=1)
					TargetBorder.grid(row=1, column=2, padx=5, pady=5, columnspan=4)
			else:
				ErrorFile = BaseName + " doesn't have a valid extension!"
				if len(BaseName) > 40:
					TargetBorder = tk.Label(text=ErrorFile, anchor="e", relief='ridge', width=51, height=1, fg='red')
				else:
					TargetBorder = tk.Label(text=ErrorFile, relief='ridge', width=51, height=1, fg='red')
				TargetBorder.grid(row=1, column=2, padx=5, pady=5, columnspan=4)

		def SaveAsButton():
			global SaveAsFile
			SaveAsFile = asksaveasfilename()
			print "SAVE AS FILE" + SaveAsFile

			FullNameRadioExtension = os.path.splitext(SaveAsFile)[0] + PrintConvertExtension(self.intvar.get())
			print "NAME RADIO" + FullNameRadioExtension

			FullConvertName = os.path.splitext(SaveAsFile)[0] + fileExtension
			print "FULL CONV NAME" + FullConvertName

			if fileExtension.lower() in AcceptableInputs:
				if len(FullConvertName) > 60:
					try:
						TargetBorder = tk.Label(text=FullNameRadioExtension, anchor='e', relief='ridge', width=51, height=1)	
					except:
						TargetBorder = tk.Label(text=FullConvertName, anchor='e', relief='ridge', width=51, height=1)
				else:
					try:
						TargetBorder = tk.Label(text=FullNameRadioExtension, relief='ridge', width=51, height=1)
					except:
						TargetBorder = tk.Label(text=FullConvertName, relief='ridge', width=51, height=1)
				TargetBorder.grid(row=1, column=2, padx=5, pady=5, columnspan=4)
			else:
				ErrorFile = BaseName + " doesn't have a valid extension!"
				if len(BaseName) > 40:
					TargetBorder = tk.Label(text=ErrorFile, anchor="e", relief='ridge', width=51, height=1, fg='red')
				else:
					TargetBorder = tk.Label(text=ErrorFile, relief='ridge', width=51, height=1, fg='red')
				TargetBorder.grid(row=1, column=2, padx=5, pady=5, columnspan=4)

		def RAWConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system(OracleFilePath + 'VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.raw --format raw')
			elif fileExtension.lower() == AcceptableInputs[1] or AcceptableInputs[2] or AcceptableInputs[3]:
				os.system(OracleFilePath + 'VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.raw --format raw')
			else:
				return

		def VDIConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system(OracleFilePath + 'VBoxManage convertdd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vdi --format vdi')
			elif fileExtension.lower() == AcceptableInputs[2] or AcceptableInputs[3]:
				os.system(OracleFilePath + 'VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vdi --format vdi')
			else:
				return

		def VHDConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system(OracleFilePath + 'VBoxManage convertdd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vhd --format vhd')
			elif fileExtension.lower() == AcceptableInputs[1] or AcceptableInputs[3]:
				os.system(OracleFilePath + 'VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vhd --format vhd')
			else:
				return

		def VMDKConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system(OracleFilePath + 'VBoxManage convertdd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vmdk --format vmdk')
			elif fileExtension.lower() == AcceptableInputs[1] or AcceptableInputs[2]:
				os.system(OracleFilePath + 'VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vmdk --format vmdk')
			else:
				return

		"""
		def RAWConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system(OracleFilePath + 'VBoxManage clonehd ' + InputFile + ' "%CD%/"' + SaveAsFile + '.raw --format raw')
			elif fileExtension.lower() == AcceptableInputs[1] or AcceptableInputs[2] or AcceptableInputs[3]:
				os.system(OracleFilePath + 'VBoxManage clonehd ' + InputFile + ' "%CD%/"' + SaveAsFile + '.raw --format raw')
			else:
				return

		def VDIConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system(OracleFilePath + 'VBoxManage convertdd ' + InputFile + ' "%CD%/"' + SaveAsFile + '.vdi --format vdi')
			elif fileExtension.lower() == AcceptableInputs[2] or AcceptableInputs[3]:
				os.system(OracleFilePath + 'VBoxManage clonehd ' + InputFile + ' "%CD%/"' + SaveAsFile + '.vdi --format vdi')
			else:
				return

		def VHDConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system(OracleFilePath + 'VBoxManage convertdd ' + InputFile + ' "%CD%/"' + SaveAsFile + '.vhd --format vhd')
			elif fileExtension.lower() == AcceptableInputs[1] or AcceptableInputs[3]:
				os.system(OracleFilePath + 'VBoxManage clonehd ' + InputFile + ' "%CD%/"' + SaveAsFile + '.vhd --format vhd')
			else:
				return

		def VMDKConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system(OracleFilePath + 'VBoxManage convertdd ' + InputFile + ' "%CD%/"' + SaveAsFile + '.vmdk --format vmdk')
			elif fileExtension.lower() == AcceptableInputs[1] or AcceptableInputs[2]:
				os.system(OracleFilePath + 'VBoxManage clonehd ' + InputFile + ' "%CD%/"' + SaveAsFile + '.vmdk --format vmdk')
			else:
				return
		"""

		def PrintConvertExtension(x):
			if x == 0:
				return ".raw"
			elif x == 1:
				return ".vdi"
			elif x == 2:
				return ".vhd"
			elif x == 3:
				return ".vmdk"
			else:
				return None

		def ConvertOption(x):
			if x == 0:
				RAWConversion()
			elif x == 1:
				VDIConversion()
			elif x == 2:
				VHDConversion()
			elif self.intvar.get() == 3:
				VMDKConversion()
			else:
				return

		def VirtualBootUSB():
			os.system(OracleFilePath + 'VBoxManage internalcommands createrawvmdk -filename "%USERPROFILE%"\Desktop\VirtualUSB.vdi -rawdisk //./PhysicalDrive2')

		BrowseBorder = tk.Label(text="", relief='ridge', width=51, height=1)
		BrowseBorder.grid(row=0, column=2, padx=5, pady=5, columnspan=4)

		TargetBorder = tk.Label(text="", relief='ridge', width=51, height=1)
		TargetBorder.grid(row=1, column=2, padx=5, pady=5, columnspan=4)
		
		ButtonBrowse = tk.Button(width=15, height=1, text='Browse', command=lambda: OpenFileButton())
		ButtonBrowse.grid(row=0, column=1, padx=5, pady=5)

		ButtonTarget = tk.Button(width=15, height=1, text='Save As', command=lambda: SaveAsButton())
		ButtonTarget.grid(row=1, column=1, padx=5, pady=5)

		ButtonOne = tk.Radiobutton(text='RAW', value=0, variable=self.intvar, command=lambda:UpdateOutputName())
		ButtonOne.place(x=60, y=80)

		ButtonTwo = tk.Radiobutton(text='VDI', value=1, variable=self.intvar, command=lambda:UpdateOutputName())
		ButtonTwo.place(x=170, y=80)

		ButtonThree = tk.Radiobutton(text='VHD', value=2, variable=self.intvar, command=lambda:UpdateOutputName())
		ButtonThree.place(x=270, y=80)

		ButtonFour = tk.Radiobutton(text='VMDK', value=3, variable=self.intvar, command=lambda:UpdateOutputName())
		ButtonFour.place(x=370, y=80)

		ConvertButton = tk.Button(text='Convert!', width=67, height=2, command=lambda: ConvertOption(self.intvar.get()))
		ConvertButton.place(x=8, y=117)

		LabelVirtualUSB = tk.Canvas(height=1, width=490, bg='gray')
		LabelVirtualUSB.place(x=2,y=170)

if __name__ == "__main__": # compile the main class/widgets to be displayed on screen.
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

VBoxManage modifyhd FILENAMEHERE.vdi --resize HDDINCREASEAMOUNT # Increase the size of .VDI HDD # modifyhd --resize function only works for .VDI and .VHD extensions
VBoxManage modifyhd FILENAMEHERE.vhd --resize HDDINCREASEAMOUNT # increase the size of .VHD HDD # modifyhd --resize function only works for .VDI and .VHD extensions
"""