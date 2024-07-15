import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed')

def hello_func():
    print("Hello")

#create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

#ttk widgets
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

#create widgets
text = tk.Text(master=window)
text.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()



#ttk hello
hello = ttk.Button(master = window, text = 'Press me', command = hello_func)
hello.pack()

#ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func)
button.pack()


#run
window.mainloop()