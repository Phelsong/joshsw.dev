# %%
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

# %%
#
import os

tlist: list = []
for x in os.walk("/assets/tech-icons"):
    tlist = x[2]
print(tlist)
