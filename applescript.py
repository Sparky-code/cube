# import applescript
import subprocess

def run_applescript():
    # import list of apps from presets, (can bulk tell to open?)
    apps = "Chrome", "VSCodium", "iTerm"
    for app in apps:
        query = subprocess.run(
            # run osascript from subprocess or alt (TO DO)
            ['osascript',
            f'tell application {app} to activate'
            ]
        )

if __name__ == "__main__":
    run_applescript()