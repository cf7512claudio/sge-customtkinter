import customtkinter as ctk
from app.utils.init_db import create_tables, create_admin
from app.views.login_view import LoginWindow

PRIMARY_COLOR = "#FF7312"
SECONDARY_COLOR = "#28272D"
TERTIARY_COLOR = "#848484"
TEXT_COLOR = "#FCFCFC"


def main():
    create_tables()
    create_admin()
    app = LoginWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
