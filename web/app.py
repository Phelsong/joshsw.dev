#!pyscript
# libs
from asyncio import ensure_future

from pyscript import when

# imports
from sigil_script.dom_router import dom_router
from web.views.about_page import about_page
from web.views.project_page import project_page


# =======================
async def main() -> None:
    # ==================================
    await dom_router.add_route(about_page, "/about")
    await dom_router.nav("/about")
    await dom_router.add_route(project_page, "/projects")

    dom_router.get_routes()

    # ==================================


ensure_future(main())
