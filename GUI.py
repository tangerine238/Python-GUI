import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# window
#window = tk.Tk()
window = ttk.Window(themename = 'darkly')
window.title('GUI')
window.geometry('700x500') #widthxheight

#title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold') #master is place where label is displayed. Text is the text
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#run
window.mainloop()
