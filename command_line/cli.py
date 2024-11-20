from monitor_manager import Monitor
from screen_manager import Screens

def detailed_info(monitor):
    return (
        f"Display: {monitor['display']}\n"
        f"Resolution: {monitor['resolution']}\n"
        f"Hertz: {monitor['hertz']}\n"
        f"Color Depth: {monitor['color_depth']}\n"
        f"Scaling: {monitor['scaling']}\n"
        f"Origin: {monitor['origin']}\n"
        f"Persistent ID: {monitor['persistent_screen_id']}\n"
        f"Contextual ID: {monitor['contextual_screen_id']}\n"
        f"Serial ID: {monitor['serial_screen_id']}"
    ) 

# Function to handle the 'display' command
def handle_display_command(args):
    monitors = Monitor.load_monitor()

    if args.details:
        # Show detailed information for each monitor
        display_monitors = []
        for preset, monitor_list in monitors.items():
            display_monitors.append(f"Preset: {preset}")
            display_monitors.append("\n".join([f"{detailed_info(monitor)}\n" for monitor in monitor_list]))
        display_monitors = "\n\n".join(display_monitors)
    else:
        # Show summary (default __repr__) for each monitor
        display_monitors = []
        for preset, monitor_list in monitors.items():
            display_monitors.append(f"Preset: {preset}")
            display_monitors.append("\n".join([f"{monitor}" for monitor in monitor_list]))
        display_monitors = "\n\n".join(display_monitors)

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

def handle_apply_command(args):

    if args.key:
        Screens.apply_display_settings()


