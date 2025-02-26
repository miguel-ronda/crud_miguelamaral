import tkinter as tk 
from tkinter import messagebox 
from crud import create_user,read_users, update_user,delete_user

class CRUDApp: 
    def __init__(self,root):
        self.root = root
        self.root.title("CRUD USUARIOS")

#ccriacao de widgets 
        self.create_widgets()        

    def create_widgets(self):
        #labels
        tk.Label(self.root,text="nome:").grid(row=0,column=0)
        tk.Label(self.root,text="telefone:").grid(row=1,column=0)
        tk.Label(self.root,text="email:").grid(row=2,column=0)
        tk.Label(self.root,text="usuario:").grid(row=3,column=0)
        tk.Label(self.root,text="senha:").grid(row=4,column=0)
              
              
        tk.Label(self.root,text="USER_ID(for update/delete)").grid(row=5,column=0)


        #CRIAR AS CAIXAS PARA DIGITAR OS VALORES
        self.nome_entry = tk.Entry(self.root)
        self.telefone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.usuario_entry = tk.Entry(self.root)
        self.senha_entry = tk.Entry(self.root)
        self.user_id_entry = tk.Entry(self.root)

        self.nome_entry.grid(row=0,column=1)
        self.telefone_entry.grid(row=1,column=1)
        self.email_entry.grid(row=2,column=1)
        self.usuario_entry.grid(row=3,column=1)
        self.senha_entry.grid(row=4,column=1)

        self.user_id_entry.grid(row=5,column=1)
        

        #botoes do crud
        tk.Button(self.root,text="criar usuario",command=self.create_user).grid(row=6,column=0,umnspan=1)
        tk.Button(self.root,text="listar usuario",command=self.create_user).grid(row=6,column=1,umnspan=1)
        tk.Button(self.root,text="alterar usuario",command=self.create_user).grid(row=7,column=0,umnspan=1)
        tk.Button(self.root,text="excluir usuario",command=self.create_user).grid(row=7,column=1,umnspan=1)





     