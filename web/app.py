#!pyscript
# libs
from asyncio import ensure_future
from senza.dom_router import dom_router

# imports
from web.elements.dock import create_dock
from web.context import site
from web.views.about_page import about_page
from web.views.project_page import project_page

# from web.views.dp_life_page import dp_life_page


# =======================
async def main() -> None:
    if SITE_ENV == "PRODUCTION":
        site.base_url = "https://www.joshsw.dev"
    else:
        site.base_url = "https://dev.local:8062"

    # ==================================
    await dom_router.add(about_page, "/")
    await dom_router.add(project_page, "projects")
    await dom_router.nav("/")
    await create_dock()


# ==================================


ensure_future(main())
