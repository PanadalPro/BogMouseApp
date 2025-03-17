import rumps, threading as th
import time
from AppKit import NSApplication
from pynput import keyboard
from pynput.mouse import Controller

app = NSApplication.sharedApplication()

class MouseApp(rumps.App):
    def __init__(self):
        super().__init__("Mouse App", icon='assets/icon.png') # Optional icon (, icon="icon_path")
        self.menu = ["Running"]

        # Hide the App in Finder (don't show it as a running app)
        app.setActivationPolicy_(2)

mouse = Controller()
saved_position = None
last_position = None
hold_start_time = None
hold_threshold = 1  # seconds

def main_loop():
    #region Mouse Position Detection
    def track_mouse():
        global last_position, hold_start_time, saved_position
        while True:
            current_position = mouse.position
            if last_position == current_position:
                if hold_start_time is None:
                    hold_start_time = time.time()
                elif time.time() - hold_start_time >= hold_threshold:
                    if saved_position != current_position:  # Save only new positions
                        saved_position = current_position
                        print(f"Position saved: {saved_position}")
                        hold_start_time = None  # Reset timer
            else:
                last_position = current_position
                hold_start_time = None  # Reset timer if the mouse moves

            time.sleep(0.1)  # Check position every 100ms

    th.Thread(target=track_mouse).start()
    #endregion

    #region Hotkey Detection
    def on_activate():
        global saved_position
        if saved_position:
            mouse.position = saved_position
            print(f"Mouse restored to: {saved_position}")
        else:
            print("No position saved yet.")

    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<cmd>+<shift>+r'),
        # Command key: <cmd>
        # Shift key: <shift>
        # Option (alt) key: <alt>
        # Shift key: <shift>
        # Normal key: eg: a
        on_activate)
    with keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as l:
        l.join()

    #endregion

th.Thread(target=main_loop).start()
MouseApp().run()