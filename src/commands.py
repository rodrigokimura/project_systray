import subprocess
from typing import Callable

from pystray import Icon, MenuItem

MenuItemCallback = Callable[[Icon, MenuItem], None]


def stop(icon: Icon, _):
    icon.stop()


def reboot(*args, **kwargs):
    subprocess.Popen("reboot".split())


def shutdown(*args, **kwargs):
    subprocess.Popen("shutdown now".split())
