from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Couter')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("images.jpeg")
# Resize the image using resize() method
upload = upload.resize(300, 300)
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='lightblue')
label.place(x=180, y=20)

label1  = Label(root, 
                text="Hey User! Welcome to Denomination Counter Application", 
                bg='lightblue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

# Adding Buttons to the main window
button1 = Button(root, text="Let's get started!", command=msg, bg='palevioletred', fg='white')
button1.place(x=260, y=360)

# Function for opening new/top window
def topwin():
    top = TopLevel()
    top.title('Denominations Calculator')
    top.configure(bg='light blue')
    top.geometry('600x350+50+50')


    label = Label(top, text="Enter total amount", bg='lightblue')
    entry = Entry(top)
    lbl = Label(top, text = "Here are number of notes for each denomination", bg='lightblue')

    l1 = Label(top, text="2000", bg='lightblue')
    l2 = Label(top, text="500", bg='lightblue')
    l3 = Label(top, text="100", bg='lightblue')


    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            amount %= 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

        