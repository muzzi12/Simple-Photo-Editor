from tkinter import *
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageFont, ImageDraw,ImageTk
import PIL
import cv2
import os
from tkinter import filedialog
from tkinter import messagebox
import pyttsx3
from pyttsx3.drivers import sapi5
import sys
from tkinter.colorchooser import askcolor
import winsound
from datetime import date
import time
import webbrowser as wb


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

splash_root = Tk()
img = Image.open('E:\pycharmprojects\Video_Editor\Cortex_premium.jpg')
img1 = ImageTk.PhotoImage(img)
label = Label(splash_root,image=img1).pack()

file = ''
contrast2 = 1
sharpness2 = 1
color2 = 1
rotate2 = 0
poster2 = 0
brightness2 = 0
blur2 = 0
color_value = '#000000'

def main():
    splash_root.destroy()

    master = Tk()
    master.wm_iconbitmap('Cortex.ico')
    def create():
        if file == '':
            messagebox.showerror('Cortex', 'Please select a picture')
        else:

            if poster2 == 0 and brightness2 == 0:
                try:
                    contrast_value = float(contrast2)
                    sharpness_value = float(sharpness2)
                    color_value = float(color2)
                    rotate_value = rotate2
                    blur_value = float(blur2)
                    img = Image.open(file)
                    contrast_create = PIL.ImageEnhance.Contrast(img).enhance((contrast_value))
                    color_create = PIL.ImageEnhance.Color(contrast_create).enhance((color_value))
                    sharpness_create = PIL.ImageEnhance.Sharpness(color_create).enhance((sharpness_value))
                    img1 = sharpness_create.filter(ImageFilter.GaussianBlur(radius=(blur_value)))
                    img2 = img1.rotate(int(rotate_value))
                    final = img2.resize((1920, 1080))
                    path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                        defaultextension='.png', initialfile='Untitled.jpg',
                                                        initialdir='D:/edited/')
                    final.save(path)
                    os.startfile(path)
                except ValueError:
                    pass

            elif poster2 == 0:
                try:
                    contrast_value = float(contrast2)
                    sharpness_value = float(sharpness2)
                    brightness_value = float(brightness2)
                    color_value = float(color2)
                    rotate_value = rotate2
                    blur_value = float(blur2)
                    img = Image.open(file)
                    contrast_create = PIL.ImageEnhance.Contrast(img).enhance((contrast_value))
                    color_create = PIL.ImageEnhance.Color(contrast_create).enhance((color_value))
                    sharpness_create = PIL.ImageEnhance.Sharpness(color_create).enhance((sharpness_value))
                    img2 = sharpness_create.filter(ImageFilter.GaussianBlur(radius=(blur_value)))
                    img1 = PIL.ImageEnhance.Brightness(img2).enhance((brightness_value))
                    img3 = img1.rotate(int(rotate_value))

                    final = img3.resize((1920, 1080))
                    path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                        defaultextension='.png', initialfile='Untitled.jpg',
                                                        initialdir='D:/edited/')
                    final.save(path)
                    os.startfile(path)
                except ValueError:
                    pass

            elif brightness2 == 0:
                try:
                    contrast_value = float(contrast2)
                    sharpness_value = float(sharpness2)
                    poster_value = (poster2)
                    color_value = float(color2)
                    rotate_value = rotate2
                    blur_value = float(blur2)
                    img = Image.open(file)
                    contrast_create = PIL.ImageEnhance.Contrast(img).enhance((contrast_value))
                    color_create = PIL.ImageEnhance.Color(contrast_create).enhance((color_value))
                    sharpness_create = PIL.ImageEnhance.Sharpness(color_create).enhance((sharpness_value))
                    img2 = sharpness_create.filter(ImageFilter.GaussianBlur(radius=(blur_value)))

                    img3 = img2.rotate(int(rotate_value))



                    final = img3.resize((1920, 1080))
                    path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                        defaultextension='.png', initialfile='Untitled.jpg',
                                                        initialdir='D:/edited/')
                    final.save(path)
                    os.startfile(path)

                except ValueError:
                    pass

            else:
                try:
                    contrast_value = float(contrast2)
                    sharpness_value = float(sharpness2)
                    color_value = float(color2)
                    brightness_value = float(brightness2)
                    rotate_value = rotate2
                    poster_value = (poster2)
                    blur_value = float(blur2)
                    img = Image.open(file)
                    contrast_create = PIL.ImageEnhance.Contrast(img).enhance((contrast_value))
                    color_create = PIL.ImageEnhance.Color(contrast_create).enhance((color_value))
                    sharpness_create = PIL.ImageEnhance.Sharpness(color_create).enhance((sharpness_value))
                    poster_create = PIL.ImageOps.posterize(sharpness_create, (poster_value))
                    img1 = poster_create.filter(ImageFilter.GaussianBlur(radius=(blur_value)))
                    brightness_create = PIL.ImageEnhance.Brightness(img1).enhance((brightness_value))
                    rotate_create = brightness_create.rotate(int(rotate_value))

                    final = rotate_create.resize((1920, 1080))
                    path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                        defaultextension='.png', initialfile='Untitled.jpg',
                                                        initialdir='D:/edited/')

                    final.save(path)
                    os.startfile(path)
                except ValueError:
                    pass

    def pencil():
        global file
        if file == '':
            messagebox.showerror('Cortex', 'Please select a picture!')
        else:
            image = cv2.imread(file)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            inverted = 255 - gray
            blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
            inverted_blurr = 255 - blurred
            pencil = cv2.divide(gray, inverted_blurr, scale=256.0)
            path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                defaultextension='.png', initialfile='Untitled.jpg',
                                                initialdir='D:/edited/')
            try:
                cv2.imwrite(path,pencil)
                os.startfile(path)

            except cv2.error:
                pass

    def emboss1():
        global file
        if file == '':
            messagebox.showerror('Cortex', 'Please select a picture!')
        else:
            img = Image.open(file)
            embossed = img.filter(ImageFilter.EMBOSS())
            path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                defaultextension='.png', initialfile='Untitled.jpg',
                                                initialdir='D:/edited/')
            try:
                embossed.save(path)
                os.startfile(path)
            except ValueError:
                pass

    def enhance1():
        global file
        if file == '':
            messagebox.showerror('Cortex', 'Please select a picture!')
        else:
            img = Image.open(file)
            embossed = img.filter(ImageFilter.EDGE_ENHANCE_MORE())
            path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                defaultextension='.png', initialfile='Untitled.jpg',
                                                initialdir='D:/edited/')
            try:
                embossed.save(path)
                os.startfile(path)
            except ValueError:
                pass

    def choose():
        global file
        path = filedialog.askopenfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                          defaultextension='.png', initialdir='E:/Captures/')
        file = path
        label1.config(text=file)

    def inverted():
        global file
        if file == '':
            messagebox.showerror('Cortex', 'Please select a picture!')
        else:
            img = Image.open(file)
            inverted_image = PIL.ImageOps.invert(img)
            final = inverted_image.resize((1920, 1080))
            path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                defaultextension='.png', initialfile='Untitled.jpg',
                                                initialdir='D:/edited/')
            try:
                final.save(path)
                os.startfile(path)
            except ValueError:
                pass

    def Mirror():
        global file
        if file == '':
            messagebox.showerror('Cortex', 'Please select a picture!')
        else:
            img = Image.open(file)
            im_mirror = ImageOps.mirror(img)
            final = im_mirror.resize((1920, 1080))
            path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                defaultextension='.png', initialfile='Untitled.jpg',
                                                initialdir='D:/edited/')
            try:
                final.save(path)
                os.startfile(path)
            except ValueError:
                pass

    def Black():
        global file
        if file == '':
            messagebox.showerror('Cortex', 'Please select a picture!')
        else:
            img = Image.open(file)
            image_file = img.convert('1')
            final = image_file.resize((1920, 1080))
            path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                defaultextension='.png', initialfile='Untitled.jpg',
                                                initialdir='D:/edited/')
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
            sharpness2 = float(contrast_l.get())
            if sharpness2 > 20:
                messagebox.showerror('Cortex', 'Invalid Value!')
            else:
                sharpnes_.config(text=sharpness2)
                newindow.destroy()

        newindow = Toplevel(master)
        newindow.geometry('250x150+800+400')
        newindow.resizable(0, 0)
        newindow.title('Sharpness')
        newindow.config(background='white')
        contrast_label = Label(newindow, text='Change The Sharpness Of Your Picture', font='cursive 10 bold italic',
                               bg='white', fg='aqua')
        contrast_label.pack(side=TOP)
        contrast_l = Scale(newindow, from_=1, to=20, resolution=0.1, bg='white', orient=HORIZONTAL, cursor='hand2',
                           length=240)
        contrast_l.place(x=1, y=50)
        contrast_button = Button(newindow, text='Confirm!', bg='black', fg='white', activeforeground='black',
                                 activebackground='white', font='cursive 12 bold italic', cursor='hand2',
                                 command=confirm)
        contrast_button.pack(side=BOTTOM)
        contrast_button.bind('<Enter>', enter1)
        contrast_button.bind('<Leave>', leave1)

    def color1():
        def enter1(event):
            color_button.config(bg='grey', fg='black', relief=SUNKEN)

        def leave1(event):
            color_button.config(bg='black', fg='white', relief=RAISED)

        def confirm():
            global color2
            color2 = float(contrast_l.get())
            if color2 > 20:
                messagebox.showerror('Cortex', 'Invalid Value!')
            else:
                color_.config(text=color2)
                newindow.destroy()

        newindow = Toplevel(master)
        newindow.geometry('250x150+800+400')
        newindow.resizable(0, 0)
        newindow.title('Color')
        newindow.config(background='white')
        color_label = Label(newindow, text='Change The Color Of Your Picture', font='cursive 10 bold italic',
                            bg='white', fg='aqua')
        color_label.pack(side=TOP)
        contrast_l = Scale(newindow, from_=1, to=20, resolution=0.1, bg='white', orient=HORIZONTAL, cursor='hand2',
                           length=240)
        contrast_l.place(x=1, y=50)
        color_button = Button(newindow, text='Confirm!', bg='black', fg='white', activeforeground='black',
                              activebackground='white', font='cursive 12 bold italic', cursor='hand2', command=confirm)
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
            poster2 = int(contrast_l.get())
            if poster2 > 8:
                messagebox.showerror('Cortex', 'Invalid Value')
            else:
                poster_.config(text=poster2)
                newindow.destroy()

        newindow = Toplevel(master)
        newindow.geometry('250x150+800+400')
        newindow.resizable(0, 0)
        newindow.title('Posterize')
        newindow.config(background='white')
        contrast_label = Label(newindow, text='Posterize Your Picture', font='cursive 10 bold italic', bg='white',
                               fg='aqua')
        contrast_label.pack(side=TOP)
        contrast_l = Scale(newindow, from_=0, to=8, resolution=1, bg='white', orient=HORIZONTAL,
                           cursor='hand2', length=240)
        contrast_l.place(x=1, y=50)
        contrast_button = Button(newindow, text='Confirm!', bg='black', fg='white', activeforeground='black',
                                 activebackground='white', font='cursive 12 bold italic', cursor='hand2',
                                 command=confirm)
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
            rotate2 = int(contrast_l.get())
            rotate_.config(text=rotate2)
            newindow.destroy()

        newindow = Toplevel(master)
        newindow.geometry('250x150+800+400')
        newindow.resizable(0, 0)
        newindow.title('Rotate')
        newindow.config(background='white')
        contrast_label = Label(newindow, text='Rotate Your Picture', font='cursive 10 bold italic', bg='white',
                               fg='aqua')
        contrast_label.pack(side=TOP)
        contrast_l = Scale(newindow, from_=0, to=360, resolution=5, bg='white', orient=HORIZONTAL, label='Degrees',
                           cursor='hand2', length=240)
        contrast_l.place(x=1, y=50)
        contrast_button = Button(newindow, text='Confirm!', bg='black', fg='white', activeforeground='black',
                                 activebackground='white', font='cursive 12 bold italic', cursor='hand2',
                                 command=confirm)
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
            contrast2 = float(contrast_l.get())
            if contrast2 > 20:
                messagebox.showerror('Cortex', 'Invalid Value!')
            else:
                contrast_.config(text=contrast2)
                newindow.destroy()

        newindow = Toplevel(master)
        newindow.geometry('250x150+800+400')
        newindow.resizable(0, 0)
        newindow.title('Contrast')
        newindow.config(background='white')
        contrast_label = Label(newindow, text='Change The Contrast Of Your Picture', font='cursive 10 bold italic',
                               bg='white', fg='aqua')
        contrast_label.pack(side=TOP)
        contrast_l = Scale(newindow, from_=1, to=20, resolution=0.1, bg='white', orient=HORIZONTAL, cursor='hand2',
                           length=240)
        contrast_l.place(x=1, y=50)
        contrast_button = Button(newindow, text='Confirm!', bg='black', fg='white', activeforeground='black',
                                 activebackground='white', font='cursive 12 bold italic', cursor='hand2',
                                 command=confirm)
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
        newindow.resizable(0, 0)
        newindow.title('Brightness')
        newindow.config(background='white')
        contrast_label = Label(newindow, text='Change The Brightness Of Your Picture', font='cursive 10 bold italic',
                               bg='white', fg='aqua')
        contrast_label.pack(side=TOP)
        contrast_l = Scale(newindow, from_=0, to=20, resolution=0.1, bg='white', orient=HORIZONTAL,
                           cursor='hand2', length=240)
        contrast_l.place(x=1, y=50)
        contrast_button = Button(newindow, text='Confirm!', bg='black', fg='white', activeforeground='black',
                                 activebackground='white', font='cursive 12 bold italic', cursor='hand2',
                                 command=confirm)
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
            blur2 = float(contrast_l.get())
            blurr_.config(text=blur2)
            newindow.destroy()

        newindow = Toplevel(master)
        newindow.geometry('250x150+800+400')
        newindow.resizable(0, 0)
        newindow.title('Blur')
        newindow.config(background='white')
        contrast_label = Label(newindow, text='Blur Your Picture', font='cursive 10 bold italic', bg='white', fg='aqua')
        contrast_label.pack(side=TOP)
        contrast_l = Scale(newindow, from_=0, to=50, resolution=1, bg='white', orient=HORIZONTAL,
                           cursor='hand2', length=240)
        contrast_l.place(x=1, y=50)
        contrast_button = Button(newindow, text='Confirm!', bg='black', fg='white', activeforeground='black',
                                 activebackground='white', font='cursive 12 bold italic', cursor='hand2',
                                 command=confirm)
        contrast_button.pack(side=BOTTOM)
        contrast_button.bind('<Enter>', enter1)
        contrast_button.bind('<Leave>', leave1)

    def on_click1(event):
        winsound.PlaySound('E:\pycharmprojects\Video_Editor\mixkit-modern-click-box-check-1120.wav', winsound.SND_ASYNC)

    def enter5(event):
        button5.config(bg='grey', fg='black', relief=SUNKEN)
        statusbar.config(text='Customize : Customize Your Picture')

    def leave5(event):
        button5.config(bg='#1D0577', fg='white', relief=RAISED)
        statusbar.config(text='')

    def enter6(event):
        openfile.config(bg='grey', fg='black', relief=SUNKEN)
        statusbar.config(text='Choose Picture : Select Any Picture')

    def leave6(event):
        openfile.config(bg='#1D0577', fg='white', relief=RAISED)
        statusbar.config(text='')

    def enter7(event):
        contrast.config(fg='grey')
        statusbar.config(text='Contrast : Enhance The Contrast Of Your Picture!')

    def leave7(event):
        contrast.config(fg='white')
        statusbar.config(text='')

    def enter8(event):
        sharpnes.config(fg='grey')
        statusbar.config(text='Sharpness : Enhance The Sharpness Of Your Picture!')

    def leave8(event):
        sharpnes.config(fg='white')
        statusbar.config(text='')

    def enter9(event):
        color.config(fg='grey')
        statusbar.config(text='Color : Enhance The Color Of Your Picture!')

    def leave9(event):
        color.config(fg='white')
        statusbar.config(text='')

    def enter10(event):
        rotate.config(fg='grey')
        statusbar.config(text='Rotate : Rotate Your Picture!')

    def leave10(event):
        rotate.config(fg='white')
        statusbar.config(text='')

    def enter11(event):
        poster.config(fg='grey')
        statusbar.config(text='Poster : Posterize Your Picture!')

    def leave11(event):
        poster.config(fg='white')
        statusbar.config(text='')

    def enter12(event):
        brightness.config(fg='grey')
        statusbar.config(text='Brightness : Enhance The Brightness Of Your Picture!')

    def leave12(event):
        brightness.config(fg='white')
        statusbar.config(text='')

    def enter15(event):
        blurr.config(fg='grey')
        statusbar.config(text='Blur : Blur Your Picture!')

    def leave15(event):
        blurr.config(fg='white')
        statusbar.config(text='')

    def enter_label(evet):
        statusbar.config(text='Welcome To Cortex')

    def leave_label(evet):
        statusbar.config(text='')

    def enter_time(event):
        statusbar.config(text=f"Time : {(time.strftime('%I:%M %p'))} ")

    def leavetime(event):
        statusbar.config(text="")

    def enter_date(event):
        statusbar.config(text=f'Date : {date.today()}')

    def leavedate(event):
        statusbar.config(text='')

    def enter_label1(event):
        value = label1['text']
        if value == '':
            pass

        else:
            statusbar.config(text=f"File : {label1['text']}")

    def Leave_label1(event):
        statusbar.config(text='')

    def speaklabel(event):
        word = label.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speakchoose(event):
        word = openfile.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speakcontrast(event):
        word = contrast.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speaksharpness(event):
        word = sharpnes.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speakcolor(event):
        word = color.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speakposterize(event):
        word = poster.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speakbrightness(event):
        word = brightness.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speakrotate(event):
        word = rotate.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speakblur(event):
        word = blurr.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speakcustomize(event):
        word = button5.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speaktime(event):
        engine.say('its ' + (time.strftime('%I:%M %p')))
        engine.runAndWait()

    def speaktimelabel(event):
        word = label_time.cget('text')
        engine.say(word)
        engine.runAndWait()

    def speakdate_label(event):
        word = label_date.cget('text')
        engine.say(word)
        engine.runAndWait()

    def ask():
        question = messagebox.askquestion('Cortex', 'Do you want to exit?')
        if question == 'yes':
            sys.exit()
        else:
            pass

    def text():
        def change_color():
            global color_value
            value = askcolor()
            color_value = value[1]
            text_color.config(bg=color_value)

        def confirm():
            global file
            value_text = text_value.get()
            value_x = x_value.get()
            value_y = y_value.get()
            text_size_value = text_size.get()

            if file == '':
                messagebox.showerror('Cortex', 'Please select a picture!')

            else:
                img = Image.open(file)
                text_img = ImageDraw.Draw(img)
                font = ImageFont.truetype(('arial.ttf'), size=text_size_value)
                text_img.text((int(value_x), int(value_y)), value_text, color_value, font)
                path = filedialog.asksaveasfilename(filetypes=[('JPG Files', '*.jpg'), ('PNG Files', '*.png')],
                                                    defaultextension='.png', initialfile='Untitled.jpg',
                                                    initialdir='D:/edited/')
                try:
                    img.save(path)
                    os.startfile(path)

                except ValueError:
                    pass

        newindow = Toplevel()
        newindow.title('Text')
        newindow.resizable(0, 0)
        newindow.geometry('300x200+800+400')
        newindow.config(background='')

        label0 = Label(newindow, text='Add Text To Your Picture', bg='white', fg='aqua', font='cursive 15 bold italic')
        label0.pack(side=TOP)
        text1 = Label(newindow, text='Text :', font='cursive 10 bold italic', bg='white', fg='black')
        text1.place(x=5, y=50)
        text_value = Entry(newindow, width=30, fg='red', border=2)
        text_value.place(x=45, y=52)

        label_coordinates = Label(newindow, text='Coordinates : ', font='curisve 10 bold italic', fg='black',
                                  bg='white').place(x=5, y=100)
        x_label = Label(newindow, text='X =', bg='white', fg='red', font='cursive 10 bold italic').place(x=100, y=100)
        x_value = Entry(newindow, width=4, border=2)
        x_value.place(x=125, y=101)

        y_label = Label(newindow, text='Y =', bg='white', fg='red', font='cursive 10 bold italic').place(x=160, y=100)
        y_value = Entry(newindow, width=4, border=2)
        y_value.place(x=185, y=101)

        text_color_label = Button(newindow, text='Text-Color :', font='cursive 10 bold italic', bg='white', border=0,
                                  cursor='hand2', activebackground='white', command=change_color).place(x=5, y=130)
        text_color = Label(newindow, width=3, bg='white')
        text_color.place(x=90, y=132)

        text_size_label = Label(newindow, text='Size :', font='cursive 10 bold italic', bg='white').place(x=5, y=160)
        text_size = Scale(newindow, from_=5, to=200, resolution=5, width=5, orient=HORIZONTAL, bg='white', length=220)
        text_size.place(x=50, y=160)

        menubar1 = Menu(newindow)
        menu5 = Menu(newindow, tearoff=0)
        menu5.add_command(label='Confirm Changes', command=confirm)
        menubar1.add_cascade(label='Text', menu=menu5)
        newindow.config(menu=menubar1)

    def source():
        wb.open_new_tab('https://github.com/kalinbhaiya/File-Downloader/blob/main/main.py')

    def about():
        messagebox.showinfo('File Downloader', "Author : \nMuhammad Muzammil Alam\
                                                        Author's E-mail Address : \nmuzammil.alam231@gmail.com\
                                                        Author's Github Profile : \nhttps://github.com/kalinbhaiya\
                                                        Author's Facebook Profile : \nhttps://www.facebook.com/profile.php?id=100052280166322 Author's Instagram Profile : \nhttps://www.instagram.com/m.muzammil1231/")

        wb.open_new_tab('https://github.com/kalinbhaiya')
        wb.open_new_tab('https://www.facebook.com/profile.php?id=100052280166322')
        wb.open_new_tab('https://www.instagram.com/m.muzammil1231/')

    def credits():
        messagebox.showinfo('Video Merger',
                            'Photo Editing Software app created by Muhammad Muzammil Alam, if you have any problem regarding this app, you can email to muzammil.alam231@gmail.com. Thanks!')

    def speakdate(event):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        dic = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
               '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
        day = date.today()

        day1 = str(day).replace('-', ' ')
        if day1[5:8] == '01 ':

            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['06'])
            engine.say('its ' + day2)
            engine.runAndWait()

        elif day1[5:8] == '02 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['02'])
            engine.say('its ' + day2)
            engine.runAndWait()

        elif day1[5:8] == '03 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['03'])
            engine.say('its ' + day2)
            engine.runAndWait()

        elif day1[5:8] == '04 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['04'])
            engine.say('its ' + day2)
            engine.runAndWait()

        elif day1[5:8] == '05 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['05'])
            engine.say('its ' + day2)
            engine.runAndWait()

        elif day1[5:8] == '06 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['06'])
            engine.say('its ' + day2)
            engine.runAndWait()

        elif day1[5:8] == '07 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['07'])
            engine.say('its ' + day2)
            engine.runAndWait()

        elif day1[5:8] == '08 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['08'])
            engine.say('its ' + day2)
            engine.runAndWait()

        elif day1[5:8] == '09 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['09'])
            engine.say('its ' + day2)
            engine.runAndWait()

        elif day1[5:8] == '10 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['10'])
            engine.say('its ' + day2)
            engine.runAndWait()

        elif day1[5:8] == '11 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['11'])
            engine.say('its ' + day2)
            engine.runAndWait()

        if day1[5:8] == '12 ':
            day1 = str(day).replace('-', ' ')
            day2 = day1.replace(day1[5:7], dic['12'])
            engine.say('its ' + day2)
            engine.runAndWait()



    master.geometry('567x450')
    master.title('Cortex')
    master.resizable(0, 0)
    master.protocol('WM_DELETE_WINDOW', ask)
    master.config(background='#1D0577')
    label = Label(master, text='Welcome To Cortex!', bg='#1D0577', fg='aqua', font='chiller 60 bold italic')
    label.pack(side=TOP)
    label.bind('<Button-3>', speaklabel)
    label.bind('<Enter>', enter_label)
    label.bind('<Leave>', leave_label)

    openfile = Button(master, text='Choose Picture', bg='#1D0577', fg='white', activeforeground='black',
                      activebackground='white', font='cursive 12 bold italic', cursor='hand2', command=choose)
    openfile.pack(padx=10, pady=10)
    openfile.bind('<Enter>', enter6)
    openfile.bind('<Button-1>', on_click1)
    openfile.bind('<Button-3>', speakchoose)
    openfile.bind('<Leave>', leave6)

    label1 = Label(master, bg='#1D0577', fg='red', font='cursive 10 bold italic')
    label1.pack(pady=10)
    label1.bind('<Enter>', enter_label1)
    label1.bind('<Leave>', Leave_label1)

    contrast = Button(master, text='Contrast: ', font='cursive 10 bold italic', bg='#1D0577', command=contrast1,
                      fg='white', activeforeground='black', activebackground='#1D0577', border=0, cursor='hand2')
    contrast.place(x=150, y=200)
    contrast_ = Label(master, text='', font='cursive 10 bold italic', bg='#1D0577', fg='red')
    contrast_.place(x=215, y=202)
    contrast.bind('<Enter>', enter7)
    contrast.bind('<Leave>', leave7)
    contrast.bind('<Button-1>', on_click1)
    contrast.bind('<Button-3>', speakcontrast)

    sharpnes = Button(master, text='Sharpness :', command=sharpness1, font='cursive 10 bold italic', bg='#1D0577',
                      fg='white', activeforeground='black', activebackground='#1D0577', border=0, cursor='hand2')
    sharpnes.place(x=150, y=250)
    sharpnes_ = Label(master, text='', font='cursive 10 bold italic', bg='#1D0577', fg='red')
    sharpnes_.place(x=230, y=252)
    sharpnes.bind('<Enter>', enter8)
    sharpnes.bind('<Leave>', leave8)
    sharpnes.bind('<Button-1>', on_click1)
    sharpnes.bind('<Button-3>', speaksharpness)

    color = Button(master, text='Color: ', command=color1, font='cursive 10 bold italic', bg='#1D0577', fg='white',
                   activeforeground='black', activebackground='#1D0577', border=0, cursor='hand2')
    color.place(x=150, y=300)
    color_ = Label(master, text='', font='cursive 10 bold italic', bg='#1D0577', fg='red')
    color_.place(x=200, y=302)
    color.bind('<Enter>', enter9)
    color.bind('<Leave>', leave9)
    color.bind('<Button-1>', on_click1)
    color.bind('<Button-3>', speakcolor)

    rotate = Button(master, text='Rotate:', command=rotate1, font='cursive 10 bold italic', bg='#1D0577', fg='white',
                    activeforeground='black', activebackground='#1D0577', border=0, cursor='hand2')
    rotate.place(x=350, y=200)
    rotate_ = Label(master, text='', font='cursive 10 bold italic', bg='#1D0577', fg='red')
    rotate_.place(x=400, y=202)
    rotate.bind('<Enter>', enter10)
    rotate.bind('<Leave>', leave10)
    rotate.bind('<Button-1>', on_click1)
    rotate.bind('<Button-3>', speakrotate)

    brightness = Button(master, text='Brightness:', command=brightness1, font='cursive 10 bold italic', bg='#1D0577',
                        fg='white', activeforeground='black', activebackground='#1D0577', border=0, cursor='hand2')
    brightness.place(x=350, y=300)
    brightness_ = Label(master, text='', font='cursive 10 bold italic', bg='#1D0577', fg='red')
    brightness_.place(x=425, y=302)
    brightness.bind('<Enter>', enter12)
    brightness.bind('<Leave>', leave12)
    brightness.bind('<Button-1>', on_click1)
    brightness.bind('<Button-3>', speakbrightness)#

    poster = Button(master, text='Posterize:', command=poster1, font='cursive 10 bold italic', bg='#1D0577', fg='white',
                    activeforeground='black', activebackground='#1D0577', border=0, cursor='hand2')
    poster.place(x=350, y=250)
    poster_ = Label(master, text='', font='cursive 10 bold italic', bg='#1D0577', fg='red')
    poster_.place(x=415, y=252)
    poster.bind('<Enter>', enter11)
    poster.bind('<Leave>', leave11)
    poster.bind('<Button-1>', on_click1)
    poster.bind('<Button-3>', speakposterize)

    blurr = Button(master, text='Blur : ', command=blur1, font='cursive 10 bold italic', bg='#1D0577', fg='white',
                   activeforeground='black', activebackground='#1D0577', border=0, cursor='hand2')
    blurr.place(x=260, y=350)
    blurr_ = Label(master, text='', font='cursive 10 bold italic', bg='#1D0577', fg='red')
    blurr_.place(x=305, y=352)
    blurr.bind('<Enter>', enter15)
    blurr.bind('<Leave>', leave15)
    blurr.bind('<Button-1>', on_click1)
    blurr.bind('<Button-3>', speakblur)

    statusbar = Label(master, text='', bg='white', bd=2, relief=GROOVE, anchor=W, font='arial 9 italic')
    statusbar.pack(side=BOTTOM, fill=X)

    button5 = Button(master, text='Customize!', bg='#1D0577', command=create, fg='white', activeforeground='black',
                     activebackground='white', font='curisve 12 bold italic', cursor='hand2')
    button5.pack(side=BOTTOM)
    button5.bind('<Enter>', enter5)
    button5.bind('<Leave>', leave5)
    button5.bind('<Button-1>', on_click1)
    button5.bind('<Button-3>', speakcustomize)

    menubar = Menu(master)
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label='Credits',foreground='aqua', background='#1D0577',
                      activeforeground='black', activebackground='grey', font='cursive 10 bold italic', command=credits)
    menu1.add_command(label='Source Code', foreground='aqua', background='#1D0577',
                      activeforeground='black', activebackground='grey', font='cursive 10 bold italic',command=source)
    menu1.add_command(label='About Author', foreground='aqua', background='#1D0577',
                      activeforeground='black', activebackground='grey', font='cursive 10 bold italic',command=about)
    menubar.add_cascade(label='Help', menu=menu1)


    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label='Mirror!', command=Mirror, foreground='aqua', background='#1D0577',
                               activeforeground='black', activebackground='grey', font='cursive 10 bold italic')

    menu2.add_command(label='Black And White!', command=Black, foreground='aqua', background='#1D0577',
                      activeforeground='black', activebackground='grey', font='cursive 10 bold italic')
    menu2.add_command(label='Enhance Edges!', command=enhance1, foreground='aqua', background='#1D0577',
                      activeforeground='black', activebackground='grey', font='cursive 10 bold italic')
    menubar.add_cascade(label='Filters', menu=menu2)

    menu3 = Menu(menu2, tearoff=0)
    menu3.add_command(label='Emboss!', command=emboss1, foreground='#1D0577', background='aqua', activeforeground='red',
                      activebackground='grey', font='cursive 10 bold italic')
    menu3.add_command(label='Invert!', command=inverted, foreground='#1D0577', background='aqua', activeforeground='red',
                      activebackground='grey', font='cursive 10 bold italic')
    menu3.add_command(label='Pencil Sketch!', command=pencil, foreground='#1D0577', background='aqua',
                      activeforeground='red', activebackground='grey', font='cursive 10 bold italic')
    menu2.add_cascade(label='Specials', menu=menu3, foreground='aqua', background='#1D0577', activeforeground='black',
                      activebackground='grey', font='cursive 10 bold italic')

    label_time = Label(master, text='Time', bg='#1D0577', fg='white', font='cursive 12 bold italic')
    label_time.place(x=1, y=400)
    label_time.bind('<Button-1>', speaktime)
    label_time.bind('<Button-3>', speaktimelabel)
    label_time.bind('<Enter>', enter_time)
    label_time.bind('<Leave>', leavetime)

    label_date = Label(master, text='Date', bg='#1D0577', fg='white', font='cursive 12 bold italic')
    label_date.place(x=522, y=400)
    label_date.bind('<Button-1>', speakdate)
    label_date.bind('<Button-3>', speakdate_label)
    label_date.bind('<Enter>', enter_date)
    label_date.bind('<Leave>', leavedate)

    menu4 = Menu(menubar, tearoff=0)
    menu4.add_command(label='Add Text', foreground='aqua', background='#1D0577', activeforeground='black',
                      activebackground='grey', font='cursive 10 bold italic', command=text)
    menubar.add_cascade(label='Text', menu=menu4)
    master.config(menu=menubar)
    master.eval('tk::PlaceWindow . center')
    master.mainloop()

splash_root.after(3000, main)
splash_root.eval('tk::PlaceWindow . center')
splash_root.overrideredirect(True)
splash_root.mainloop()
main()
