# libs
from pyscript.web import when, page
from senza.components import Div, Button
from senza.dom_router import dom_router

# imports
from web.context import site
from web.elements.dock_button import DockButton


async def create_dock() -> None:
    dock_container = Div(page.body, "nav-dock")
    about_button = DockButton(
        dock_container,
        "about-dock-button",
        icon="""<svg stroke="currentColor" fill="#88c0d0" stroke-width="0" viewBox="0 0 512 512" height="1rem" width="1rem" xmlns="http://www.w3.org/2000/svg"><path d="M256 21C126.426 21 21 126.426 21 256s105.426 235 235 235 235-105.426 235-235S385.574 21 256 21zm0 36c110.118 0 199 88.882 199 199s-88.882 199-199 199S57 366.118 57 256 145.882 57 256 57zm-7.352 36.744c-8.227 0-15.317 2.976-21.27 8.928-5.776 5.952-8.665 12.955-8.665 21.008 0 8.227 2.89 15.23 8.666 21.006 5.95 5.776 13.04 8.666 21.268 8.666 8.228 0 15.23-2.89 21.006-8.666 5.777-5.777 8.666-12.78 8.666-21.006 0-8.053-2.976-15.056-8.927-21.008-5.777-5.952-12.692-8.928-20.745-8.928zm-62.757 82.453v28.096h46.215v186.13H185.89v27.833h140.22v-27.834h-45.69V176.197h-94.53z"></path></svg>
""",
        tooltip_text="about me",
    )

    @when("mousedown", selector="#about-dock-button")
    async def a_button_listener(event) -> None:
        await dom_router.nav("/")

    # ----------------------
    projects_button = DockButton(
        dock_container,
        "projects-dock-button",
        icon="""<svg stroke="currentColor" fill="#88c0d0" stroke-width="0" version="1.1" viewBox="0 0 32 32" height="3rem" width="3rem" xmlns="http://www.w3.org/2000/svg"><path d="M11.067 10.423l-4.817 5.863 4.817 5.862 1.139-1.874-3.246-3.989 3.246-3.989zM13.175 22.008h2.114l3.361-11.477h-2.115zM20.933 10.423l-1.139 1.874 3.246 3.989-3.246 3.989 1.139 1.874 4.817-5.862z"></path></svg>
""",
        tooltip_text="projects",
    )

    @when("mousedown", selector="#projects-dock-button")
    async def p_button_listener(event) -> None:
        await dom_router.nav("/projects")

    # ----------------------
    repl_button = DockButton(
        dock_container,
        "repl-dock-button",
        icon="""<svg stroke="currentColor" fill="currentColor" stroke-width="0" version="1.1" viewBox="0 0 32 32" height="200px" width="200px" xmlns="http://www.w3.org/2000/svg"><path d="M25.716 6.696h-19.296c-0.888 0-1.608 0.72-1.608 1.608v16.080c0 0.888 0.72 1.608 1.608 1.608h19.296c0.888 0 1.608-0.72 1.608-1.608v-16.080c0-0.888-0.72-1.608-1.608-1.608zM8.028 17.952l3.216-3.216-3.216-3.216 1.608-1.608 4.824 4.824-4.824 4.824-1.608-1.608zM20.892 19.56h-6.432v-1.608h6.432v1.608z"></path></svg>
""",
        tooltip_text="terminal",
    )

    @when("mousedown", selector="#repl-dock-button")
    async def r_button_listener(event) -> None:
        await dom_router.nav("/repl")

    return None
