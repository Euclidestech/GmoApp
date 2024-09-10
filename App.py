import customtkinter as ctk
from tkinter import messagebox
from Salvar import salvar_agendamento, salvar_paciente, salvar_usuario, gerar_relatorio,salvar_prontuario
from PIL import Image
from cadastrouser import criar_frame_cadastro_funcionario



def criar_janela_principal():
    ctk.set_appearance_mode("dark")  
    ctk.set_default_color_theme("dark-blue")  
    janela = ctk.CTk()  
    janela.title("Gerenciador de Saúde Ocupacional")
    janela.geometry("1300x500")
    janela.maxsize(1366,768)
    janela.minsize(1000,700)
   
    
    
    # Menu lateral
    menu_lateral = ctk.CTkFrame(janela, width=100, corner_radius=10)
    menu_lateral.pack(side="left", fill="y", padx=5, pady=0)
    
    #logo app
    icon_logo = ctk.CTkImage(Image.open("Img/logo1.png"),size=(200,50))
    logo_app = ctk.CTkFrame(menu_lateral,width=200,height=50,corner_radius=20)
    logo_app.pack(side="top", fill="none", padx=0, pady=0)
    logo_bt = ctk.CTkLabel(logo_app,image=icon_logo,compound="left",text="")
    logo_bt.place(x=0,y=0)
    
    
    # Botões no menu lateral
    icon_home = ctk.CTkImage(Image.open("Img/icon.png"),size=(20,20))
    btn_Home = ctk.CTkButton(menu_lateral,image=icon_home,compound="left" ,text="Início", command=lambda: mostrar_frame(frame_inicial))
    btn_Home.pack(pady=10)
    
    icon_add = ctk.CTkImage(Image.open("Img/add.png"),size=(20,20))
    btn_cadastro_usuarios = ctk.CTkButton(menu_lateral,image=icon_add,compound="left" ,text="Usuario", command=lambda: mostrar_frame(frame_cadastro_usuarios))
    btn_cadastro_usuarios.pack(pady=10)

    btn_cadastro_pacientes = ctk.CTkButton(menu_lateral,image=icon_add, text="Pacientes", command=lambda: mostrar_frame(frame_cadastro_pacientes))
    btn_cadastro_pacientes.pack(pady=10)
    
    icon_ag = ctk.CTkImage(Image.open("Img/ag.png"),size=(20,20))
    btn_agendamentos = ctk.CTkButton(menu_lateral,image=icon_ag,compound="left", text="Agendamentos", command=lambda:mostrar_frame(frame_agendamentos))
    btn_agendamentos.pack(pady=10)

    icon_rel = ctk.CTkImage(Image.open("Img/rel.png"),size=(20,20))
    btn_relatorios = ctk.CTkButton(menu_lateral,image=icon_rel,compound="left", text="Relatórios", command=lambda: mostrar_frame(frame_relatorios))
    btn_relatorios.pack(pady=10)
    
    icon_conv = ctk.CTkImage(Image.open("Img/conv.png"),size=(20,20))
    btn_convenios = ctk.CTkButton(menu_lateral,image=icon_conv,compound="left",text="Convenios",command=lambda: mostrar_frame(frame_convenios))
    btn_convenios.pack(pady=10)
    
    icon_pront = ctk.CTkImage(Image.open("Img/rel.png"),size=(20,20))  # Novo ícone para o prontuário
    btn_prontuario = ctk.CTkButton(menu_lateral, image=icon_pront, compound="left", text="Prontuário", command=lambda: mostrar_frame(frame_prontuario))
    btn_prontuario.pack(pady=10)
    
    # Área principal da aplicação (Frames)
    container = ctk.CTkFrame(janela, corner_radius=10)
    container.pack(side="right", expand=True, fill="both", padx=5, pady=0)

    # Frames para cada seção
    global frame_cadastro_usuarios, frame_cadastro_pacientes, frame_agendamentos, frame_relatorios, frame_inicial,frame_prontuario
    frame_cadastro_usuarios = ctk.CTkFrame(container)
    frame_cadastro_pacientes = ctk.CTkFrame(container)
    frame_agendamentos = ctk.CTkFrame(container)
    frame_relatorios = ctk.CTkFrame(container)
    frame_inicial = ctk.CTkFrame(container)
    frame_convenios = ctk.CTkFrame(container)
    frame_prontuario = ctk.CTkFrame(container)

    for frame in (frame_cadastro_usuarios, frame_cadastro_pacientes,frame_agendamentos,frame_relatorios, frame_inicial,frame_convenios,frame_prontuario):
        frame.place(x=0, y=0, relwidth=1, relheight=1)
    
    
    
  

    # Conteúdo do frame Cadastro de Usuários
    ctk.CTkLabel(frame_cadastro_usuarios, text="Cadastro de Usuários", font=("Arial", 24)).pack(pady=20)
    ctk.CTkLabel(frame_cadastro_usuarios, text="Nome:").place(x=10,y=80)#pack(pady=5)
    entry_nome = ctk.CTkEntry(frame_cadastro_usuarios,placeholder_text="Nome",width=250)
    entry_nome.place(x=10,y=110)#pack(pady=5)

    ctk.CTkLabel(frame_cadastro_usuarios, text="E-mail:").place(x=300,y=80)#pack(pady=5)
    entry_email = ctk.CTkEntry(frame_cadastro_usuarios,width=200,placeholder_text="E-mail")
    entry_email.place(x=300,y=110)#pack(pady=5)

    ctk.CTkLabel(frame_cadastro_usuarios, text="Data Nascimento:").place(x=550,y=80)#pack(pady=5)
    entry_nascimento = ctk.CTkEntry(frame_cadastro_usuarios,width=200,placeholder_text="Nascimento")
    entry_nascimento.place(x=550,y=110)
    
    ctk.CTkLabel(frame_cadastro_usuarios, text="Sexo:").place(x=370,y=150)
    sexo = ctk.CTkComboBox(frame_cadastro_usuarios,values=["Masculino","Feminino","Outro"])
    sexo.set("Escolha")
    sexo.place(x=370,y=180)
    
    ctk.CTkLabel(frame_cadastro_usuarios, text="Tipo de Usuario:").place(x=200,y=150)
    combo_tipo = ctk.CTkComboBox(frame_cadastro_usuarios,values=["Administrador", "Paciente" , "Funcionario"])
    combo_tipo.set("Escolha")
    combo_tipo.place(x=200,y=180)
    
    ctk.CTkLabel(frame_cadastro_usuarios, text="Senha:").place(x=10,y=150)
    entry_senha = ctk.CTkEntry(frame_cadastro_usuarios, show="*",placeholder_text="Senha")
    entry_senha.place(x=10,y=180)
    

    btn_salvar_usuario = ctk.CTkButton(frame_cadastro_usuarios, text="Cadastrar Usuário",
                                       command=lambda: salvar_usuario(entry_nome.get(), entry_email.get(), entry_senha.get(), combo_tipo.get()))
    btn_salvar_usuario.place(x=200,y=300)

    
    
     # Conteúdo do frame Agendamentos
    ctk.CTkLabel(frame_agendamentos, text="Agendamentos", font=("Arial", 24)).pack(pady=20)
    ctk.CTkLabel(frame_agendamentos, text="Paciente:").place(x=10,y=80)
    entry_paciente = ctk.CTkEntry(frame_agendamentos,width=200)
    entry_paciente.place(x=10,y=110)

    ctk.CTkLabel(frame_agendamentos, text="Data:").place(x=225,y=80)
    entry_data = ctk.CTkEntry(frame_agendamentos)
    entry_data.place(x=220,y=110)

    ctk.CTkLabel(frame_agendamentos, text="Hora:").place(x=400,y=80)
    entry_hora = ctk.CTkEntry(frame_agendamentos)
    entry_hora.place(x=400,y=110)

    btn_salvar_agendamento = ctk.CTkButton(frame_agendamentos, text="Salvar Agendamento", command=salvar_agendamento)
    btn_salvar_agendamento.place(x=300,y=170)
    
    
    
    

    # Conteúdo do frame Cadastro de Pacientes
    ctk.CTkLabel(frame_cadastro_pacientes, text="Cadastro de Pacientes", font=("Arial", 24)).pack(pady=20)
    #ctk.CTkLabel(frame_cadastro_pacientes, text="Nome:").pack(pady=5)
    #entry_nome_paciente = ctk.CTkEntry(frame_cadastro_pacientes)
    #entry_nome_paciente.pack(pady=5)

    #ctk.CTkLabel(frame_cadastro_pacientes, text="Idade:").pack(pady=5)
    #entry_data_nascimento = ctk.CTkEntry(frame_cadastro_pacientes)
    #entry_data_nascimento.pack(pady=5)

    #ctk.CTkLabel(frame_cadastro_pacientes, text="CPF:").pack(pady=5)
    #entry_cpf = ctk.CTkEntry(frame_cadastro_pacientes)
    #entry_cpf.pack(pady=5)

    #btn_salvar_paciente = ctk.CTkButton(frame_cadastro_pacientes, text="Salvar Paciente",
     #                                   command=lambda: salvar_paciente(entry_nome_paciente.get(), entry_data_nascimento.get(), entry_cpf.get()))
    #btn_salvar_paciente.pack(pady=20)
    
    # Conteúdo do frame Convenios
    ctk.CTkLabel(frame_convenios,text="Convenios",font=("Arial", 24)).pack(pady=20)
    
    ctk.CTkLabel(frame_convenios, text="Cadastro de Convênios", font=("Arial", 24)).pack(pady=20)
    
    ctk.CTkLabel(frame_convenios, text="Nome do Convênio:").place(x=10, y=80)
    entry_nome_convenio = ctk.CTkEntry(frame_convenios, width=300, placeholder_text="Nome do Convênio")
    entry_nome_convenio.place(x=10, y=110)

    ctk.CTkLabel(frame_convenios, text="Número do Convênio:").place(x=10, y=150)
    entry_numero_convenio = ctk.CTkEntry(frame_convenios, width=300, placeholder_text="Número do Convênio")
    entry_numero_convenio.place(x=10, y=180)

    ctk.CTkLabel(frame_convenios, text="Telefone:").place(x=10, y=220)
    entry_telefone_convenio = ctk.CTkEntry(frame_convenios, width=300, placeholder_text="Telefone")
    entry_telefone_convenio.place(x=10, y=250)
    
    def salvar_convenio_interface():
        nome = entry_nome_convenio.get()
        numero = entry_numero_convenio.get()
        telefone = entry_telefone_convenio.get()
        if not nome or not numero or not telefone:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
       
            """
        else:
            def salvar_convenio(nome, numero, telefone)
            messagebox.showinfo("Sucesso", "Convênio cadastrado com sucesso.")
            entry_nome_convenio.delete(0, 'end')
            entry_numero_convenio.delete(0, 'end')
            entry_telefone_convenio.delete(0, 'end')
            """
    
    btn_salvar_convenio = ctk.CTkButton(frame_convenios, text="Salvar Convênio", command=salvar_convenio_interface)
    btn_salvar_convenio.place(x=10, y=300)
    
    
    
    
    
    
    
    
    

    # Conteúdo do frame Relatórios
    ctk.CTkLabel(frame_relatorios, text="Relatórios", font=("Arial", 24)).place(x=300,y=50)
    ctk.CTkLabel(frame_relatorios, text="Selecionar Paciente:").place(x=200  , y=100)
    combo_paciente = ctk.CTkEntry(frame_relatorios)
    combo_paciente.place(x=200,y=125)

    ctk.CTkLabel(frame_relatorios, text="Tipo de Relatório:").place(x=400,y=100)
    combo_relatorio = ctk.CTkComboBox(frame_relatorios,values=["Exames","Agendamentos","Consultas"])
    combo_relatorio.set("")
    combo_relatorio.place(x=400,y=125)


    btn_gerar_relatorio = ctk.CTkButton(frame_relatorios, text="Gerar Relatório", command=gerar_relatorio)
    btn_gerar_relatorio.place(x=400,y=200)

    
    
    # Conteúdo do frame Prontuário
    ctk.CTkLabel(frame_prontuario, text="Prontuário Médico", font=("Arial", 24)).pack(pady=20)

    ctk.CTkLabel(frame_prontuario, text="Nome do Paciente:").place(x=10, y=80)
    entry_nome_pront = ctk.CTkEntry(frame_prontuario, placeholder_text="Nome", width=300)
    entry_nome_pront.place(x=10, y=110)

    ctk.CTkLabel(frame_prontuario, text="Idade:").place(x=330, y=80)
    entry_idade_pront = ctk.CTkEntry(frame_prontuario, placeholder_text="Idade", width=100)
    entry_idade_pront.place(x=330, y=110)

    ctk.CTkLabel(frame_prontuario, text="Histórico Médico:").place(x=10, y=150)
    entry_historico_pront = ctk.CTkTextbox(frame_prontuario, width=300, height=80)
    entry_historico_pront.place(x=10, y=180)

    ctk.CTkLabel(frame_prontuario, text="Sintomas:").place(x=330, y=150)
    entry_sintomas_pront = ctk.CTkTextbox(frame_prontuario, width=300, height=80)
    entry_sintomas_pront.place(x=330, y=180)

    ctk.CTkLabel(frame_prontuario, text="Diagnóstico:").place(x=10, y=270)
    entry_diagnostico_pront = ctk.CTkTextbox(frame_prontuario, width=300, height=80)
    entry_diagnostico_pront.place(x=10, y=300)

    ctk.CTkLabel(frame_prontuario, text="Prescrição:").place(x=330, y=270)
    entry_prescricao_pront = ctk.CTkTextbox(frame_prontuario, width=300, height=80)
    entry_prescricao_pront.place(x=330, y=300)

    btn_salvar_prontuario = ctk.CTkButton(frame_prontuario, text="Salvar Prontuário",
                                          command=lambda: salvar_prontuario(entry_nome_pront.get(), entry_idade_pront.get(), 
                                                                            entry_historico_pront.get("1.0", "end"), 
                                                                            entry_sintomas_pront.get("1.0", "end"), 
                                                                            entry_diagnostico_pront.get("1.0", "end"), 
                                                                            entry_prescricao_pront.get("1.0", "end")))
    btn_salvar_prontuario.place(x=250, y=400)



    # Tela inicial
    ctk.CTkLabel(frame_inicial, text="Bem Vindo ao GMO",font=("Arial", 30),width=300).place(x=400,y=10)
    ctk.CTkLabel(frame_inicial, corner_radius=10,text="Infor 1", font=("Arial", 30),text_color="black",width=150,height=70,fg_color="#87CEEB").place(y=70,x=100)
    ctk.CTkLabel(frame_inicial, corner_radius=10,text="Infor 2", font=("Arial", 30),text_color="black",width=150,height=70,fg_color="#87CEEB").place(y=70,x=300)
    ctk.CTkLabel(frame_inicial, corner_radius=10,text="Infor 3", font=("Arial", 30),text_color="black",width=150,height=70,fg_color="#87CEEB").place(y=70,x=500)
    ctk.CTkLabel(frame_inicial, corner_radius=10,text="Infor 4", font=("Arial", 30),text_color="black",width=150,height=70,fg_color="#87CEEB").place(y=70,x=700)
    ctk.CTkLabel(frame_inicial, corner_radius=10,text="Infor 5", font=("Arial", 30),text_color="black",width=150,height=70,fg_color="#87CEEB").place(y=70,x=900)

    frame_cadastro_funcionario = criar_frame_cadastro_funcionario(frame_cadastro_pacientes)
    
    def mostrar_frame(frame):
        frame.tkraise()

    mostrar_frame(frame_inicial)  
    janela.mainloop()


if __name__ == "__main__":
    criar_janela_principal()
