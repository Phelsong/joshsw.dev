from pyscript.web import dom
from senza.components import Div, Button
from web.context import site


async def create_dock() -> None:
    dock_container = Div(dom["body"][0], "nav-dock", inner_text="i")
    dock_button = Button(dock_container, "dock-button1", inner_text="about", class_list={"dock-ico"})

    return None
