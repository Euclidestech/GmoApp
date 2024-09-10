import customtkinter as ctk
from tkinter import messagebox

def criar_frame_cadastro_funcionario(container):
    frame_cadastro_funcionario = ctk.CTkFrame(container)
    frame_cadastro_funcionario.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Título do Frame
    ctk.CTkLabel(frame_cadastro_funcionario, text="Cadastro Pacientes", font=("Arial", 24)).pack(pady=20)

    # Informações Pessoais
    ctk.CTkLabel(frame_cadastro_funcionario, text="Nome Completo:").place(x=10, y=80)
    entry_nome = ctk.CTkEntry(frame_cadastro_funcionario, width=300, placeholder_text="Nome Completo")
    entry_nome.place(x=10, y=110)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Data de Nascimento:").place(x=10, y=150)
    entry_data_nascimento = ctk.CTkEntry(frame_cadastro_funcionario, width=150, placeholder_text="DD/MM/YYYY")
    entry_data_nascimento.place(x=10, y=180)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Sexo:").place(x=200, y=150)
    combo_sexo = ctk.CTkComboBox(frame_cadastro_funcionario, values=["Masculino", "Feminino", "Outro"])
    combo_sexo.set("Escolha")
    combo_sexo.place(x=200, y=180)

    ctk.CTkLabel(frame_cadastro_funcionario, text="CPF:").place(x=10, y=220)
    entry_cpf = ctk.CTkEntry(frame_cadastro_funcionario, width=150, placeholder_text="CPF")
    entry_cpf.place(x=10, y=250)

    ctk.CTkLabel(frame_cadastro_funcionario, text="RG:").place(x=200, y=220)
    entry_rg = ctk.CTkEntry(frame_cadastro_funcionario, width=150, placeholder_text="RG")
    entry_rg.place(x=200, y=250)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Endereço:").place(x=10, y=290)
    entry_endereco = ctk.CTkEntry(frame_cadastro_funcionario, width=300, placeholder_text="Endereço")
    entry_endereco.place(x=10, y=320)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Telefone:").place(x=10, y=360)
    entry_telefone = ctk.CTkEntry(frame_cadastro_funcionario, width=300, placeholder_text="Telefone")
    entry_telefone.place(x=10, y=390)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Email:").place(x=10, y=430)
    entry_email = ctk.CTkEntry(frame_cadastro_funcionario, width=300, placeholder_text="Email")
    entry_email.place(x=10, y=460)

    # Informações de Trabalho
    ctk.CTkLabel(frame_cadastro_funcionario, text="Cargo:").place(x=500, y=80)
    entry_cargo = ctk.CTkEntry(frame_cadastro_funcionario, width=300, placeholder_text="Cargo")
    entry_cargo.place(x=500, y=110)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Departamento:").place(x=500, y=150)
    entry_departamento = ctk.CTkEntry(frame_cadastro_funcionario, width=300, placeholder_text="Departamento")
    entry_departamento.place(x=500, y=180)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Data de Admissão:").place(x=500, y=220)
    entry_data_admissao = ctk.CTkEntry(frame_cadastro_funcionario, width=150, placeholder_text="DD/MM/YYYY")
    entry_data_admissao.place(x=500, y=250)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Tipo de Contrato:").place(x=500, y=290)
    combo_contrato = ctk.CTkComboBox(frame_cadastro_funcionario, values=["CLT", "Temporário", "Estagiário"])
    combo_contrato.set("Escolha")
    combo_contrato.place(x=500, y=320)

    # Informações Médicas
    ctk.CTkLabel(frame_cadastro_funcionario, text="Histórico Médico:").place(x=400, y=360)
    entry_historico_medico = ctk.CTkTextbox(frame_cadastro_funcionario, width=200, height=80)
    entry_historico_medico.place(x=400, y=390)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Vacinas:").place(x=650, y=360)
    entry_vacinas = ctk.CTkTextbox(frame_cadastro_funcionario, width=200, height=80)
    entry_vacinas.place(x=650, y=390)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Alergias:").place(x=400, y=570)
    entry_alergias = ctk.CTkTextbox(frame_cadastro_funcionario, width=200, height=80)
    entry_alergias.place(x=400, y=600)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Medicamentos em Uso:").place(x=10, y=570)
    entry_medicamentos = ctk.CTkTextbox(frame_cadastro_funcionario, width=300, height=80)
    entry_medicamentos.place(x=10, y=600)

    ctk.CTkLabel(frame_cadastro_funcionario, text="Convenio:").place(x=10,y=500)
    convenio = ctk.CTkEntry(frame_cadastro_funcionario,placeholder_text="Nº Convenio")
    convenio.place(x=10,y=530)

    # Função para salvar dados
    def salvar_funcionario_interface():
        nome = entry_nome.get()
        data_nascimento = entry_data_nascimento.get()
        sexo = combo_sexo.get()
        cpf = entry_cpf.get()
        rg = entry_rg.get()
        endereco = entry_endereco.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        cargo = entry_cargo.get()
        departamento = entry_departamento.get()
        data_admissao = entry_data_admissao.get()
        contrato = combo_contrato.get()
        historico_medico = entry_historico_medico.get("1.0", "end")
        vacinas = entry_vacinas.get("1.0", "end")
        alergias = entry_alergias.get("1.0", "end")
        medicamentos = entry_medicamentos.get("1.0", "end")

        if not nome or not data_nascimento or not sexo or not cpf or not rg or not endereco or not telefone or not email or not cargo or not departamento or not data_admissao or not contrato:
            messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios.")
        else:
            # Aqui você pode adicionar a lógica para salvar as informações, por exemplo, em um banco de dados
            messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso.")
            # Limpar campos após salvar
            entry_nome.delete(0, 'end')
            entry_data_nascimento.delete(0, 'end')
            combo_sexo.set("Escolha")
            entry_cpf.delete(0, 'end')
            entry_rg.delete(0, 'end')
            entry_endereco.delete(0, 'end')
            entry_telefone.delete(0, 'end')
            entry_email.delete(0, 'end')
            entry_cargo.delete(0, 'end')
            entry_departamento.delete(0, 'end')
            entry_data_admissao.delete(0, 'end')
            combo_contrato.set("Escolha")
            entry_historico_medico.delete("1.0", "end")
            entry_vacinas.delete("1.0", "end")
            entry_alergias.delete("1.0", "end")
            entry_medicamentos.delete("1.0", "end")
    
    btn_salvar_funcionario = ctk.CTkButton(frame_cadastro_funcionario, text="Salvar Funcionário", command=salvar_funcionario_interface)
    btn_salvar_funcionario.place(x=200, y=950)

    return frame_cadastro_funcionario
