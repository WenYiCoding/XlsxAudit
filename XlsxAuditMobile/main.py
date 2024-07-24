import flet as ft
import asyncio

async def pseudoSplash(page: ft.Page, sleepTime: 3):
    page.padding = ft.padding.only(108, 331.8, 0, 0)
    splashIcon = ft.Image(
        src=f"/icon.png",
        width=150,
        height=150,
        fit=ft.ImageFit.CONTAIN,
    )
    
    page.add(
        ft.SafeArea(
            splashIcon
        )
    )

    await asyncio.sleep(sleepTime)
    page.controls.pop()

APPBAR_HEIGHT = 56
async def home(page: ft.Page):
    page.padding = ft.padding.only(0, 0, 0, 0)

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.HOME),
        leading_width=40,
        title=ft.Text("Home"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        toolbar_height=APPBAR_HEIGHT
    )
    page.bgcolor = "#ffffff"

    fileName = "Choose a file"
    def pick_files_result(e: ft.FilePickerResultEvent):
        fileName = ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        selected_files.value = fileName
        if (fileName != "Cancelled!"):
            pageContents.append(fileLoad_Btn)
        else:
            pageContents.remove(fileLoad_Btn)

        page.update()
        
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    def filePick(e):
        pick_files_dialog.pick_files(
            allow_multiple=False,
            allowed_extensions=["xlsx"],
            file_type=ft.FilePickerFileType.CUSTOM
        )
        filePick_Btn.content = ft.Text(fileName)
        page.update()

    filePick_Btn = ft.ElevatedButton(
        content=ft.Text(fileName),
        on_click=filePick
    )
    
    fileLoad_Btn = ft.ElevatedButton(
        text="Load",
        icon=ft.icons.PLAY_ARROW_SHARP,
        icon_color="green"
    )

    pageContents = [
        ft.Text("Choose an Excel file to load"),
        filePick_Btn,
        selected_files]
    
    page.add(
        ft.SafeArea(
            ft.Column(
                pageContents,
                expand=False,
                width=SCREEN_WIDTH,
                height=(SCREEN_HEIGHT - APPBAR_HEIGHT),
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )

SCREEN_WIDTH = 366
SCREEN_HEIGHT = 813.6
async def main(page: ft.Page):
    page.title = "XlsxAudit"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window.width = SCREEN_WIDTH
    page.window.height = SCREEN_HEIGHT
    page.window.maximizable = False
    
    page.bgcolor = "#9ad6bb"

    await pseudoSplash(page, 0)
    await home(page)
    
ft.app(main)
