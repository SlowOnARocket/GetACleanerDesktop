import customtkinter
import subprocess
import time
import os

def button():
    print('installing...')
    button.configure(state='disabled',text="Installing...")
    msg = subprocess.run(['winget', "install", "translucentTB"])
    print(f'{msg}')
    time.sleep(1)
    button.configure(text="Installed")

def button2():
    print('installing...')
    button1.configure(state='disabled',text="Installing...")
    msg = subprocess.run(['winget', "install", "LivelyWallpaper"])
    print(f'{msg}')
    time.sleep(1)
    button1.configure(text="Installed")

def button3():
    print('installing...')
    abutton.configure(state='disabled',text="Installing...")
    msg = subprocess.run(['winget', 'install', 'BeWidgets'])
    print(f'{msg}')
    time.sleep(1)
    abutton.configure(text="Installed")
    

customtkinter.set_appearance_mode('dark')
instance = customtkinter.CTk()
instance.geometry("700x305")
instance.title("GACD V2.0 (Stable)")
instance.iconbitmap("assets/gacd.ico")

translucentTB = customtkinter.CTkLabel(master=instance,text="TranslucentTB (Latest version)",font=('Montserrat Ultra-Bold',18))
translucentTB.place(relx=0.2,rely=0.128, anchor=customtkinter.CENTER)
button = customtkinter.CTkButton(master=instance, text='install',command=button)
button.place(relx=0.88, rely=0.128, anchor='center')


LivelyWallpapers = customtkinter.CTkLabel(master=instance,text="Lively Wallpapers (Latest version)",font=('Montserrat Ultra-Bold',18))
LivelyWallpapers.place(relx=0.21,rely=0.228, anchor=customtkinter.CENTER)
button1 = customtkinter.CTkButton(master=instance, text='install',command=button2)
button1.place(relx=0.88, rely=0.228, anchor='center')


BeWidgets = customtkinter.CTkLabel(master=instance,text="BeWidgets (Latest version)",font=('Montserrat Ultra-Bold',18))
BeWidgets.place(relx=0.17,rely=0.328, anchor=customtkinter.CENTER)
abutton = customtkinter.CTkButton(master=instance, text='install',command=button3)
abutton.place(relx=0.88, rely=0.328, anchor='center')
instance.resizable(False,False)
instance.mainloop()