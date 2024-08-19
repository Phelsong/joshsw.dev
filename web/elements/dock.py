# libs
from pyscript import when
from pyscript.web import dom
from senza.components import Div, Button
from senza.dom_router import dom_router

# imports
from web.context import site


async def create_dock() -> None:
    dock_container = Div(dom["body"][0], "nav-dock", inner_text="i")
    about_button = Button(
        dock_container, "about-dock-button", inner_text="about", class_list={"dock-ico"}
    )

    @when("mousedown", selector="#about-dock-button")
    async def a_button_listener(event) -> None:
        await dom_router.nav("/")

    projects_button = Button(
        dock_container,
        "projects-dock-button",
        inner_text="projects",
        class_list={"dock-ico"},
    )

    @when("mousedown", selector="#projects-dock-button")
    async def p_button_listener(event) -> None:
        await dom_router.nav("/projects")

    return None
