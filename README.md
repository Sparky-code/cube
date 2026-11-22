# Usage



## Tasks

### Applications

#### open_application
#### move_window

### Screen Control

#### get_screen_layout
#### apply_preset

### App Control

#### open_tabs

Dependencies

## [Typer](https://github.com/fastapi/typer/blob/master/README.md)

## [PyObjC](https://pyobjc.readthedocs.io/en/latest/core/intro.html#an-introduction-to-pyobjc) > AppKit

## [Subprocess](https://docs.python.org/3/library/subprocess.html)

## [Webbrowser](https://docs.python.org/3/library/webbrowser.html)

# Dev

 - Get Open Apps || Create list of wanted apps (validate against available apps) 
 >> DONE - TO Do: reformat these into clearer classes under manage_apps

 - Get existing screens
 - Prompt organization of existing apps on existing screens (is this laid out how you want it?)
 - Get organization of apps on screens (coordinates in relationship)
 - Attach coordinates to list of apps
 - (Optional) - Offer Presets based on number of apps chosen and available screens

 - Prompt name of layout
 - Prompt any tags
 - (Prompt Author?)
 - Create Layout - save as JSON
 -- Create JSON template
 - Apply Template from JSON
 - Allow trigger on start-up
 - Allow trigger from slack-bot (Eg. OnCall!)

# Testing
 - One Screen, Two apps / split screen
 - One screen, Three apps / split and quartered
 - Two screens, Three apps / full and split (One portait one landscape)