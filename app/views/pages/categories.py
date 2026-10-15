import customtkinter as ctk
from app.views.pages.base_page import BasePage
from app.models.category import Category

from PIL import Image
from tkinter import messagebox

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

        self.refresh_list()

    def add_category(self):
        name = self.entry_name.get().strip()

        if not name:
            messagebox.showwarning("ATENÇÃO!", "Prenncha o nome da categoria que deseja adicionar.")
            return

        if Category.select().where(Category.name == name).exists():
            messagebox.showerror("ERRO!", "Esta categoria já está cadastrada!")
            return

        Category.create(name= name)
        messagebox.showinfo("SUCESSO!", "Categoria cadastrada com sucesso.")
        self.entry_name.delete(0, "end")

        self.refresh_list()

    def refresh_list(self):
        for widget in self.set_list_frame.winfo_children():
            widget.destroy()

        categories = Category.select().order_by(Category.name)

        for category in categories:
            frame = ctk.CTkFrame(self.set_list_frame)
            frame.pack(padx=8, pady=8, fill="x")

            name_label = ctk.CTkLabel(frame, text= f"{category.name}")
            name_label.pack(side= "left", padx=8)

            btn_edit = ctk.CTkButton(frame, text= "Editar", corner_radius=12, bg_color="transparent", border_width=2, border_color="#fca311", fg_color= "transparent", hover_color="#848484", font=("Helvetica",14), text_color="#fca311", height=24, width= 65, command= lambda c: self.edit_category(c))
            btn_edit.pack(side= "right", padx=12)

            btn_delete = ctk.CTkButton(frame, text= "Excluir", corner_radius=12, bg_color="transparent", border_width= 2, border_color="#bf4342", fg_color= "transparent", hover_color="#848484", font=("Helvetica",14), text_color="#bf4342", height=24, width= 65, command= lambda c: self.delete_category(c))
            btn_delete.pack(side= "right", padx=12)

    def edit_category(self):
        pass

    def delete_category(self):
        pass

