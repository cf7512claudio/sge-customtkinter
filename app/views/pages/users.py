import customtkinter as ctk
from app.views.pages.base_page import BasePage

class UsersPage(BasePage):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ctk.CTkLabel(self, text="USUÁRIOS", font=("Helvetica", 28, "bold"), text_color="#FF7312").pack(pady=30)