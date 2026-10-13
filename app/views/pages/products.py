import customtkinter as ctk
from app.views.pages.base_page import BasePage
from PIL import Image

class ProductsPage(BasePage):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.icon_title = ctk.CTkImage(light_image= Image.open("app/assets/barcode.png"), dark_image= Image.open("app/assets/barcode.png"), size= (32,32))

        self.title = ctk.CTkLabel(self, text=" PRODUTOS", image= self.icon_title, compound= "left", font=("Helvetica", 28, "bold"), text_color="#FCFCFC")
        self.title.pack(pady=30, padx= 50, anchor= ctk.NW)