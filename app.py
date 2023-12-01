import flet as ft 
from flet import *
from Pages.login import MainLogin
from Pages.chat1 import MainChat

print("loading")

def main(page:ft.Page):
    print("Starting.....")
    def fn_views(page):
        return {
            "/login":View(
                route="/",
                controls=[
                    MainLogin(page)
                ]
            ),"/openai":View(
                route="/openai",
                controls=[
                    MainChat(page)
                ]
            )

        }
    print("Go Login ...")
    page.go("/login")
    page.views.append(fn_views(page))
    print(page.pwa)

ft.app(target=main)
