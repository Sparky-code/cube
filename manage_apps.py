import subprocess
import pprint
# from AppKit import NSScreen, NSWorkspace

p = pprint.PrettyPrinter(indent=4, width=80)


class Applications():

    def open_application(app_name):
        subprocess.run(["open", f"/Applications/{app_name}.app"])

    def get_applications():
        script = '''
        tell application "System Events"
            set apps to name of every application process whose visible is true
        end tell
        '''
        result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
        apps_list = result.stdout.strip().split(", ")
        return apps_list
    
    def search_installed_apps():
        result = subprocess.run(["mdfind", "kMDItemKind == 'Application'"], capture_output=True, text=True)
        apps_list = result.stdout.strip().split("\n")
        apps_list = [app.split("/")[-1].replace(".app", "") for app in apps_list]
        return apps_list
    
    def filter_applications(apps_list, ignore_list):
        filtered_apps_list = [app for app in apps_list if app not in ignore_list]
        apps_dict = {index: app for index, app in enumerate(filtered_apps_list, start=1)}
        print("The following applications were added to this preset:")
        p.pprint(apps_dict)
        return apps_dict
    
    def remove_items_from_list(filtered_list):
        to_remove = input("Type the numbers of any items you want removed from the list, separated by commas, or press Enter to continue: ")
        if to_remove:
            to_remove_indices = [int(x.strip()) for x in to_remove.split(",") if x.strip().isdigit()]
            for index in to_remove_indices:
                filtered_list.pop(index, None)
        return filtered_list

    def move_window(app_name, x, y, width, height):
        script = f'''
        tell application "{app_name}"
            set bounds of front window to {{ {x}, {y}, {x + width}, {y + height} }}
        end tell
        '''
        subprocess.run(["osascript", "-e", script])

# # Example usage
# open_application("Google Chrome")
# move_window("Google Chrome", 100, 100, 800, 600)
Applications.get_applications()