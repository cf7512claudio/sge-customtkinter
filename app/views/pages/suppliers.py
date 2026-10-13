import customtkinter as ctk
from app.views.pages.base_page import BasePage
from PIL import Image

class SuppliersPage(BasePage):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.icon_title = ctk.CTkImage(light_image= Image.open("app/assets/supplier.png"), dark_image= Image.open("app/assets/supplier.png"), size= (32,32))

        self.title = ctk.CTkLabel(self, text=" FORNECEDORES", image= self.icon_title, compound= "left", font=("Helvetica", 28, "bold"), text_color="#FCFCFC")
        self.title.pack(pady=30, padx= 50, anchor= ctk.NW)