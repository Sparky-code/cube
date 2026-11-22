import time
import typer
import json
import pprint
import webbrowser
import subprocess
import difflib
from manage_apps import Applications


app = typer.Typer()
p = pprint.PrettyPrinter(indent=4, width=80)

## App Controls

# Gather Running Applications
@app.command()
def gather():
    print("Gathering running applications", end="")
    apps_list = Applications.get_applications()
    for _ in range(4):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()


    ignore_list = [ "Finder", "System Preferences" ]
    filtered_list = Applications.filter_applications(apps_list, ignore_list)

    approved_list = Applications.remove_items_from_list(filtered_list)

    print("Updated applications list:")
    p.pprint(approved_list)
    return approved_list

# Create Application Preset
@app.command()
def create():
    installed_apps = Applications.search_installed_apps()
    installed_apps_lower = [app.lower() for app in installed_apps]

    user_input = input("Type the names of the required applications, separated by commas: ")
    user_apps = [app.strip() for app in user_input.split(",")]

    valid_apps = {}
    for index, app in enumerate(user_apps, start=1):
        app_lower = app.lower()
        if app_lower in installed_apps_lower:
            valid_apps[index] = installed_apps[installed_apps_lower.index(app_lower)]
        else:
            close_matches = difflib.get_close_matches(app, installed_apps, n=1)
            if close_matches:
                suggestion = close_matches[0]
                response = input(f"Error: '{app}' is not a valid installed application. Did you mean '{suggestion}'? (y/n): ")
                if response.lower() == 'y':
                    valid_apps[index] = suggestion
                else:
                    print(f"'{app}' was not added.")
            else:
                print(f"Error: '{app}' is not a valid installed application.")

    # Reset the keys of the valid_apps dictionary
    valid_apps = {index: app for index, app in enumerate(valid_apps.values(), start=1)}
    
    print("\nValidated applications list:")
    p.pprint(valid_apps)
    return valid_apps


@app.command()
def open_tabs(urls: list[str]):
    for url in urls:
        webbrowser.open(url)

@app.command()
def zen():
    import this
    

# class Applications():

#     def open_application(app_name):
#         subprocess.run(["open", f"/Applications/{app_name}.app"])

#     def move_window(app_name, x, y, width, height):
#         script = f'''
#         tell application "{app_name}"
#             set bounds of front window to {{ {x}, {y}, {x + width}, {y + height} }}
#         end tell
#         '''
#         subprocess.run(["osascript", "-e", script])

# ## Control All Connected Monitors

# # Get Screen(s) Layout 
# @app.command()
# def get():
#     screens = NSScreen.screens()
#     layout = []
#     for screen in screens:
#         frame = screen.frame()
#         layout.append({
#             "x": frame.origin.x,
#             "y": frame.origin.y,
#             "width": frame.size.width,
#             "height": frame.size.height
#         })
#     print(layout)
#     return layout

# # Apply presets > run get first if not existing presets
# @app.command()
# def apply(preset_file: str):
#     with open(preset_file) as f:
#         preset = json.load(f)
    
#     for screen in preset["screens"]:
#         open_application(screen["app"])
#         pos = screen["position"]
#         move_window(screen["app"], pos["x"], pos["y"], pos["width"], pos["height"])


if __name__ == "__main__":
    app()