from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os

if __name__ == '__main__':
    # basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notebook.ico")

    root.geometry("644x788")

    # add TextArea
    TextArea = Text(root, font="lucida 12")
    file = None
    TextArea.pack(expand=TRUE, fill=BOTH)


    # functions

    def Newfile():
        global file
        root.title("Untitled-NotePad")
        file = None
        TextArea.delete(1.0, END)


    def Openfile():
        global file
        file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("TextDocuments", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - NotePad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()


    def Savefile():
        global file
        if file == None:
            file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"), ("TextDocuments", "*.txt")])
            if file == "":
                file = None
            else:
                # save as a new file
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()

                root.title(os.path.basename(file) + " - NotePad")
                print("File Saved")


        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

    def Exitapp():
        root.destroy()


    def Filemenu():
        pass


    def cut():
        TextArea.event_generate(("<<Cut>>"))


    def copy():
        TextArea.event_generate(("<<Copy>>"))


    def paste():
        TextArea.event_generate(("<<Paste>>"))


    def about():
        showinfo("NotePad", "NotePad By Kartik-Cybertron")


    # file Menu

    # lets crate a menu bar
    menuBar = Menu(root)
    fileMenu = Menu(menuBar, tearoff=0)  # tearoff to remove line
    # to open new file
    fileMenu.add_command(label="New", command=Newfile)
    fileMenu.add_command(label="Open", command=Openfile)

    # to save current file
    fileMenu.add_command(label="Save", command=Savefile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=Exitapp)
    menuBar.add_cascade(label="File", menu=fileMenu)

    # Edit menu
    editMenu = Menu(menuBar, tearoff=0)
    # Features of menu
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu=editMenu)

    # help menu
    helpMenu = Menu(menuBar, tearoff=0)

    helpMenu.add_command(label="About", command=about)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menuBar)

    # adding scollbar
    scrollBar = Scrollbar(TextArea)
    scrollBar.pack(side=RIGHT, fill=Y)
    scrollBar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollBar.set)

    root.mainloop()
