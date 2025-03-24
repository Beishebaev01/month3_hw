import flet as ft
import datetime as dt

def main(page: ft.Page):
    page.title = "First Desktop App"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    greeting_text = ft.Text("Hello, World!")

    greeting_history = []

    history_text = ft.Text("History", style="bodyMedium")

    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            greeting_text.value = f"Hello, {name}!"
            greet_button.text = "Hi again"
            name_input.value = ""
            time = dt.datetime.now().strftime("%H:%M:%S")
            if time > "06:00:00" and time < "12:00:00":
                greeting_text.value = f"Good morning, {name}!"
                greeting_text.color = ft.colors.YELLOW
            elif time > "12:00:00" and time < "18:00:00":
                greeting_text.value = f"Good afternoon, {name}!"
                greeting_text.color = ft.colors.ORANGE
            elif time > "18:00:00" and time < "23:59:59":
                greeting_text.value = f"Good evening, {name}!"
                greeting_text.color = ft.colors.RED
            else:
                greeting_text.value = f"Good night, {name}!"
                greeting_text.color = ft.colors.BLUE
            greeting_history.append(f"{time} - {name}")
            history_text.value = "History: " + "\n".join(greeting_history)
        else:
            greeting_text.text = "Enter your name"

        page.update()


    name_input = ft.TextField(label="Enter your name:", autofocus=True, on_submit=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "History"
        page.update()


    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    
    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Change mode", on_click=toggle_theme)

    greet_button = ft.ElevatedButton("Hi", on_click=on_button_click)

    clear_button = ft.IconButton(icon=ft.icons.DELETE, tooltip="Clear", on_click=clear_history)

    page.add(ft.Row([theme_button], alignment=ft.MainAxisAlignment.END), 
             greeting_text, 
             name_input, 
             greet_button,
             clear_button,
             history_text
             )
    

ft.app(target=main)