import flet as ft
import appbar
import body



def main(page: ft.Page):
    page.title = "Flet"
    page.horizontal_alignment = "center"
    page.scroll = "always"
    
    view = ft.Column(
        width=1080,
        controls=[ft.Row(controls=[
            body.mainImage, body. fletDefinition,
        ]),body.description,
        ft.Row(controls=[
            body.rowElementOne,
            body.rowElementTwo,
            body.rowElementThree
        ]),
        ft.Row(controls=[
            body.rowElementFour,
            body.rowElementFive,
            body.rowElementSix
        ]),
        ft.Text(),
        body.newsletter
        ]
    )
    page.add(
        appbar.appbar,
        view      
    )

ft.app(target=main, view=ft.WEB_BROWSER)