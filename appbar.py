from tkinter import CENTER
import flet as ft
def showMenu(e):
    ft.Page.add(
        ft.Container(
            ft.ListView(
                ft.Text("Docs")
            )
        )
    )
    ft.Page.update()
appbar = ft.AppBar(
    leading = ft.IconButton(ft.icons.MENU, on_click=showMenu),
    leading_width = 40,
    title = ft.Text("Flet", size=18, weight=ft.FontWeight.BOLD),
    center_title = False,

    actions=[
        ft.Container(
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED)
        ),
        ft.Container(
            ft.TextField(prefix_icon=ft.icons.SEARCH, border_radius= 10, height=30, width=150, content_padding=5),
            padding=10
        ),        
    ]
)
