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

		AcceptableInputs = ['.raw', '.vdi', '.vhd', '.vmdk']
		ConvertedImageName = "ConvertedImage"
		
		def OpenFileButton():

			global InputFile
			InputFile = askopenfilename()

			global fileExtension
			fileName, fileExtension = os.path.splitext(InputFile)
			BaseName = os.path.basename(InputFile)

			if fileExtension.lower() in AcceptableInputs: #60
				if len(InputFile) > 60:
					BrowseBorder = tk.Label(text=InputFile, anchor='e', relief='ridge', width=51, height=1)
				else:
					BrowseBorder = tk.Label(text=InputFile, relief='ridge', width=51, height=1)
				BrowseBorder.grid(row=0, column=2, padx=5, pady=5, columnspan=4)
			else:
				ErrorFile = BaseName + " doesn't have a valid extension!"
				BrowseBorder = tk.Label(text=ErrorFile, anchor='e', relief='ridge', width=51, height=1, fg='red')
				BrowseBorder.grid(row=0, column=2, padx=5, pady=5, columnspan=4)

		def RAWConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system('VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.raw --format raw')
			elif fileExtension.lower() == AcceptableInputs[1] or AcceptableInputs[2] or AcceptableInputs[3]:
				os.system('VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.raw --format raw')
			else:
				print "wamp wamp waaaamp"

		def VDIConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system('VBoxManage convertdd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vdi --format vdi')
			elif fileExtension.lower() == AcceptableInputs[2] or AcceptableInputs[3]:
				os.system('VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vdi --format vdi')
			else:
				print "wamp wamp waaaamp"

		def VHDConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system('VBoxManage convertdd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vhd --format vhd')
			elif fileExtension.lower() == AcceptableInputs[1] or AcceptableInputs[3]:
				os.system('VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vhd --format vhd')
			else:
				print "wamp wamp waaaamp"

		def VMDKConversion():
			if fileExtension.lower() == AcceptableInputs[0]:
				os.system('VBoxManage convertdd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vmdk --format vmdk')
			elif fileExtension.lower() == AcceptableInputs[1] or AcceptableInputs[2]:
				os.system('VBoxManage clonehd ' + InputFile + ' "%CD%/"' + ConvertedImageName + '.vmdk --format vmdk')
			else:
				print "wamp wamp waaaamp"

		BrowseBorder = tk.Label(text="", relief='ridge', width=51, height=1)
		BrowseBorder.grid(row=0, column=2, padx=5, pady=5, columnspan=4)
		
		ButtonOpen = tk.Button(width=15, height=1, text='Browse', command=lambda: OpenFileButton())
		ButtonOpen.grid(row=0, column=1, padx=5, pady=5)

		ButtonOne = tk.Button(width=15, height=2, text='RAW', command=lambda: RAWConversion())
		ButtonOne.grid(row=1, column=1, padx=5, pady=5)

		ButtonTwo = tk.Button(width=15, height=2, text='VDI', command=lambda: VDIConversion())
		ButtonTwo.grid(row=1, column=2, padx=5, pady=5)

		ButtonThree = tk.Button(width=15, height=2, text='VHD', command=lambda: VHDConversion())
		ButtonThree.grid(row=1, column=3, padx=5, pady=5)

		ButtonFour = tk.Button(width=15, height=2, text='VMDK', command=lambda: VMDKConversion())
		ButtonFour.grid(row=1, column=4, padx=5, pady=5)

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

VBoxManage modifyhd FILENAMEHERE.vdi --resize HDDINCREASEAMOUNT # Increase the size of .VDI HDD # modifyhd --resize function only works for .VDI and .VHD extensions
VBoxManage modifyhd FILENAMEHERE.vhd --resize HDDINCREASEAMOUNT # increase the size of .VHD HDD # modifyhd --resize function only works for .VDI and .VHD extensions
"""