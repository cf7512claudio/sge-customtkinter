import customtkinter as ctk
from app.models.user import User
from app.views.main_window_view import MainWindow

from tkinter import messagebox

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SGE - LOGIN")
        self.geometry("450x300")
        self.configure(fg_color="#191919")

        TITLE_FONT = ctk.CTkFont(
            family= "Helvetica",
            size= 24,
            weight= "bold"
        )

        self.label_title = ctk.CTkLabel(self, text= "SGE LOGIN", text_color= "#FCFCFC", font= (TITLE_FONT))
        self.label_title.pack(pady=20)

        self.entry_username = ctk.CTkEntry(self, placeholder_text="Nome de usuário...", corner_radius=12, border_width=0, width=300)
        self.entry_username.pack(pady=12)

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Senha...", show="*", corner_radius=12, border_width=0, width=300)
        self.entry_password.pack(pady=16)

        self.button_login = ctk.CTkButton(self, text="Login", corner_radius=12, bg_color="transparent", fg_color="#bf4342", hover_color="#848484", font=("Helvetica",16, "bold"), text_color="#fcfcfc", height=40, command=self.login)
        self.button_login.pack(pady=24)

    def login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        if not username or not password:
            messagebox.showwarning("Atenção!","Preencha todos os campos!")
            return

        try:
            user = User.get(User.username == username)
            if user.verify_password(password):
                # messagebox.showinfo("Logado", "Bem vindo ao SGE!")
                self.destroy()
                MainWindow(user).mainloop()
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos.")
        except User.DoesNotExist:
            messagebox.showerror("Erro", "Usuário não encontrado. Solicite o cadastro no sistema, ou verifique o nome do usuário!")


        