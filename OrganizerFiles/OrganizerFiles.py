#python 3.9.9
# -*- coding: utf-8 -*-
# created by: Tanke6003
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
import shutil
import webbrowser
#Functions

def SelectFolder():
    folderSelected = filedialog.askdirectory()
    if folderSelected:
        selectedPathLabel.config(text="Selected Path: "+folderSelected,fg="#0000ff")
        startButton.config(state="active",fg="#4BB543")
        selectedPathLabel.update()
        startButton.update()
    return
def OrganizeFiles():
    path = selectedPathLabel.cget("text")
    path = path.replace("Selected Path: ","")
    if not os.path.exists(path):
        messagebox.showerror("Error","The path is not valid!!")
        return
    files = os.listdir(path)
    extensions = []
    for file in files:
        # Si es un archivo (no un directorio)
        if os.path.isfile(os.path.join(path, file)):
            file_split = file.split(".")
            # Verificar si hay al menos una parte después del último punto
            if len(file_split) > 1:
                ext = file_split[-1]
                # Agregar la extensión a la lista si aún no está presente
                if ext not in extensions:
                    extensions.append(ext)
    for ext in extensions:
        try:
            os.mkdir(path+"/"+ext)
        except:
            pass
    for file in files:
        fileSplit = file.split(".")
        if len(fileSplit) > 1:
            ext = fileSplit[-1]
            shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    messagebox.showinfo("Process Finished","The process has finished successfully")
    return


def openGitHub():
    webbrowser.open("https://github.com/Tanke6003/Twitch")

#Create a window with Tkinter
root = tk.Tk()
root.title("Organizer Files")
root.minsize(500,100)
root.resizable(True,True)
root.configure(bg="#f2f2f2")
#Create a Main Frame to Content All
mainFrame = tk.Frame(root)
mainFrame.pack(fill="both",expand=True,pady=10,padx=10)
#Create a Frame to Select the folder to be Organized
selectFrame = tk.Frame(mainFrame)
selectFrame.pack(side="top",fill="x",pady=5)
selectButton = tk.Button(selectFrame,text="Select Folder",cursor="hand2",command=lambda:SelectFolder())
selectButton.pack()
selectedPathLabel = tk.Label(selectFrame,text="Path no Selected",fg="#000000")
selectedPathLabel.pack(pady=10)
#Create a Frame to Organize
startFrame = tk.Frame(mainFrame)
startFrame.pack(fill="x")
startButton = tk.Button(startFrame,text="Run",cursor="hand2",state="disabled",disabledforeground="#ff0000",command=lambda:OrganizeFiles())
startButton.pack()
footerFrame = tk.Frame(mainFrame)
footerFrame.pack(side="bottom",fill="x",pady=10)
footerButton = tk.Button(footerFrame,text="GitHub Repo",command=lambda:openGitHub())
footerButton.pack()
root.mainloop()