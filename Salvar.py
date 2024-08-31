import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
import csv
from Conexao import criar_conexao


def salvar_usuario(nome, email, senha, tipo):
  #  if not nome or  email or  senha or  tipo:
   #     messagebox.showwarning("Erro de Validação", "Todos os campos são obrigatórios.")
    #    return
    
    conexao = criar_conexao()
    if conexao is None:
        return
    
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO usuarios (nome, email, senha, tipo) VALUES (%s, %s, %s, %s)"#
        valores = (nome, email, senha, tipo )#tipo
        cursor.execute(sql, valores)
        conexao.commit()
        messagebox.showinfo("Sucesso", "Usuário salvo com sucesso!")
    except Error as e:
        messagebox.showerror("Erro", f"Erro ao salvar o usuário: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para salvar o paciente no banco de dados
def salvar_paciente(nome, data_nascimento, cpf):
    if not nome or not data_nascimento or not cpf:
        messagebox.showwarning("Erro de Validação", "Todos os campos são obrigatórios.")
        return
    
    conexao = criar_conexao()
    if conexao is None:
        return
    
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO pacientes (nome, data_nascimento, cpf) VALUES (%s, %s, %s)"
        valores = (nome, data_nascimento, cpf)
        cursor.execute(sql, valores)
        conexao.commit()
        messagebox.showinfo("Sucesso", "Paciente salvo com sucesso!")
    except Error as e:
        messagebox.showerror("Erro", f"Erro ao salvar o paciente: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para obter pacientes do banco de dados
def obter_pacientes():
    conexao = criar_conexao()
    pacientes = []
    if conexao is None:
        return pacientes
    
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome FROM pacientes")
        pacientes = cursor.fetchall()
    except Error as e:
        messagebox.showerror("Erro", f"Erro ao obter pacientes: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return pacientes

# Função para salvar um agendamento no banco de dados
def salvar_agendamento(paciente_id, data, hora):
    if not paciente_id or not data or not hora:
        messagebox.showwarning("Erro de Validação", "Todos os campos são obrigatórios.")
        return
    
    conexao = criar_conexao()
    if conexao is None:
        return
    
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO agendamentos (paciente_id, data, hora) VALUES (%s, %s, %s)"
        valores = (paciente_id, data, hora)
        cursor.execute(sql, valores)
        conexao.commit()
        messagebox.showinfo("Sucesso", "Agendamento salvo com sucesso!")
    except Error as e:
        messagebox.showerror("Erro", f"Erro ao salvar o agendamento: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

# Função para gerar relatório de agendamentos
def gerar_relatorio():
    conexao = criar_conexao()
    if conexao is None:
        return
    
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT p.nome, a.data, a.hora FROM agendamentos a JOIN pacientes p ON a.paciente_id = p.id")
        agendamentos = cursor.fetchall()
        
        with open('relatorio_agendamentos.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Paciente', 'Data', 'Hora'])
            writer.writerows(agendamentos)
            
        messagebox.showinfo("Sucesso", "Relatório gerado com sucesso! (relatorio_agendamentos.csv)")
    except Error as e:
        messagebox.showerror("Erro", f"Erro ao gerar o relatório: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            
def obter_pacientes():
    conexao = criar_conexao()
    pacientes = []
    if conexao is None:
        return pacientes
    
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome FROM pacientes")
        pacientes = cursor.fetchall()
    except Error as e:
        messagebox.showerror("Erro", f"Erro ao obter pacientes: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return pacientes