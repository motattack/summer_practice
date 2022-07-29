import pyscreenshot as ImageGrab
import datetime

path = "engine/bot/screenshots"


def screen():
    im = ImageGrab.grab()
    dt_now = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    im.save(f"{path}/screen{dt_now}.png", "PNG")

    return open(f'{path}/screen{dt_now}.png', 'rb')
