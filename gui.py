import tkinter as tk

def loadGUI():
    global info

    window = tk.Tk()
    label = tk.Label(text="Chapter")
    entry = tk.Entry()
    label.pack()
    entry.pack()
    button = tk.Button(text="select")
    button.pack()
    #window setup
    
    def handle_click(event):
        info = entry.get()
        window.destroy()
        print(f"You have chosen chapter {info}!")
        return info
    number = button.bind("<Button-1>", handle_click)
    #button function
    
    window.mainloop()
    #start window
    return number

print(loadGUI())
    