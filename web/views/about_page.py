from senza.components import Div, Img, SVG, P
from web.queries import get_data_txt


async def about_page(parent):
    """about"""

    about_container = Div(parent, "about_page")
    profile_pic = Img(
        about_container, "profile-pic", src="assets/imgs/headshot-small.jpg"
    )
    bio = P(
        about_container,
        "bio",
        inner_text="""
    I spent of the first 10 years of my career journey as a Directory of
    Photography, but moved into the Development world in 2022. I love building
    beautiful solutions to complex problems and creating things that have never
    been seen before.
    <br />
    I'm inspired by automation or anything new and interesting. I aspire to build
    projects that are well used and loved. Also, eventually working on virtual
    cinematography projects.
        """,
    )
    SVG(
        about_container,
        "beekeeper-svg",
        svg_image=await get_data_txt("assets/icons/BeekeeperLogo.svg"),
    )
    SVG(
        about_container,
        "python-logo",
        svg_image=await get_data_txt("assets/icons/fa-python.svg"),
    )

    return about_container
