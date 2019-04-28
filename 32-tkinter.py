# tkinter
"""
GUI di python
"""

import tkinter

main_window = tkinter.Tk() # biasanya root

def event_tekan():
	label2 = tkinter.Label(main_window, text="aku ditekan ^_^")
	label2.pack()

label = tkinter.Label(main_window, text = " halo saya adalah GUI sederhana dengan \n menggunkaan python")
tombol=tkinter.Button(main_window, text="tekan akuh", command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop() # file berputar-putar terus, blm exit
