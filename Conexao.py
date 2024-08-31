import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='', 
            database='saude_ocupacional'
        )
        if conexao.is_connected():
             messagebox.showerror("conectado")
        return conexao
    except Error as e:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao MySQL: {e}")
        return None