import yaml

# Whats the difference between 'Monitor' and 'Screen'?
# Monitor is the data we ingest from the system, what are the specs that the monitors/computer spit out when 

class Monitor():
    def __init__(self, **kwargs):
        self.persistent_id = kwargs.get('persistent_screen_id')
        self.contextual_id = kwargs.get('contextual_screen_id')
        self.serial_id = kwargs.get('serial_screen_id')
        self.display = kwargs.get('display')
        self.resolution = kwargs.get('resolution')
        self.hertz = kwargs.get('hertz')
        self.color_depth = kwargs.get('color_depth')
        self.scaling = kwargs.get('scaling')
        self.origin = kwargs.get('origin')
    
    def __repr__(self):
        return f"<Monitor (display: {self.display}, resolution: {self.resolution})>"
    
    def to_dict(self):
        return {
            'persistent_screen_id': self.persistent_id,
            'contextual_screen_id': self.contextual_id,
            'serial_screen_id': self.serial_id,
            'display': self.display,
            'resolution': self.resolution,
            'hertz': self.hertz,
            'color_depth': self.color_depth,
            'scaling': self.scaling,
            'origin': self.origin
        }

    @staticmethod
    def save_monitor(monitor_dict):
            mapped_kwargs = {
                "persistent_screen_id": monitor_dict.get("Persistent screen id"),
                "contextual_screen_id": monitor_dict.get("Contextual screen id"),
                "serial_screen_id": monitor_dict.get("Serial screen id"),
                "display": monitor_dict.get("Type"),
                "resolution": monitor_dict.get("Resolution"),
                "hertz": monitor_dict.get("Hertz"),
                "color_depth": monitor_dict.get("Color Depth"),
                "scaling": monitor_dict.get("Scaling"),
                "origin": monitor_dict.get("Origin")
            }
            return Monitor(**mapped_kwargs)

    def monitor_constructor(loader, node):
        values = loader.construct_mapping(node)
        return Monitor(**values)

    yaml.add_constructor('tag:yaml.org,2002:python/object:preset_manager.Monitor', monitor_constructor)

    @staticmethod
    def load_monitor():
        try:
            with open('presets.yaml', 'r') as file:
                monitors = yaml.load(file, Loader=yaml.Loader)
                if not isinstance(monitors, dict):
                    monitors = {}
        except FileNotFoundError:
            monitors = {}
        return monitors

    @staticmethod
    def save_monitors_setup(monitors, preset_name):
        try:
            data = Monitor.load_monitor() or {}
        except FileNotFoundError:
            data = {}

        # if preset_name not in data:
        #     data[preset_name] = []

        # Add or update preset with new Monitor details
        data[preset_name] = [monitor.to_dict() for monitor in monitors]
        
        with open('presets.yaml', 'w') as file:
            yaml.dump(data, file)