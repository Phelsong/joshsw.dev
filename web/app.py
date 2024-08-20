#!pyscript
# libs
from asyncio import ensure_future

# imports

from senza.dom_router import dom_router
from web.views.about_page import about_page
from web.context import site

from web.views.project_page import project_page
from web.elements.dock import create_dock
# from web.views.dp_life_page import dp_life_page


# =======================
async def main() -> None:
    # await create_dock()
    # ==================================
    await dom_router.add(about_page, "/")
    await dom_router.add(project_page, "projects")
    await dom_router.nav("/")


# ==================================


ensure_future(main())
