import tkinter
import customtkinter
from PIL import Image,ImageTk
import pyperclip

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def pin():
    text_label.set("            Pin Length : ")
    b_pin.configure(fg_color="#144870")
    b_password.configure(fg_color="#1F6AA5",hover_color="#144870")
    option.set(2)
    output.set("")
    entry_output.configure(text_color="white")
    label_3.configure(text_color="grey")
    progressbar.configure(progress_color="grey")
    progressbar.set(0)
    page.update()

def password():
    text_label.set("Password Length : ")
    b_password.configure(fg_color="#144870")
    b_pin.configure(fg_color="#1F6AA5",hover_color="#144870")
    option.set(1)
    output.set("")
    label_3.configure(text_color="white")
    progressbar.configure(progress_color="#30A572")
    progressbar.set(0)
    page.update()

def generate():
    import random
    global img_
    uppercase_bool = False
    lowercase_bool = False
    symbols_bool = False
    digits_bool = False
    # strength()
    n = option.get()
    try:
        uppercase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        lowercase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>' , '(', ')', '<',"!","^","&","_","-","+","=","[","]","{","}","'",'"']
        digits=["1","2","3","4","5","6","7","8","9","0"]
        l = [uppercase,lowercase,symbols,digits]
        password=''
        if n == 1: 
            for i in range (int(entry_len.get())):
                a = random.randint(0,3)
                password=password+(random.choice(l[a]))
        elif n==2:
            for j in range(int(entry_len.get())):
                password=password+(random.choice(digits))
        # print("YOUR PASSWORD IS:",password)
        output.set(password)
        for a in output.get():
            if a in uppercase:
                uppercase_bool = True
            elif a in lowercase:
                lowercase_bool = True
            elif a in symbols:
                symbols_bool = True
            elif a in digits:
                digits_bool = True
        li = [uppercase_bool,lowercase_bool,symbols_bool,digits_bool]
        if li.count(True) == 4 and option.get() == 1:
            progressbar.configure(progress_color="#30A572")
            entry_output.configure(text_color="#30A572")
            progressbar.set(1)
            page.update()
            root.update()
        elif li.count(True) == 3 and option.get() == 1:
            progressbar.configure(progress_color="#FEFF70")
            entry_output.configure(text_color="#FEFF70")
            progressbar.set(0.75)
            page.update()
            root.update()
        elif li.count(True) == 2 and option.get() == 1:
            progressbar.configure(progress_color="red")
            entry_output.configure(text_color="red")
            progressbar.set(0.50)
            page.update()
            root.update()
        elif li.count(True) == 1 and option.get() == 1:
            progressbar.configure(progress_color="red")
            entry_output.configure(text_color="red")
            progressbar.set(0.25)
            page.update()
            root.update()
    except:
        SyntaxError
        
def copy_password():
    import time
    output_password = output.get()
    pyperclip.copy(output_password)
    time.sleep(0.5)
    label_4.place(rely=0.51,relx=0.815)
    page.update()
    time.sleep(1.1)
    label_4.place(rely=1)
    page.update()


root = customtkinter.CTk()
root.geometry("433x433")
root.title("Password Generator")
root.wm_iconbitmap("lock-icon.ico")
root.resizable(False,False)
root.eval('tk::PlaceWindow . center')
root.maxsize(433,400)

copy_image = customtkinter.CTkImage(dark_image=Image.open("copy.png"),size=(30,30))

page = customtkinter.CTkFrame(master=root)

option = tkinter.IntVar()
option.set(1)

b_pin = customtkinter.CTkButton(master=page,text="Pin",font=customtkinter.CTkFont(family="lucida",size=20,weight="bold"),height=40,command=pin)
b_pin.pack()
b_pin.place(anchor=tkinter.CENTER,relx=0.29,rely=0.11)

b_password = customtkinter.CTkButton(master=page,text="Password",fg_color="#144870",font=customtkinter.CTkFont(family="lucida",size=20,weight="bold"),height=40,command=password)
b_password.pack()
b_password.place(anchor=tkinter.CENTER,relx=0.7,rely=0.11)

text_label = tkinter.StringVar()
text_label.set("Password Length : ")

label_1 = customtkinter.CTkLabel(master=page,textvariable=text_label,font=customtkinter.CTkFont(family="lucida",size=21,weight="bold"))
label_1.pack()
label_1.place(rely=0.26,relx=0.09)

entry_len = customtkinter.CTkEntry(master=page,height=40,justify = "center",font=customtkinter.CTkFont(family="lucida",size=20,weight="bold"),placeholder_text="0")
entry_len.pack()
entry_len.place(rely = 0.24,relx=0.55)

label_2 = customtkinter.CTkLabel(master=page,text="Your Password : ",font=customtkinter.CTkFont(family="lucida",size=21,weight="bold"))
label_2.pack()
label_2.place(rely=0.59,relx=0.15)

b_generate = customtkinter.CTkButton(master=page,text="Generate",font=customtkinter.CTkFont(family="lucida",size=20,weight="bold"),height=40,command=generate)
b_generate.pack()
b_generate.place(anchor=tkinter.CENTER,relx=0.5,rely=0.46)

b_copy = customtkinter.CTkButton(master=page,text="",font=customtkinter.CTkFont(family="lucida",size=20,weight="bold"),fg_color="transparent",height=20,width=20,image=copy_image,command=copy_password)
b_copy.pack()
b_copy.place(anchor=tkinter.CENTER,relx=0.93,rely=0.63)


label_4 = customtkinter.CTkLabel(master=page,text="Text copied!",font=customtkinter.CTkFont(family="lucida",size=11,weight="bold"))
# label_4.pack(pady=600,padx=170)

output = tkinter.StringVar()

entry_output = customtkinter.CTkEntry(master=page,height=40,justify = "center",font=customtkinter.CTkFont(family="lucida",size=20,weight="bold"),placeholder_text="0",textvariable=output,state="disabled")
entry_output.pack()
entry_output.place(rely = 0.58,relx=0.55)

label_3 = customtkinter.CTkLabel(master=page,text="Password Strength:",font=customtkinter.CTkFont(family="lucida",size=21,weight="bold"))
label_3.pack()
label_3.place(rely=0.75,relx=0.03)

progressbar = customtkinter.CTkProgressBar(master=page)
progressbar.set(0)
progressbar.pack()
progressbar.place(relx = 0.25,rely = 0.85)

page_image = customtkinter.CTkFrame(master=page,fg_color="transparent")

my_image = customtkinter.CTkImage(dark_image=Image.open("strength0.png"),size=(55, 55))
label_image = customtkinter.CTkLabel(master=page_image,text="",image=my_image)
label_image.pack()
# label_image.place(rely=0.75,relx=0.75)

my_image1 = customtkinter.CTkImage(dark_image=Image.open("ranplay.png"),size=(30, 27))
label_image1 = customtkinter.CTkLabel(master=root,text="",image=my_image1)
label_image1.pack()
label_image1.place(rely=0.93)

# page_image.pack()
page_image.place(rely=0.75,relx=0.75)
# page_image.pack()
page.pack(fill="both",expand=1)

root.mainloop()