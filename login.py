import tkinter as tk
from tkinter import messagebox
from App import criar_janela_principal
from customtkinter import *
import customtkinter as ctk
from PIL import Image


def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "123":
        root.destroy()
        criar_janela_principal()
    else:
        ctk.CTkMessagebox(title="Erro", message="Usuário ou senha incorretos", icon="cancel").show()

def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.configure(show='')
        show_password_button.configure(text='')
    else:
        password_entry.configure(show='*')
        show_password_button.configure(text='')



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue") 
root = ctk.CTk()
root.title("Tela de Login")
root.geometry("600x310")
root.maxsize(550,310)
root.minsize(550,310)

logo = CTkImage(Image.open("Img/logo.png"),size=(255,300))
logo_inicial = ctk.CTkFrame(root, width=270, corner_radius=10,fg_color="#143548")
logo_inicial.pack(side="left", fill="y", padx=0, pady=0)
btn = ctk.CTkLabel(logo_inicial,image=logo,compound="left",text="")
btn.place(x=0,y=2)

username_label = ctk.CTkLabel(root, text="Usuário:")
username_label.place(x=300,y=60)

username_entry = ctk.CTkEntry(root, width=200)
username_entry.place(x=300,y=90)

password_label = ctk.CTkLabel(root, text="Senha:")
password_label.place(x=300,y=120)

password_entry = ctk.CTkEntry(root, show="*", width=200)
password_entry.place(y=150,x=300)

olho = CTkImage(Image.open("Img/olho.png"),size=(20,20))
loginT = ctk.CTkLabel(root,text="Login",font=("Arial", 24,"bold"),text_color="#F0F8FF").place(y=20,x=360)
show_password_button = ctk.CTkButton(root,image=olho, text="", command=toggle_password,width=10,fg_color="transparent")
show_password_button.place(y=150,x=500)

login_button = ctk.CTkButton(root,font=("Arial",14,"bold") ,text="Entrar",fg_color="#00FA9A",text_color="black",hover_color="#006400",width=100,command=login)
login_button.place(y=200,x=360)

root.mainloop()
