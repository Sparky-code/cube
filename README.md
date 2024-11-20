Bash Man Pages
> Man bash

Applescript Man Pages
> man osascript

LoginItems Repo
https://github.com/OJFord/loginitems

DisplayPlacer Repo
https://github.com/jakehilborn/displayplacer

Usage:
python3 main.py save | apply | display 
save --preset 'preset_name'
apply --key 'saved_preset'
display --details


TO DO

# Does applescripts support MD?

# on startup run:

# applescripts to open list of applications - Does this make more sense to use login items + bash to download / ascribe default apps to open on start up?

# Refresh to close all and reopen default setup?

# "Browser (DEFAULT)", "Slack / Teams", VSCode / IntelliJ, Beekeeper Studios, iTerm2

# bash script to organize windows across available screens - prompt expected config, confirm
# bash script to open list of webpages in Browser based on input var (daily, oncall, research, etc)

Process:

Data representing each screen is ingested as a Screen. These screens are parsed and stripped into Monitors.
Each Monitor contains key data about each screen which is then saved into a presets YAML file.

From here each Monitor can be loaded to print its specs (curious what your screen layout looks like technically?).
Each Monitor can be added to a composition (presets for your Home or Office workstation!).
Each Monitor can then be populated with application Windows. These can follow List and Pattern workflows (Choose your apps, choose your pattern) or can be 'handdrawn' with your mouse and then captures with a command.

Workflow

Its more efficient to build screen compositions using your System Settings but [PENDING] you can also define compositions from the command line.

