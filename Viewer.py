from tkinter import  *
from PIL import ImageTk,Image

root = Tk()
root.title ("Viewer")
root.iconbitmap("image.ico")

global index
global image_list

my_img1= ImageTk.PhotoImage(Image.open("images/img1.jpg"))
my_img2= ImageTk.PhotoImage(Image.open("images/img2.jpg"))
my_img3= ImageTk.PhotoImage(Image.open("images/img3.jpg"))
my_img4= ImageTk.PhotoImage(Image.open("images/img4.jpg"))
my_img5= ImageTk.PhotoImage(Image.open("images/img5.jpg"))

image_list=[my_img1, my_img2, my_img3,my_img4,my_img5]


index = 3

my_label = Label(image=image_list[index])
my_label.grid( row=0, column=0, columnspan=3)

def back():
    global index
    global image_list
    global my_label
    if(index == 0):
        index=4
    else:
        index -= 1
    my_label.grid_forget()
    my_label = Label(image=image_list[index])
    my_label.grid(row=0, column=0, columnspan=3)


def forwar():
    global index
    global image_list
    global my_label
    if (index == 4):
        index = 0
    else:
        index += 1

    my_label.grid_forget()
    my_label = Label(image=image_list[index])
    my_label.grid(row=0, column=0, columnspan=3)




button_back = Button(root,text="<<", command=back)
button_quit = Button(root,text = "Exit program", command=root.destroy)
button_forward = Button(root, text=">>", command=forwar)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()