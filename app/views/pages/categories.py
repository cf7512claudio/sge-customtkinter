import customtkinter as ctk
from app.views.pages.base_page import BasePage
from PIL import Image

class CategoriesPage(BasePage):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.icon_title = ctk.CTkImage(light_image= Image.open("app/assets/grids.png"), dark_image= Image.open("app/assets/grids.png"), size= (32,32))


        self.title = ctk.CTkLabel(self, text=" CATEGORIAS", image= self.icon_title, compound= "left", font=("Helvetica", 28, "bold"), text_color="#FCFCFC")
        self.title.pack(pady=30, padx= 50, anchor= ctk.NW)

        self.description = ctk.CTkLabel(self, text="Gerencie as categorias do seu sistema.", font= ("Helvetica", 16, "italic"), text_color= "#AEACB9")
        self.description.pack(pady=0)

        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady= 20, padx= 300, fill= "x")

        self.form_title = ctk.CTkLabel(self.form_frame, text="Cadastro de Categorias", font=("Helvetica", 22, "bold"))
        self.form_title.pack(pady=10)

        self.entry_name = ctk.CTkEntry(self.form_frame, placeholder_text= "Nome da categoria...")
        self.entry_name.pack(pady= 5, padx= 15, fill= "x")

        self.btn_add = ctk.CTkButton(self.form_frame, text="Adicionar Categoria", corner_radius=12, bg_color="transparent", fg_color="#bf4342", hover_color="#848484", font=("Helvetica",16, "bold"), text_color="#fcfcfc", height=40, command=self.add_category)
        self.btn_add.pack(pady=10)

        self.set_list_frame = ctk.CTkScrollableFrame(self, label_text= "Categorias Cadastradas", label_font= ("", 18, "bold"))
        self.set_list_frame.pack(pady= 5, padx= 300, fill= "both", expand= True)


    def add_category(self):
        pass