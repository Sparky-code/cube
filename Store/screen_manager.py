import subprocess
import logging as log
import pprint
import json
import yaml
import re
import os

from monitor_manager import Monitor


# get all windows details using displayplacer
# create k:v pairs for each 
# set organization of windows as a preset

# how do I define the relationship?
# common corners? midpoints? keypoints? maybe take a que from magnets snapping settings
# setup click with args to open 3 applications with set positions
# setup presets for applications by window > open multiple applications within a given window

    # def create_monitor_setup
    # each setup pulls the current screen organization 
    # each screen gets an object
    # each object is tied to the monitor_setup
    # save these in yaml

    # def load_monitor_setup
    # display setups available 
    # select with 1-9 or naming
    # use display placer to apply relationship

    # def create_windows_organization
    # for each window we can have applications that are applied with respect to origin using the persistant and/or contextual ID
    # set max limit of applications per window
    # can any point on the screen be used as the origin? This would create variable anchors per application per screen.

    # def create_windows_presets
    # take current list and organization of windows
    # take list of app presets - can pull from start up apps?
    # can check currently open (from start up)?
    # static lists in presets.yaml for 'work-1, label-n,...'

        


class Screens():
    def __init__():
        self.id = id
        self.context = 'context'
        self.serial = 'serial'
        self.display = 'text'
        # These are the macbook pro standards
        self.resolution = '1440x900' 
        self.hz = 60
        self.colord = 8
        self.scale = on
        self.origin = 0,0

    def get_specs():
        # run displayplacer and capture the settings for all internal and attached monitors/displays
        query = subprocess.run(['displayplacer', 'list'], capture_output=True, text=True, check=True)
        output = query.stdout
        screens = Screens.parse_specs(output)
        return screens
    
    def parse_specs(output):
        # Sort display outputs and organize them as seperate objects
        monitors = []
        lines = output.split('\n')
        nested_items = [l.split(':') for l in lines]
        header = 'Persistent screen id'

        for index, item in enumerate(nested_items):
            if item[0].strip() == header:
                new_dict = {}
                new_dict[item[0].strip()] = item[1].strip()

                # Capture only relevant details and discard the remainder
                for follow_index in range(1, 11):
                    if index + follow_index < len(nested_items):
                        next_item = nested_items[index + follow_index]
                        if len(next_item) == 2:
                            key = next_item[0].strip()
                            value = next_item[1].strip()
                            new_dict[key] = value
            
                monitors.append(new_dict)

        return monitors

    def store_specs():
        specs = Screens.get_specs()
        stored_monitors = []

        # Modify object characteristics as necessary for clarity and uniformity
        for monitor in specs:
            if 'type' in monitor:
                monitor['display'] = monitor.pop('type')
            if 'Origin' in monitor:
                coordinates = re.findall(r'\((.*?)\)', monitor['Origin'])
                monitor['Origin'] = ','.join(coordinates)

            stored_monitors.append(Monitor.save_monitor(monitor))

        # Load existing or stage for new
        try:
            with open('data/presets.yaml', 'r') as file:
                data = yaml.load(file, Loader=yaml.Loader) or {}
        except FileNotFoundError:
            data = {}

        # Add new monitors to the preset (e.g., default preset name 'default')
        preset_name = 'default'  # You can change this to a dynamic value if needed
        if preset_name not in data:
            data[preset_name] = []

        # Append new monitors to the existing preset
        data[preset_name].extend([monitor.to_dict() for monitor in stored_monitors])

        # Save updated presets back to YAML file
        with open('data/presets.yaml', 'w') as file:
            yaml.dump(data, file, sort_keys=True)

        return stored_monitors

    def load_presets(file_path='data/presets.yaml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def generate_displayplacer_command(monitor):
        # Extract fields from monitors dictionary
        persistent_screen_id = monitor['persistent_screen_id']  # Use serial_screen_id instead of persistent_screen_id
        serial_id = monitor['serial_screen_id']
        hertz = monitor['hertz']
        scaling = monitor['scaling']
        color_depth = monitor['color_depth']
        resolution = monitor['resolution']

        origin_str = monitor['origin']
        origin_coords = origin_str.split(' ')[0].strip('()').split(',')
        origin_x = origin_coords[0]
        origin_y = origin_coords[1]

        command = f'id:{persistent_screen_id} res:{resolution} hz:{hertz} color_depth:{color_depth} enabled:true scaling:{scaling} origin:{origin_x},{origin_y} degree:0'
        alt_command = f'serial_id:{serial_id} res:{resolution} hz:{hertz} color_depth:{color_depth} enabled:true scaling:{scaling} origin:{origin_x},{origin_y} degree:0'

        return command, alt_command

    def apply_display_settings(preset_name='default', file_path='data/presets.yaml'):
        
        commands = []
        presets = Screens.load_presets(file_path)

        if preset_name not in presets:
            print(f"Preset '{preset_name}' not found.")
            return

        for monitor in presets[preset_name]:
            # Verify if persistant id will work? if not use serial id
            command = Screens.generate_displayplacer_command(monitor)
            commands.append(command)

        quoted_commands = [f'"{command}"' for command in commands]
        full_command = ' '.join(quoted_commands)
        full_command = f'displayplacer {full_command}'
        print(f"Executing:\n{full_command}")

        try:
            result = subprocess.run(full_command, shell=True, check=True, capture_output=True, text=True)
            print(f'Command executed successfully:\n{result.stdout}')
        except subprocess.CalledProcessError as e:
            print(f'Error occured cwhile executing command:\n{e.stderr}')        