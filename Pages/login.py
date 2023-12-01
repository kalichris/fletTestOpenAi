import flet as ft 
from flet import *
from Pages.chat1 import *
import math 

class MainLogin(UserControl):
    def __init__(self,page):
        super().__init__()

        print("Start Login")
        self.page = page

        # Page setting 
        self.page.bgcolor = "#000000"
        self.page.title = "ChatGPT"

        # Page resize 

        self.page.window_min_width = 450
        self.page.window_min_height = 750

        self.page.window_height = 1000
        self.page.window_width = 500

        self.build()
    def build(self):
        print("Start Login Page")
        #self.page.window_center()
        
        def LoginOnClick(self):
            self.page.views.clear()
            self.page.views.append(
                View(
                    "/openai",[
                        MainChat(self.page)
                       
                    ]
                )
            )
            self.page.go("/openai")
           

            
        def SingUpOnClick(self):
            # self.page.views.clear()
            # self.page.views.append(
            #     View(
            #         "/SignIn",[
            #             MainSigun(self.page)
            #         ]
            #     )
            # )
            # self.page.go("/SignIn")
            pass
        
        HeadText = Container(
            Row(
                [
                    Container(
                        Text(
                            "ChatGPT",
                            color = "#ffffff",
                            size = 28,
                            weight = "bold"
                        ), margin = margin.only(top=30,left=50)
                    ) ,Container(
                            CircleAvatar(bgcolor=ft.colors.WHITE, radius=5,width=20,height=20),
                            alignment=ft.alignment.center,
                            margin=margin.only(top=30)

                       ),
                    
                ],spacing=2
            )  
        )


        StartText = Container(
                    Text(
                        "Get started",
                        color = "#ffffff",
                        size = 25 ,
                        weight = "bold",

                    ),
                    alignment = alignment.center,
                               
                 margin=margin.only(top=250))
        
    
        ButtonLogin = Container(
            OutlinedButton(
                "Log in",
                width=400,
                height=50,
                on_click=LoginOnClick,
                style=ButtonStyle(
                    padding=padding.only(top=0),
                   
                    shape={
                        "":RoundedRectangleBorder(radius=5),
                    },color={
                        "":"#fafbff",
                    },bgcolor={
                        '':"#3c46ff"
                    },side={
                        "":BorderSide(2, "#0c161823"),
                        MaterialState.SELECTED:BorderSide(2,"#face15"),
                    },
                ),
            ),
            alignment=alignment.center,
        )
  

        ButtonSingUp =Container(
            OutlinedButton(
                "Sign up",
                width=400,
                height=50,
               # on_click=SingUpOnClick,
                style=ButtonStyle(
                    padding=padding.only(top=0),
                   
                    shape={
                        "":RoundedRectangleBorder(radius=5),
                    },color={
                        "":"#fafbff",
                    },bgcolor={
                        '':"#3c46ff"
                    },side={
                        "":BorderSide(2, "#0c161823"),
                        ft.MaterialState.SELECTED:BorderSide(2,"#face15"),
                    },
                ),
            ),
            alignment=alignment.center
        )


        LabelOpenAi = Container(
            Column(
                [
                    Text(
                        "OpenAi",
                        color='#ffffff',
                        size=22,
                    )
                ]
            ),alignment=alignment.center,margin=margin.only(top=380)
        )

        LinkTeam = Container(
            Row( vertical_alignment=CrossAxisAlignment.CENTER,alignment=MainAxisAlignment.CENTER,
                controls=[
                    Text(
                        "Terms of use",
                        color='#ffffff',
                        size=14
                    ),Container(
                        width = 1,
                        height = 10,
                        bgcolor='#ffffff'
                        
                    ),Text(
                        "Privacy policy",
                        color='#ffffff',
                        size=14
                        
                    )
                ],
            ),alignment=alignment.center
        )

        self.page.add(
            HeadText,
            StartText,
            ButtonLogin,
            ButtonSingUp,
            LabelOpenAi,
            LinkTeam,
        )

        self.page.update()
        def ScreenMediaCheck():
            while True:
                pass #o'
def main (page:ft.Page):
     MainLogin(page)
 
ft.app(target=main,port=3000,view=ft.AppView.WEB_BROWSER)