from PIL import Image, ImageDraw
from pystray import Icon, Menu, MenuItem

state = False


def on_clicked(_, item: MenuItem):
    global state
    state = not item.checked


def create_image(width, height, color1, color2):
    image = Image.new("RGB", (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
    dc.rectangle((0, height // 2, width // 2, height), fill=color2)

    return image


def stop(icon: Icon, _):
    icon.stop()


menu = Menu(
    MenuItem("Exit", stop), MenuItem("Checkable", on_clicked, checked=lambda _: state)
)


class App:
    def start(self):
        icon = Icon(
            "menu",
            icon=create_image(64, 64, "black", "white"),
            menu=menu,
        )
        icon.run()

    def stop(self):
        pass


if __name__ == "__main__":
    App().start()
