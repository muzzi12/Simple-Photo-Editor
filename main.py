from tkinter import *
from PIL import Image,ImageEnhance,ImageOps,ImageFilter,ImageFont,ImageDraw
import PIL
import cv2
import os
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer
import pyttsx3
import sys
from tkinter.colorchooser import askcolor


master = Tk()
file = ''
contrast2 = 1
sharpness2 = 1
color2 = 1
rotate2 = 0
poster2 = 0
brightness2= 0
blur2 = 0
color_value = '#000000'

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

def on_click1(event):
    mixer.init()
    mixer.music.load('mixkit-arcade-game-jump-coin-216.wav')
    mixer.music.play()


def on_click(event):
    mixer.init()
    mixer.music.load('mixkit-game-click-1114.wav')
    mixer.music.play()

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

def speaklabel(event):
    word = label.cget('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def speakchoose(event):
    word = openfile.cget('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def speakcontrast(event):
    word = contrast.cget('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def speaksharpness(event):
    word = sharpnes.cget('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def speakcolor(event):
    word = color.cget('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def speakposterize(event):
    word = poster.cget('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def speakbrightness(event):
    word = brightness.cget('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def speakrotate(event):
    word = rotate.cget('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def speakblur(event):
    word = blurr.cget('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def speakcustomize(event):
    word = button5.cget('text')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)
    engine.runAndWait()

def ask():
    question = messagebox.askquestion('Photo Editor','Do you want to exit?')
    if question=='yes':
        sys.exit()
    else:
        pass

def text():
    def change_color():
        global color_value
        value = askcolor()
        color_value= value[1]
        text_color.config(bg=color_value)

    def confirm():
        global file
        value_text = text_value.get()
        value_x = x_value.get()
        value_y = y_value.get()
        text_size_value = text_size.get()

        if file=='':
            messagebox.showerror('Photo Editor','Please select a picture!')

        else:
            img = Image.open(file)
            text_img = ImageDraw.Draw(img)
            font = ImageFont.truetype(('arial.ttf'), size=text_size_value)
            text_img.text((int(value_x),int(value_y)),value_text,color_value,font)
            path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                          defaultextension='.png',initialfile='Untitled.jpg',initialdir='D:/edited/')
            try:
                img.save(path)
                os.startfile(path)

            except ValueError:
                pass



    newindow = Toplevel()
    newindow.title('Text')
    newindow.resizable(0,0)
    newindow.geometry('300x200')
    newindow.config(background='')

    label0 = Label(newindow,text='Add Text To Your Picture',bg='white',fg='aqua',font='cursive 15 bold italic')
    label0.pack(side=TOP)
    text1 = Label(newindow,text='Text :',font='cursive 10 bold italic',bg='white',fg='black')
    text1.place(x=5,y=50)
    text_value = Entry(newindow,width=30,fg='red',border=2)
    text_value.place(x=45,y=52)

    label_coordinates = Label(newindow,text='Coordinates : ',font='curisve 10 bold italic',fg='black',bg='white').place(x=5,y=100)
    x_label = Label(newindow,text='X =',bg='white',fg='red',font='cursive 10 bold italic').place(x=100,y=100)
    x_value = Entry(newindow,width=4,border=2)
    x_value.place(x=125,y=101)

    y_label = Label(newindow,text='Y =',bg='white',fg='red',font='cursive 10 bold italic').place(x=160,y=100)
    y_value = Entry(newindow,width=4,border=2)
    y_value.place(x=185,y=101)

    text_color_label = Button(newindow,text='Text-Color :',font='cursive 10 bold italic',bg='white',border=0,cursor='hand2',activebackground='white',command=change_color).place(x=5,y=130)
    text_color = Label(newindow,width=3,bg='white')
    text_color.place(x=90,y=132)

    text_size_label = Label(newindow,text='Size :',font='cursive 10 bold italic',bg='white').place(x=5,y=160)
    text_size = Scale(newindow,from_=5,to=200,resolution=5,width=5,orient=HORIZONTAL,bg='white',length=220)
    text_size.place(x=50,y=160)

    menubar1 = Menu(newindow)
    menu5 = Menu(newindow,tearoff=0)
    menu5.add_command(label='Confirm Changes',command=confirm)
    menubar1.add_cascade(label='Text',menu=menu5)
    newindow.config(menu=menubar1)


master.geometry('565x450+600+200')
master.title('Image Editor')
master.resizable(0,0)
master.protocol('WM_DELETE_WINDOW',ask)
master.config(background='white')
label = Label(master,text='Welcome To The Photo Editor!',bg='white',fg='aqua',font='chiller 40 bold italic')
label.pack(side=TOP)
label.bind('<Button-3>',speaklabel)

openfile = Button(master,text='Choose Picture',bg='black',fg='white',activeforeground='black',activebackground='white',font='cursive 12 bold italic',cursor='hand2',command=choose)
openfile.pack(padx=10,pady=20)
openfile.bind('<Enter>',enter6)
openfile.bind('<Button-1>',on_click1)
openfile.bind('<Button-3>',speakchoose)
openfile.bind('<Leave>',leave6)

label1 = Label(master,bg='white',fg='red',font='cursive 10 bold italic')
label1.pack(pady=10)

contrast = Button(master,text='Contrast: ',font='cursive 10 bold italic',bg='white', command=contrast1,fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
contrast.place(x=150,y=200)
contrast_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
contrast_.place(x=215,y=202)
contrast.bind('<Enter>',enter7)
contrast.bind('<Leave>',leave7)
contrast.bind('<Button-1>',on_click1)
contrast.bind('<Button-3>',speakcontrast)

sharpnes = Button(master,text='Sharpness :',command=sharpness1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
sharpnes.place(x=150,y=250)
sharpnes_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
sharpnes_.place(x=230,y=252)
sharpnes.bind('<Enter>',enter8)
sharpnes.bind('<Leave>',leave8)
sharpnes.bind('<Button-1>',on_click1)
sharpnes.bind('<Button-3>',speaksharpness)

color = Button(master,text='Color: ',command=color1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
color.place(x=150,y=300)
color_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
color_.place(x=200,y=302)
color.bind('<Enter>',enter9)
color.bind('<Leave>',leave9)
color.bind('<Button-1>',on_click1)
color.bind('<Button-3>',speakcolor)

rotate = Button(master,text='Rotate:',command=rotate1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
rotate.place(x=350,y=200)
rotate_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
rotate_.place(x=400,y=202)
rotate.bind('<Enter>',enter10)
rotate.bind('<Leave>',leave10)
rotate.bind('<Button-1>',on_click1)
rotate.bind('<Button-3>',speakrotate)

brightness = Button(master,text='Brightness:',command=brightness1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
brightness.place(x=350,y=300)
brightness_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
brightness_.place(x=425,y=302)
brightness.bind('<Enter>',enter12)
brightness.bind('<Leave>',leave12)
brightness.bind('<Button-1>',on_click1)
brightness.bind('<Button-3>',speakbrightness)

poster= Button(master,text='Posterize:',command=poster1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
poster.place(x=350,y=250)
poster_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
poster_.place(x=415,y=252)
poster.bind('<Enter>',enter11)
poster.bind('<Leave>',leave11)
poster.bind('<Button-1>',on_click1)
poster.bind('<Button-3>',speakposterize)

blurr= Button(master,text='Blur : ',command=blur1,font='cursive 10 bold italic',bg='white', fg='black',activeforeground='black',activebackground='white',border=0,cursor='hand2')
blurr.place(x=260,y=350)
blurr_ = Label(master,text='',font='cursive 10 bold italic',bg='white',fg='red')
blurr_.place(x=305,y=352)
blurr.bind('<Enter>',enter15)
blurr.bind('<Leave>',leave15)
blurr.bind('<Button-1>',on_click1)
blurr.bind('<Button-3>',speakblur)

button5 = Button(master,text='Customize!',bg='black',command=create, fg='white',activeforeground='black',activebackground='white',font='curisve 12 bold italic',cursor='hand2')
button5.pack(side=BOTTOM)
button5.bind('<Enter>',enter5)
button5.bind('<Leave>',leave5)
button5.bind('<Button-1>',on_click1)
button5.bind('<Button-3>',speakcustomize)

menubar = Menu(master)
menu = Menu(menubar,tearoff=0)
menu.add_command(label='Credits',command=credits,foreground='red',background='black',activeforeground='black',activebackground='grey',font='cursive 10 bold italic')
menubar.add_cascade(label='Help',menu=menu)
master.config(menu=menubar)

menu2 = Menu(menubar,tearoff=0)
mirror = menu2.add_command(label='Mirror!',command=Mirror,foreground='red',background='black',activeforeground='black',activebackground='grey',font='cursive 10 bold italic')
menu2.bind('<<MenuSelect>>',on_click)
menu.bind('<<MenuSelect>>',on_click)
menu2.add_command(label='Black And White!',command=Black,foreground='red',background='black',activeforeground='black',activebackground='grey',font='cursive 10 bold italic')
menu2.add_command(label='Enhance Edges!',command=enhance1,foreground='red',background='black',activeforeground='black',activebackground='grey',font='cursive 10 bold italic')
menubar.add_cascade(label='Filters',menu=menu2)

menu3 = Menu(menu2,tearoff=0)
menu3.add_command(label='Emboss!',command=emboss1,foreground='red',background='yellow',activeforeground='red',activebackground='grey',font='cursive 10 bold italic')
menu3.add_command(label='Invert!',command=inverted,foreground='red',background='yellow',activeforeground='red',activebackground='grey',font='cursive 10 bold italic')
menu3.add_command(label='Pencil Sketch!',command=emboss1,foreground='red',background='yellow',activeforeground='red',activebackground='grey',font='cursive 10 bold italic')
menu2.add_cascade(label='Specials',menu=menu3,foreground='red',background='black',activeforeground='black',activebackground='grey',font='cursive 10 bold italic')
menu3.bind('<<MenuSelect>>',on_click)

menu4 = Menu(menubar,tearoff=0)
menu4.add_command(label='Add Text',foreground='red',background='black',activeforeground='black',activebackground='grey',font='cursive 10 bold italic',command=text)
menubar.add_cascade(label='Text',menu=menu4)
menu4.bind('<<MenuSelect>>',on_click)

master.mainloop()
