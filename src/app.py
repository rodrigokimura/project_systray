from PIL import Image
from pystray import Icon, Menu, MenuItem

from commands import reboot, shutdown, stop
from locker import Locker

menu = Menu(
    MenuItem("Reboot", reboot),
    MenuItem("Shutdown", shutdown),
    MenuItem("Exit", stop),
)


class App:
    def __init__(self) -> None:
        self.locker = Locker("lock")
        self.icon = Icon(
            "menu",
            icon=Image.open("icon.ico"),
            menu=menu,
        )

    def start(self):
        if self.locker.locked:
            return
        self.locker.lock()
        self.icon.run()

    def stop(self):
        pass


if __name__ == "__main__":
    App().start()
