import customtkinter as ctk
from app.models.user import User
from app.views.pages.dashboard import DashboardPage
from app.views.pages.categories import CategoriesPage
from app.views.pages.products import ProductsPage
from app.views.pages.stock import StockPage
from app.views.pages.suppliers import SuppliersPage
from app.views.pages.users import UsersPage

class MainWindow(ctk.CTk):
    def __init__(self, user):
        super().__init__()

        self.user = user
        self.current_page = None
        self.selected_button = None

        ctk.set_appearance_mode("Dark")

        self.title("SGE - Sistema de Gestão de Estoque")
        self.geometry("1360x768")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color= "#28272D")
        self.sidebar.grid(row=0, column=0, sticky="nswe")
        self.sidebar.grid_rowconfigure(7, weight=1)

        ctk.CTkLabel(self.sidebar, text="MENU", font= ("Helvetica", 16, "bold")).pack(pady=30, padx=50)

        self.create_menu_buttons()

        # Content
        self.content = ctk.CTkFrame(self, corner_radius=0)
        self.content.grid(row=0, column=1, sticky="nswe")

        # Página inicial
        self.show_page(DashboardPage)

    def create_menu_buttons(self):
        buttons = [
            ("Dashboard", DashboardPage),
            ("Produtos", ProductsPage),
            ("Estoque", StockPage),
            ("Categorias", CategoriesPage),
            ("Fornecedores", SuppliersPage),
        ]
        if self.user.role == "admin":
            buttons.append(("Usuários", UsersPage))

        for text, page in buttons:
            btn = ctk.CTkButton(
                self.sidebar,
                text= text,
                width= 176,
                bg_color= "transparent",
                fg_color= "#28272D",
                hover_color= "#1D1C20",
                command= lambda p=page: self.show_page(p)
            )
            btn.pack(pady=4, padx=12)

            # Agora btn já existe
            btn.configure(
                command=lambda b=btn, p=page: self.select_button(b, p)
            )

             # Dashboard começa selecionado
            if page == DashboardPage:
                self.selected_button = btn
                btn.configure(
                    fg_color="#FF7312"
                )

    def select_button(self, button, page):

        SIDEBAR_COLOR = "#28272D"
        SIDEBAR_ACTIVE = "#FF7312"

        # Volta o botão anterior para a cor normal
        if self.selected_button is not None:
            self.selected_button.configure(
                fg_color=SIDEBAR_COLOR
            )

        # Ativa o botão clicado
        button.configure(
            fg_color=SIDEBAR_ACTIVE
        )

        # Guarda o botão selecionado
        self.selected_button = button

        # Mostra a página
        self.show_page(page)

    def show_page(self, page_class):
        # Remover a página atual e mostrar a nova página
        if self.current_page:
            self.current_page.destroy()

        self.current_page = page_class(self.content)
        self.current_page.pack(fill="both", expand=True)