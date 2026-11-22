import typer
import json
import webbrowser

class Screen_Control():

    app = typer.Typer()

    @app.command()
    def apply_preset(preset_file: str):
        with open(preset_file) as f:
            preset = json.load(f)
        
        for screen in preset["screens"]:
            open_application(screen["app"])
            pos = screen["position"]
            move_window(screen["app"], pos["x"], pos["y"], pos["width"], pos["height"])

class App_Control():

    def open_tabs(urls):
        for url in urls:
            webbrowser.open(url)

# Example usage
# open_tabs(["https://www.google.com", "https://github.com"])