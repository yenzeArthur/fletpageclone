from ctypes import alignment
from tkinter import Button
import flet as ft

mainImage = ft.Container(
    alignment=ft.alignment.top_left,
    content = ft.Image(
        src=f"https://flet.dev/img/pages/home/flet-home.png",
        width=540,
        height=540,
        fit=ft.ImageFit.FILL
    )
)

fletDefinition = ft.Container(
    width=540,
    height=540,
    content=ft.Column(controls=[
            ft.Text(
                "The fastest way to build flutter apps in python",
                size=55,
                color="#19A7CE",
                weight=ft.FontWeight.BOLD,
            ),
            ft.Text(),
            ft.Text("Flet enables developers to easily build realtime web, mobile and desktop apps in python. No frontend experience required.",
                size=25,
                ),
            ft.Text(),
            ft.Column(
                alignment=ft.alignment.center,
                controls=[
                ft.ElevatedButton(
                width=160, 
                height=50,
                bgcolor="pink",
                content=ft.Container(
                    width=95,
                    content=ft.Row([ft.Text("Get Started",color="white", size=18)]),
            ))

            ])
    ]
    )
)

description = ft.Container(
    alignment=ft.alignment.center,
    content=ft.Text("Main Features", size=30, weight=ft.FontWeight.BOLD)
)

rowElementOne=ft.Container(
        content=ft.Column(
            width=350,
            height=350,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Icon(name=ft.icons.BOLT, color="blue", size=80)),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("From Idea to app in minutes", weight=ft.FontWeight.BOLD, size=20),
                ),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("An internal tool or a dashboard for your team, weekend project, data entry form, kiosk app or high-fidelity prototype - Flet is an ideal framework to quickly hack a great-looking interactive apps to serve a group of users.",
                    size=18,
                    text_align=ft.TextAlign.CENTER),
                ),
            ]
        )
    )

rowElementTwo=ft.Container(
        content=ft.Column(
            width=350,
            height=350,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Icon(name=ft.icons.HOME_ROUNDED, color="blue", size=80)),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Simple Architechure", weight=ft.FontWeight.BOLD, size=20),
                ),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("No more complex architecture with JavaScript frontend, REST API backend, database, cache, etc. With Flet you just write a monolith stateful app in Python only and get multi-user, realtime Single-Page Application (SPA).",
                    size=18,
                    text_align=ft.TextAlign.CENTER),
                ),
            ]
        )
    )

rowElementThree=ft.Container(
        content=ft.Column(
            width=350,
            height=350,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Icon(name=ft.icons.BATTERY_SAVER_ROUNDED, color="blue", size=80)),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Batteries Included", weight=ft.FontWeight.BOLD, size=20)
                ),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("To start developing with Flet, you just need your favorite IDE or text editor. No SDKs, no thousands of dependencies, no complex tooling - Flet has built-in web server with assets hosting and desktop clients.",
                    size=18,
                    text_align=ft.TextAlign.CENTER),
                ),
            ]
        )
    )

rowElementFour=ft.Container(
        content=ft.Column(
            width=350,
            height=350,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Icon(name=ft.icons.FLUTTER_DASH, color="blue", size=80)),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Powered by Flutter", weight=ft.FontWeight.BOLD, size=20)
                ),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Flet UI is built with Flutter, so your app looks professional and can be delivered to any platform. Flet simplifies Flutter model by combining smaller \"widgets\" into ready-to-use \"controls\" with imperative programming model.",
                    size=18,
                    text_align=ft.TextAlign.CENTER),
                ),
            ]
        )
    )

rowElementFive=ft.Container(
        content=ft.Column(
            width=350,
            height=350,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Icon(name=ft.icons.LANGUAGE_ROUNDED, color="blue", size=80)),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Speaks your language", weight=ft.FontWeight.BOLD, size=20)
                ),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Flet is language-agnostic, so anyone on your team could develop Flet apps in their favorite language. Python is already supported, Go, C# and others are coming next.",
                    size=18,
                    text_align=ft.TextAlign.CENTER),
                ),
            ]
        )
    )

rowElementSix=ft.Container(
        content=ft.Column(
            width=350,
            height=350,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Icon(name=ft.icons.PHONE_ANDROID_ROUNDED, color="blue", size=80)),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Deliver to any device", weight=ft.FontWeight.BOLD, size=20)
                ),
                ft.Text(),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Deploy Flet app as a web app and view it in a browser. Package it as a standalone desktop app for Windows, macOS and Linux. Install it on mobile as PWA or view via Flet app for iOS and Android.",
                    size=18,
                    text_align=ft.TextAlign.CENTER),
                ),
            ]
        )
    )

newsletter=ft.ListView(
    controls=[
        ft.Text("Subscribe to Flet newsletter for project updates and tutorials!", text_align=ft.TextAlign.CENTER,
        size=18, weight=ft.FontWeight.BOLD),
        ft.Container(
            alignment=ft.alignment.center,
            content=ft.TextField(label="Your email address", width=700, height=40, border_color="blue")
        )
    ]
)