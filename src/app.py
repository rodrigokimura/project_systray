from PIL import Image
from pystray import Icon, Menu, MenuItem

from commands import reboot, shutdown, stop

menu = Menu(
    MenuItem("Reboot", reboot),
    MenuItem("Shutdown", shutdown),
    MenuItem("Exit", stop),
)


class App:
    def start(self):
        icon = Icon(
            "menu",
            icon=Image.open("icon.ico"),
            menu=menu,
        )
        icon.run()

    def stop(self):
        pass


if __name__ == "__main__":
    App().start()
