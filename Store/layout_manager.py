import subprocess

def save_layout():
    script = '''
    tell application "System Events"
        set appList to (application processes where background only is false)
        repeat with appProc in appList
            set winList to windows of appProc
            repeat with win in winList
                set winBounds to bounds of win
                -- Save bounds logic here
            end repeat
        end repeat
    end tell
    '''
    subprocess.run(["osascript", "-e", script])

def restore_layout():
    script = '''
    tell application "System Events"
        set bounds of window 1 of process "Safari" to {100, 100, 800, 600}
    end tell
    '''
    subprocess.run(["osascript", "-e", script])