from monitor_manager import Monitor
from screen_manager import Screens

def detailed_info(self):
    return (
        f"Display: {self.display}\n"
        f"Resolution: {self.resolution}\n"
        f"Hertz: {self.hertz}\n"
        f"Color Depth: {self.color_depth}\n"
        f"Scaling: {self.scaling}\n"
        f"Origin: {self.origin}\n"
        f"Persistent ID: {self.persistent_id}\n"
        f"Contextual ID: {self.contextual_id}\n"
        f"Serial ID: {self.serial_id}"
    )

# Function to handle the 'display' command
def handle_display_command(args):
    monitors = Monitor.load_monitor()

    if args.details:
        # Show detailed information for each monitor
        display_monitors = "\n\n".join([detailed_info(monitor) for monitor in monitors])
    else:
        # Show summary (default __repr__) for each monitor
        display_monitors = "\n".join([f"{monitor}" for monitor in monitors])

    print(f"\n{display_monitors}\n")

def handle_save_command(args):
    monitor_specs = Screens.get_specs()
    monitors = [Monitor.save_monitor(monitor) for monitor in monitor_specs]

    if args.preset:
        Monitor.save_monitors_setup(monitors, args.preset)
        print(f"\nMonitors setup saved as: {args.preset}\n")

    else:
        saved_monitors = "\n".join([f"{monitor.display} saved" for monitor in monitors])
        print(f"\n{saved_monitors}\n")
