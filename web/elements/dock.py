# libs
from pyscript import window
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
    github_button = DockButton(
        dock_container,
        "github-dock-button",
        icon="""<svg stroke="currentColor" fill="#88c0d0" stroke-width="0" viewBox="0 0 496 512" height="1rem" width="1rem" xmlns="http://www.w3.org/2000/svg"><path d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"></path></svg>
""",
        tooltip_text="Github",
    )

    @when("mousedown", selector="#github-dock-button")
    async def gh_button_listener(event) -> None:
        window.open("https://github.com/Phelsong", "_blank")

    return None
