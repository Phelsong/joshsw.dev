# %% C1
from functools import lru_cache


class DomRouter:
    def __init__(self):
        self.routes: dict = {}

    def add_route(self, func, url: str) -> None:
        self.routes[url] = func

    def remove_route(self, url: str) -> None:
        self.routes.__delitem__(url)

    def get_routes(self) -> set[str]:
        return self.routes.keys()

    def nav(self, url: str) -> None:
        self.routes[url]()


dom_router = DomRouter()


def route(route):
    @lru_cache(maxsize=2048)
    def wrapper(func):
        dom_router.add_route(func, route)

    return wrapper


@route("/home")
def home():
    print("home")


@route("/home/nest")
def page():
    print("i work")


print(dom_router.get_routes())
dom_router.nav("/home/nest")
dom_router.remove_route("/home")

# -------
# %% C2

import os

tlist: list = []
for x in os.walk("/assets/tech-icons"):
    tlist = x[2]
print(tlist)

# --------
# %% C3
# lib
from pyscript import document

# imports
from senza.components import Div, A


async def repl_page(parent):
    """projects"""
    repl_container = Div(
        parent,
        "repl-page-container",
    )
    try:
        repl_container.innerHTML = "<script async type='py' id='py-term' terminal worker>print('hello')</script>"
    except Exception:
        pass

    return repl_container

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


# ---------------------------
# %% C4
