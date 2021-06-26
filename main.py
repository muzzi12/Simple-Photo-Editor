from tkinter import *
from PIL import Image,ImageEnhance,ImageOps,ImageFilter
import PIL
import cv2
import os
from tkinter import filedialog
from tkinter import messagebox


master = Tk()
file = ''
contrast2 = 1
sharpness2 = 1
color2 = 1
rotate2 = 0
poster2 = 0
brightness2= 0
blur2 = 0

def create():
    if file=='':
        messagebox.showerror('Photo Editor', 'Please select a picture')
    else:

        if poster2==0 and brightness2==0:
            try:
                contrast_value = contrast2
                sharpness_value = sharpness2
                color_value = color2
                rotate_value = rotate2
                blur_value = blur2
                img = Image.open(file)
                contrast_create = PIL.ImageEnhance.Contrast(img).enhance(int(contrast_value))
                color_create = PIL.ImageEnhance.Color(contrast_create).enhance(int(color_value))
                sharpness_create = PIL.ImageEnhance.Sharpness(color_create).enhance(int(sharpness_value))
                img1 = sharpness_create.filter(ImageFilter.GaussianBlur(radius=int(blur_value)))
                img2 = img1.rotate(int(rotate_value))
                final = img2.resize((1920,1080))
                path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                    defaultextension='.png', initialfile='Untitled.jpg',
                                                    initialdir='D:/edited/')
                final.save(path)
                os.startfile(path)
            except ValueError:
                pass

        elif poster2==0:
            try:
                contrast_value = contrast2
                sharpness_value = sharpness2
                brightness_value = brightness2
                color_value = color2
                rotate_value = rotate2
                blur_value = blur2
                img = Image.open(file)
                contrast_create = PIL.ImageEnhance.Contrast(img).enhance(int(contrast_value))
                color_create = PIL.ImageEnhance.Color(contrast_create).enhance(int(color_value))
                sharpness_create = PIL.ImageEnhance.Sharpness(color_create).enhance(int(sharpness_value))
                img2 = sharpness_create.filter(ImageFilter.GaussianBlur(radius=int(blur_value)))
                img3 = img2.rotate(int(rotate_value))
                img1 = PIL.ImageEnhance.Brightness(img3).enhance(float(brightness_value))

                final = img1.resize((1920, 1080))
                path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                    defaultextension='.png', initialfile='Untitled.jpg',
                                                    initialdir='D:/edited/')
                final.save(path)
                os.startfile(path)
            except ValueError:
                pass

        elif brightness2==0:
            try:
                contrast_value = contrast2
                sharpness_value = sharpness2
                poster_value = poster2
                color_value = color2
                rotate_value = rotate2
                blur_value = blur2
                img = Image.open(file)
                contrast_create = PIL.ImageEnhance.Contrast(img).enhance(int(contrast_value))
                color_create = PIL.ImageEnhance.Color(contrast_create).enhance(int(color_value))
                sharpness_create = PIL.ImageEnhance.Sharpness(color_create).enhance(int(sharpness_value))
                img2 = sharpness_create.filter(ImageFilter.GaussianBlur(radius=int(blur_value)))
                img3 = img2.rotate(int(rotate_value))
                img1 = PIL.ImageOps.posterize(img3,int(poster_value))

                final = img1.resize((1920, 1080))
                path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                    defaultextension='.png', initialfile='Untitled.jpg',
                                                    initialdir='D:/edited/')
                final.save(path)
                os.startfile(path)

            except ValueError:
                pass

        else:
            try:
                contrast_value = contrast2
                sharpness_value = sharpness2
                color_value = color2
                brightness_value = brightness2
                rotate_value = rotate2
                poster_value = poster2
                blur_value = blur2
                img = Image.open(file)
                contrast_create = PIL.ImageEnhance.Contrast(img).enhance(int(contrast_value))
                color_create = PIL.ImageEnhance.Color(contrast_create).enhance(int(color_value))
                sharpness_create = PIL.ImageEnhance.Sharpness(color_create).enhance(int(sharpness_value))
                poster_create = PIL.ImageOps.posterize(sharpness_create, int(poster_value))
                img1 = poster_create.filter(ImageFilter.GaussianBlur(radius=int(blur_value)))
                rotate_create = img1.rotate(int(rotate_value))
                brightness_create = PIL.ImageEnhance.Brightness(rotate_create).enhance(float(brightness_value))

                final = brightness_create.resize((1920,1080))
                path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                    defaultextension='.png', initialfile='Untitled.jpg',
                                                    initialdir='D:/edited/')

                final.save(path)
                os.startfile(path)
            except ValueError:
                pass
def pencil():
    global file
    if file=='':
        messagebox.showerror('Photo Editor','Please select a picture!')
    else:
        image = cv2.imread(file)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        inverted = 255 - gray
        blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
        inverted_blurr = 255 - blurred
        pencil = cv2.divide(gray, inverted_blurr, scale=256.0)
        path = filedialog.asksaveasfilename(filetypes=[('JPG Files','*.jpg'),('PNG Files','*.png')],defaultextension='.png',initialfile='Untitled.jpg',initialdir='D:/edited/')
        try:
            cv2.imwrite(path, pencil)
            os.startfile(path)
        except cv2.error:
            pass

def emboss1():
    global file
    if file=='':
        messagebox.showerror('Photo Editor','Please select a picture!')
    else:
        img = Image.open(file)
        embossed = img.filter(ImageFilter.EMBOSS())
        path = filedialog.asksaveasfilename(filetypes=[('JPG Files','*.jpg'),('PNG Files','*.png')],defaultextension='.png',initialfile='Untitled.jpg',initialdir='D:/edited/')
        try:
            embossed.save(path)
            os.startfile(path)
        except ValueError:
            pass

def enhance1():
    global file
    if file=='':
        messagebox.showerror('Photo Editor','Please select a picture!')
    else:
        img = Image.open(file)
        embossed = img.filter(ImageFilter.EDGE_ENHANCE_MORE())
        path = filedialog.asksaveasfilename(filetypes=[('JPG Files','*.jpg'),('PNG Files','*.png')],defaultextension='.png',initialfile='Untitled.jpg',initialdir='D:/edited/')
        try:
            embossed.save(path)
            os.startfile(path)
        except ValueError:
            pass

def credits():
    messagebox.showinfo('Photo Editor','Photo Editor Made By Muzammil!')

def choose():
    global file
    path = filedialog.askopenfilename(filetypes=[('JPG Files','*.jpg'),('PNG Files','*.png')],defaultextension='.png',initialdir='E:/Captures/')
    file = path
    label1.config(text=file)

def inverted():
    global file
    if file=='':
        messagebox.showerror('Photo Editor','Please select a picture!')
    else:
        img = Image.open(file)
        inverted_image = PIL.ImageOps.invert(img)
        final = inverted_image.resize((1920,1080))
        path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                          defaultextension='.png',initialfile='Untitled.jpg',initialdir='D:/edited/')
        try:
            final.save(path)
            os.startfile(path)
        except ValueError:
            pass

def Mirror():
    global file
    if file=='':
        messagebox.showerror('Photo Editor','Please select a picture!')
    else:
        img = Image.open(file)
        im_mirror = ImageOps.mirror(img)
        final = im_mirror.resize((1920,1080))
        path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                          defaultextension='.png',initialfile='Untitled.jpg',initialdir='D:/edited/')
        try:
            final.save(path)
            os.startfile(path)
        except ValueError:
            pass


def Black():
    global file
    if file=='':
        messagebox.showerror('Photo Editor','Please select a picture!')
    else:
        img = Image.open(file)
        image_file = img.convert('1')
        final = image_file.resize((1920,1080))
        path = filedialog.asksaveasfilename(filetypes=[('JPG Files','*.jpg'),('PNG Files','*.png')],defaultextension='.png',initialfile='Untitled.jpg',initialdir='D:/edited/')
        try:
            final.save(path)
            os.startfile(path)
        except ValueError:
            pass


def sharpness1():
    def enter1(event):
        contrast_button.config(bg='grey', fg='black', relief=SUNKEN)

    def leave1(event):
        contrast_button.config(bg='black', fg='white', relief=RAISED)
    def confirm():
        global sharpness2
        sharpness2=int(contrast_l.get())
        if sharpness2>20:
            messagebox.showerror('Video Editor','Invalid Value!')
        else:
            sharpnes_.config(text=sharpness2)
            newindow.destroy()

    newindow = Toplevel(master)
    newindow.geometry('250x150+800+400')
    newindow.resizable(0,0)
    newindow.title('Sharpness')
    newindow.config(background='white')
    contrast_label = Label(newindow,text='Change The Sharpness Of Your Picture',font='cursive 10 bold italic',bg='white',fg='aqua')
    contrast_label.pack(side=TOP)
    contrast_l = Scale(newindow,from_=1, to=20,resolution=0.1,bg='white',orient=HORIZONTAL,cursor='hand2',length=240)
    contrast_l.place(x=1,y=50)
    contrast_button = Button(newindow,text='Confirm!',bg='black',fg='white',activeforeground='black',activebackground='white',font='cursive 12 bold italic',cursor='hand2',command=confirm)
    contrast_button.pack(side=BOTTOM)
    contrast_button.bind('<Enter>',enter1)
    contrast_button.bind('<Leave>',leave1)

def color1():
    def enter1(event):
        color_button.config(bg='grey', fg='black', relief=SUNKEN)

    def leave1(event):
        color_button.config(bg='black', fg='white', relief=RAISED)

    def confirm():
        global color2
        color2=int(contrast_l.get())
        if color2>20:
            messagebox.showerror('Video Editor','Invalid Value!')
        else:
            color_.config(text=color2)
            newindow.destroy()

    newindow = Toplevel(master)
    newindow.geometry('250x150+800+400')
    newindow.resizable(0,0)
    newindow.title('Color')
    newindow.config(background='white')
    color_label = Label(newindow,text='Change The Color Of Your Picture',font='cursive 10 bold italic',bg='white',fg='aqua')
    color_label.pack(side=TOP)
    contrast_l = Scale(newindow,from_=1, to=20,resolution=0.1,bg='white',orient=HORIZONTAL,cursor='hand2',length=240)
    contrast_l.place(x=1,y=50)
    color_button = Button(newindow,text='Confirm!',bg='black',fg='white',activeforeground='black',activebackground='white',font='cursive 12 bold italic',cursor='hand2',command=confirm)
    color_button.pack(side=BOTTOM)
    color_button.bind('<Enter>', enter1)
    color_button.bind('<Leave>', leave1)


def poster1():
    def enter1(event):
        contrast_button.config(bg='grey', fg='black', relief=SUNKEN)

    def leave1(event):
        contrast_button.config(bg='black', fg='white', relief=RAISED)
    def confirm():
        global poster2
        poster2=int(contrast_l.get())
        if poster2>8:
            messagebox.showerror('Video Editor','Invalid Value')
        else:
            poster_.config(text=poster2)
            newindow.destroy()

    newindow = Toplevel(master)
    newindow.geometry('250x150+800+400')
    newindow.resizable(0,0)
    newindow.title('Posterize')
    newindow.config(background='white')
    contrast_label = Label(newindow,text='Posterize Your Picture',font='cursive 10 bold italic',bg='white',fg='aqua')
    contrast_label.pack(side=TOP)
    contrast_l = Scale(newindow, from_=0, to=8, resolution=1, bg='white', orient=HORIZONTAL,
                       cursor='hand2', length=240)
    contrast_l.place(x=1, y=50)
    contrast_button = Button(newindow,text='Confirm!',bg='black',fg='white',activeforeground='black',activebackground='white',font='cursive 12 bold italic',cursor='hand2',command=confirm)
    contrast_button.pack(side=BOTTOM)
    contrast_button.bind('<Enter>', enter1)
    contrast_button.bind('<Leave>', leave1)

def rotate1():
    def enter1(event):
        contrast_button.config(bg='grey', fg='black', relief=SUNKEN)

    def leave1(event):
        contrast_button.config(bg='black', fg='white', relief=RAISED)
    def confirm():
        global rotate2
        rotate2=contrast_l.get()
        rotate_.config(text=rotate2)
        newindow.destroy()

    newindow = Toplevel(master)
    newindow.geometry('250x150+800+400')
    newindow.resizable(0,0)
    newindow.title('Rotate')
    newindow.config(background='white')
    contrast_label = Label(newindow,text='Rotate Your Picture',font='cursive 10 bold italic',bg='white',fg='aqua')
    contrast_label.pack(side=TOP)
    contrast_l = Scale(newindow,from_=0, to=360,resolution=5,bg='white',orient=HORIZONTAL,label='Degrees',cursor='hand2',length=240)
    contrast_l.place(x=1,y=50)
    contrast_button = Button(newindow,text='Confirm!',bg='black',fg='white',activeforeground='black',activebackground='white',font='cursive 12 bold italic',cursor='hand2',command=confirm)
    contrast_button.pack(side=BOTTOM)
    contrast_button.bind('<Enter>', enter1)
    contrast_button.bind('<Leave>', leave1)

def contrast1():
    def enter1(event):
        contrast_button.config(bg='grey', fg='black', relief=SUNKEN)

    def leave1(event):
        contrast_button.config(bg='black', fg='white', relief=RAISED)
    def confirm():
        global contrast2
        contrast2 = int(contrast_l.get())
        if contrast2 >20:
            messagebox.showerror('Video Editor','Invalid Value!')
        else:
            contrast_.config(text=contrast2)
            newindow.destroy()

    newindow = Toplevel(master)
    newindow.geometry('250x150+800+400')
    newindow.resizable(0,0)
    newindow.title('Contrast')
    newindow.config(background='white')
    contrast_label = Label(newindow,text='Change The Contrast Of Your Picture',font='cursive 10 bold italic',bg='white',fg='aqua')
    contrast_label.pack(side=TOP)
    contrast_l = Scale(newindow,from_=1, to=20,resolution=0.1,bg='white',orient=HORIZONTAL,cursor='hand2',length=240)
    contrast_l.place(x=1,y=50)
    contrast_button = Button(newindow,text='Confirm!',bg='black',fg='white',activeforeground='black',activebackground='white',font='cursive 12 bold italic',cursor='hand2',command=confirm)
    contrast_button.pack(side=BOTTOM)
    contrast_button.bind('<Enter>', enter1)
    contrast_button.bind('<Leave>', leave1)

def brightness1():
    def enter1(event):
        contrast_button.config(bg='grey', fg='black', relief=SUNKEN)

    def leave1(event):
        contrast_button.config(bg='black', fg='white', relief=RAISED)
    def confirm():
        global brightness2
        brightness2 = float(contrast_l.get())
        brightness_.config(text=brightness2)
        newindow.destroy()

    newindow = Toplevel(master)
    newindow.geometry('250x150+800+400')
    newindow.resizable(0,0)
    newindow.title('Brightness')
    newindow.config(background='white')
    contrast_label = Label(newindow,text='Change The Brightness Of Your Picture',font='cursive 10 bold italic',bg='white',fg='aqua')
    contrast_label.pack(side=TOP)
    contrast_l = Scale(newindow, from_=0, to=20, resolution=0.1, bg='white', orient=HORIZONTAL,
                       cursor='hand2', length=240)
    contrast_l.place(x=1, y=50)
    contrast_button = Button(newindow,text='Confirm!',bg='black',fg='white',activeforeground='black',activebackground='white',font='cursive 12 bold italic',cursor='hand2',command=confirm)
    contrast_button.pack(side=BOTTOM)
    contrast_button.bind('<Enter>', enter1)
    contrast_button.bind('<Leave>', leave1)

def blur1():
    def enter1(event):
        contrast_button.config(bg='grey', fg='black', relief=SUNKEN)

    def leave1(event):
        contrast_button.config(bg='black', fg='white', relief=RAISED)
    def confirm():
        global blur2
        blur2 = contrast_l.get()
        blurr_.config(text=blur2)
        newindow.destroy()

    newindow = Toplevel(master)
    newindow.geometry('250x150+800+400')
    newindow.resizable(0,0)
    newindow.title('Blur')
    newindow.config(background='white')
    contrast_label = Label(newindow,text='Blur Your Picture',font='cursive 10 bold italic',bg='white',fg='aqua')
    contrast_label.pack(side=TOP)
    contrast_l = Scale(newindow, from_=0, to=50, resolution=1, bg='white', orient=HORIZONTAL,
                       cursor='hand2', length=240)
    contrast_l.place(x=1, y=50)
    contrast_button = Button(newindow,text='Confirm!',bg='black',fg='white',activeforeground='black',activebackground='white',font='cursive 12 bold italic',cursor='hand2',command=confirm)
    contrast_button.pack(side=BOTTOM)
    contrast_button.bind('<Enter>', enter1)
    contrast_button.bind('<Leave>', leave1)


def enter1(event):
    button1.config(bg='grey',fg='black',relief=SUNKEN)

def leave1(event):
    button1.config(bg='black',fg='white',relief=RAISED)

def enter2(event):
    button2.config(bg='grey',fg='black',relief=SUNKEN)

def leave2(event):
    button2.config(bg='black',fg='white',relief=RAISED)

def enter3(event):
    button3.config(bg='grey',fg='black',relief=SUNKEN)

def leave3(event):
    button3.config(bg='black',fg='white',relief=RAISED)

def enter4(event):
    button4.config(bg='grey',fg='black',relief=SUNKEN)

def leave4(event):
    button4.config(bg='black',fg='white',relief=RAISED)

def enter5(event):
    button5.config(bg='grey',fg='black',relief=SUNKEN)

def leave5(event):
    button5.config(bg='black',fg='white',relief=RAISED)

def enter6(event):
    openfile.config(bg='grey',fg='black',relief=SUNKEN)

def leave6(event):
    openfile.config(bg='black',fg='white',relief=RAISED)


def enter7(event):
    contrast.config(fg='grey')

def leave7(event):
    contrast.config(fg='black')


def enter8(event):
    sharpnes.config(fg='grey')

def leave8(event):
    sharpnes.config(fg='black')


def enter9(event):
    color.config(fg='grey')

def leave9(event):
    color.config(fg='black')


def enter10(event):
    rotate.config(fg='grey')

def leave10(event):
    rotate.config(fg='black')


def enter11(event):
    poster.config(fg='grey')

def leave11(event):
    poster.config(fg='black')

def enter12(event):
    brightness.config(fg='grey')

def leave12(event):
    brightness.config(fg='black')

def enter15(event):
    blurr.config(fg='grey')

def leave15(event):
    blurr.config(fg='black')

def enter13(event):
    button6.config(bg='grey',fg='black',relief=SUNKEN)

def leave13(event):
    button6.config(bg='black',fg='white',relief=RAISED)

def enter14(event):
    button7.config(bg='grey',fg='black',relief=SUNKEN)

def leave14(event):
    button7.config(bg='black',fg='white',relief=RAISED)


master.geometry('600x500+600+200')
master.title('Image Editor')
master.config(background='white')
label = Label(master,text='Welcome To The Photo Editor!',bg='white',fg='aqua',font='chiller 40 bold italic').pack(side=TOP)
openfile = Button(master,text='Choose Picture',bg='black',fg='white',activeforeground='black',activebackground='white',font='cursive 12 bold italic',cursor='hand2',command=choose)
openfile.pack(padx=10,pady=20)
openfile.bind('<Enter>',enter6)
openfile.bind('<Leave>',leave6)

label1 = Label(master,bg='white',fg='red',font='cursive 10 bold italic')
label1.pack(pady=10)

contrast = Button(master,text='Contrast: ',font='cursive 10 bold italic',bg='white', command=contrast1,fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
contrast.place(x=150,y=200)
contrast_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
contrast_.place(x=215,y=202)
contrast.bind('<Enter>',enter7)
contrast.bind('<Leave>',leave7)

sharpnes = Button(master,text='Sharpness :',command=sharpness1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
sharpnes.place(x=150,y=250)
sharpnes_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
sharpnes_.place(x=230,y=252)
sharpnes.bind('<Enter>',enter8)
sharpnes.bind('<Leave>',leave8)

color = Button(master,text='Color: ',command=color1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
color.place(x=150,y=300)
color_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
color_.place(x=200,y=302)
color.bind('<Enter>',enter9)
color.bind('<Leave>',leave9)

rotate = Button(master,text='Rotate:',command=rotate1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
rotate.place(x=350,y=200)
rotate_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
rotate_.place(x=400,y=202)
rotate.bind('<Enter>',enter10)
rotate.bind('<Leave>',leave10)

brightness = Button(master,text='Brightness:',command=brightness1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
brightness.place(x=350,y=300)
brightness_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
brightness_.place(x=425,y=302)
brightness.bind('<Enter>',enter12)
brightness.bind('<Leave>',leave12)

poster= Button(master,text='Posterize:',command=poster1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
poster.place(x=350,y=250)
poster_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
poster_.place(x=415,y=252)
poster.bind('<Enter>',enter11)
poster.bind('<Leave>',leave11)

blurr= Button(master,text='Blurr : ',command=blur1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
blurr.place(x=260,y=350)
blurr_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
blurr_.place(x=305,y=352)
blurr.bind('<Enter>',enter15)
blurr.bind('<Leave>',leave15)



menubar = Menu(master)
menu = Menu(menubar,tearoff=0)
menu.add_command(label='Credits',command=credits)
menubar.add_cascade(label='Help',menu=menu)
master.config(menu=menubar)

button1= Button(master,text='Pencil Sketch!',command=pencil,bg='black', fg='white',activeforeground='black',activebackground='white',font='curisve 12 bold italic',cursor='hand2')
button1.place(x=5,y=460)
button1.bind('<Enter>',enter1)
button1.bind('<Leave>',leave1)

button2 = Button(master,text='Inverted!',bg='black',command=inverted ,fg='white',activeforeground='black',activebackground='white',font='curisve 12 bold italic',cursor='hand2')
button2.place(x=190,y=460)
button2.bind('<Enter>',enter2)
button2.bind('<Leave>',leave2)

button3 = Button(master,text='Mirror!',bg='black',command=Mirror, fg='white',activeforeground='black',activebackground='white',font='curisve 12 bold italic',cursor='hand2')
button3.place(x=330,y=460)
button3.bind('<Enter>',enter3)
button3.bind('<Leave>',leave3)

button4 = Button(master,text='Black and White!',bg='black',command=Black, fg='white',activeforeground='black',activebackground='white',font='curisve 12 bold italic',cursor='hand2')
button4.place(x=455,y=460)
button4.bind('<Enter>',enter4)
button4.bind('<Leave>',leave4)

button5 = Button(master,text='Customize!',bg='black',command=create, fg='white',activeforeground='black',activebackground='white',font='curisve 12 bold italic',cursor='hand2')
button5.place(x=251,y=420)
button5.bind('<Enter>',enter5)
button5.bind('<Leave>',leave5)

button6 = Button(master,text='Emboss!',bg='black',command=emboss1, fg='white',activeforeground='black',activebackground='white',font='curisve 12 bold italic',cursor='hand2')
button6.place(x=24,y=420)
button6.bind('<Enter>',enter13)
button6.bind('<Leave>',leave13)

button7 = Button(master,text='Enhance Edges!',command=enhance1,bg='black', fg='white',activeforeground='black',activebackground='white',font='curisve 12 bold italic',cursor='hand2')
button7.place(x=455,y=420)
button7.bind('<Enter>',enter14)
button7.bind('<Leave>',leave14)

master.mainloop()
