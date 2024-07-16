import flet as ft
import asyncio

async def pseudoSplash(page: ft.Page, sleepTime: 3):
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

async def home(page: ft.Page):
    page.padding = ft.padding.only(0, 0, 0, 0)

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.HOME),
        leading_width=40,
        title=ft.Text("Home"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT
    )
    page.bgcolor = "#ffffff"

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.update()
    filePick_Btn = ft.ElevatedButton("Choose files...",
        on_click=lambda _: pick_files_dialog.pick_files(
            allow_multiple=False,
            allowed_extensions=["xlsx"],
            file_type=ft.FilePickerFileType.CUSTOM
        )
    )

    page.add(
        ft.SafeArea(
            ft.Column(
                [ft.Text("Please load an Excel file to start"),
                filePick_Btn,
                selected_files],
                expand=False,
                width=SCREEN_WIDTH,
                height=SCREEN_HEIGHT,
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
    
    page.padding = ft.padding.only(108, 331.8, 0, 0)
    page.bgcolor = "#9ad6bb"

    page.window.maximizable = False

    await pseudoSplash(page, 0)
    await home(page)
    
ft.app(main)
