# import applescript
import subprocess

def open_applications():
    # import list of apps from presets, (can bulk tell to open?)
    apps = "Chrome", "VSCodium", "iTerm"
    for app in apps:
        query = subprocess.run(
            # run osascript from subprocess or alt (TO DO)
            ['osascript',
            f'tell application {app} to activate'
            ]
        )
