import flet as ft 
from flet import *
from modules.chataiM import * 
from Pages.login import *

class ChatStyle(UserControl):
    def __init__(self,name,replay):
        super().__init__()
        self.name=name+" :"
        self.replay=replay
        
    def build(self):
        def copy_msg(e):
            self.page.set_clipboard(self.replay)
            
        return Container(
            padding=15,
            border_radius=10,
            content=Column(
                [
                    Text(self.name,color="#ffffff"),
                    Text(self.replay,color="white"), 
                    Divider(height=1,color="white"),
                    Row(
                        [
                            IconButton(
                                icon=icons.COPY,
                                icon_color="white",
                                icon_size=20,
                                tooltip="copy message",
                                on_click=copy_msg
                            )
                        ]
                    )
                ]
            )     
        )


class MainChat(UserControl):
    def __init__(self,page):
        super().__init__()
    
        print("Start Chat")
        self.page = page

        # Page setting 
        self.page.bgcolor = "#ffffff"
        self.page.title = "ChatGPT Chat"

        # Page resize 

        # self.page.window_min_width = 750
        # self.page.window_min_height = 550

        self.page.window_height = 600
        self.page.window_max_height=600
        self.page.window_max_width=1000
        self.page.window_width = 1000

        self.page.scroll = "auto"
        #self.page.window_center()
       
    def build(self):
        def sendMsg(e):
            TextFieldValue = self.pageAdd.controls[1].controls[2].controls[1].controls[0].controls[0]
            print(TextFieldValue.value)
            ChatBody= self.pageAdd.controls[1].controls[2].controls[0].content.controls[0].content
            print(ChatBody.controls)
            ChatBody.controls.append(ChatStyle("Me :",TextFieldValue.value))
            ChatBody.update()
            try:
                
                msg=ChatAi().sendAi(TextFieldValue.value)
                ChatBody.controls.append(ChatStyle("OpenAi :",msg))
            except:
                
                ChatBody.controls.append(ChatStyle("OpenAi :","Sorry, Try Later"))
    
            TextFieldValue.value=''
            TextFieldValue.update()
            TextFieldValue.autofocus=True

            ChatBody.update()
        def clear_msg(e):
            ChatBody= self.pageAdd.controls[1].controls[2].controls[0].content.controls[0].content
            ChatBody.controls.clear()
            self.page.update()
        def fileUploading(e):
            selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
                    )
            selected_files.update()
       
        pick_files_dialog = FilePicker()
        selected_files=Text("")
        self.page.overlay.append(pick_files_dialog)
       
        leftBar=NavigationRail(

            selected_index=0,
            label_type=NavigationRailLabelType.ALL,
            #extended=True,
            min_width=100,
            height=500,
            bgcolor="#383c4a",
            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon_content=Icon(icons.FAVORITE_BORDER,color="#ffffff"), selected_icon=icons.FAVORITE, 
                    label_content=Text("Test 1",color="#ffffff"),
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.BOOKMARK_BORDER,color="#ffffff"),
                    selected_icon_content=Icon(icons.BOOKMARK),
                    label_content=Text("Test 2",color="#ffffff"),
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.SETTINGS_OUTLINED,color="#ffffff"),
                    selected_icon_content=Icon(icons.SETTINGS),
                    label_content=Text("Test 3",color="#ffffff"),
                ),
            ]
        )

        appbar = Container(
                bgcolor="#0078d4",
                height=75,
                border_radius=10,
                content=Row(
                    [
                        Container(
                            padding=padding.only(left=20) ,
                        content=Text('OpenGPT Chat',
                    size=22,
                    color="#FFFFEE", 
                    text_align="start",
                    weight=FontWeight.BOLD,
                )),
                    PopupMenuButton(
                        items=[
                            PopupMenuItem(text="Clear message" ,
                            on_click=clear_msg),
                            PopupMenuItem(text="upload file",
                            on_click=lambda _:pick_files_dialog.pick_files(allow_multiple=True)),  
                            PopupMenuItem(
                                text="Checked item", 
                            checked=False, 
                            ),      
                            PopupMenuItem(text="test"
                            )
                        ]
                    )
                ],alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )
     
        InputChat=TextField(
            hint_text='Enter your text ',
            border_radius=15,
            bgcolor="#f1f1f2",
            color="black",
            border_color='transparent',
            width=320,
            cursor_color="#000000",
            content_padding=20,
            autofocus=True,
            shift_enter=True,  
            multiline=True,
            filled=True,
            expand=True,
        )
       

        ButtonChat = IconButton(
            icon=icons.SEND,
            icon_color="#3476e6",
            icon_size=45,
            tooltip="Send Message",
            on_click=sendMsg,
        )


        DivButttonInput=Column([
        Row(
            [
                InputChat,
                ButtonChat
            ],alignment=ft.CrossAxisAlignment.END
        )
        ])




        ChatMassgBody=Container(
            bgcolor="#000000",
            border_radius = 15,
            margin = margin.only(top=0),
            content=Column(
                height=420,
                 width=self.page.width-100,
                scroll='auto',
                controls=[
                    Container(
                      padding=15,
                    content=Column(
                        [
                          
                           Text("OpenAi Chating",color="white")


                        ]
                    )
                    
                    
                    )
                ]      
            )
            
        )

        # self.page.add(
        #      AppBarStyle,
        #   Row(
        #     [
        #         leftBar,
        #         VerticalDivider(width=1),
        #         Column(spacing=5,controls=[ 
                   
        #             ChatMassgBody,
        #             DivButttonInput
        #         ], alignment=CrossAxisAlignment.END, expand=True),
                
        #     ],
        #    # expand=True,
        # ),
           
        # )
        # self.page.update()

        self.pageAdd=Column([
           appbar,
            
          Row(
            [
                leftBar,
                VerticalDivider(width=1),
                Column(spacing=5,controls=[ 
                   
                    ChatMassgBody,
                    DivButttonInput
                ], alignment=CrossAxisAlignment.END, expand=True),
                
            ],
           # expand=True,
        ),
        ])
        return self.pageAdd
           