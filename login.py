import tkinter as tk
from tkinter import messagebox

# ------------------------- CLASSES -------------------------

class Cliente:
    def __init__(self, nome, cpf, email, telefone, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nEmail: {self.email}\nTelefone: {self.telefone}"


class SistemaCadastro:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        if any(c.cpf == cliente.cpf for c in self.clientes):
            return False
        self.clientes.append(cliente)
        return True

    def autenticar_cliente(self, cpf, senha):
        for cliente in self.clientes:
            if cliente.cpf == cpf and cliente.senha == senha:
                return cliente
        return None

# ------------------------- INTERFACE -------------------------

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("FinanMais - Sistema de Cadastro")
        self.root.geometry("500x550")
        self.root.configure(bg="#EAF6F6")

        self.sistema = SistemaCadastro()

        self.tela_inicial()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------- TELA INICIAL ----------
    def tela_inicial(self):
        self.limpar_tela()

        tk.Label(self.root, text="Bem-vindo ao FinanMais", font=("Arial", 18, "bold"), bg="#EAF6F6", fg="#333").pack(pady=30)

        tk.Button(self.root, text="Entrar na Conta", width=25, height=2, command=self.tela_login, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(self.root, text="Cadastrar Novo Cliente", width=25, height=2, command=self.tela_cadastro, bg="#2196F3", fg="white").pack(pady=10)

    # ---------- TELA DE LOGIN ----------
    def tela_login(self):
        self.limpar_tela()

        tk.Label(self.root, text="Entrar na Conta", font=("Arial", 16, "bold"), bg="#EAF6F6").pack(pady=20)

        self.cpf_login = tk.StringVar()
        self.senha_login = tk.StringVar()

        self.criar_input("CPF:", self.cpf_login)
        self.criar_input("Senha:", self.senha_login, show="*")

        tk.Button(self.root, text="Entrar", command=self.entrar_na_conta, bg="#4CAF50", fg="white", width=20).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial, bg="#bbb").pack(pady=5)

    def entrar_na_conta(self):
        cpf = self.cpf_login.get().strip()
        senha = self.senha_login.get().strip()

        cliente = self.sistema.autenticar_cliente(cpf, senha)

        if cliente:
            self.tela_perfil(cliente)
        else:
            messagebox.showerror("Erro", "CPF ou senha incorretos.")

    # ---------- TELA DE PERFIL ----------
    def tela_perfil(self, cliente):
        self.limpar_tela()

        tk.Label(self.root, text="Perfil do Cliente", font=("Arial", 16, "bold"), bg="#EAF6F6").pack(pady=20)

        tk.Label(self.root, text=str(cliente), bg="#EAF6F6", font=("Arial", 12), justify="left").pack(pady=10)

        tk.Button(self.root, text="Sair", command=self.tela_inicial, bg="#bbb", width=20).pack(pady=10)

    # ---------- TELA DE CADASTRO ----------
    def tela_cadastro(self):
        self.limpar_tela()

        tk.Label(self.root, text="Cadastro de Novo Cliente", font=("Arial", 16, "bold"), bg="#EAF6F6").pack(pady=20)

        self.nome_var = tk.StringVar()
        self.cpf_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.tel_var = tk.StringVar()
        self.senha_var = tk.StringVar()

        self.criar_input("Nome:", self.nome_var)
        self.criar_input("CPF:", self.cpf_var)
        self.criar_input("Email:", self.email_var)
        self.criar_input("Telefone:", self.tel_var)
        self.criar_input("Senha:", self.senha_var, show="*")

        tk.Button(self.root, text="Cadastrar", command=self.cadastrar_cliente, bg="#4CAF50", fg="white", width=20).pack(pady=15)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial, bg="#bbb").pack()

    def criar_input(self, label_text, var, show=None):
        frame = tk.Frame(self.root, bg="#EAF6F6")
        frame.pack(pady=5)
        tk.Label(frame, text=label_text, bg="#EAF6F6", width=10, anchor="w").pack(side="left")
        tk.Entry(frame, textvariable=var, width=30, show=show).pack(side="left")

    def cadastrar_cliente(self):
        nome = self.nome_var.get().strip()
        cpf = self.cpf_var.get().strip()
        email = self.email_var.get().strip()
        telefone = self.tel_var.get().strip()
        senha = self.senha_var.get().strip()

        if not all([nome, cpf, email, telefone, senha]):
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        cliente = Cliente(nome, cpf, email, telefone, senha)
        if self.sistema.adicionar_cliente(cliente):
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self.tela_inicial()
        else:
            messagebox.showerror("Erro", "CPF já cadastrado.")

# ------------------------- EXECUÇÃO -------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
