from senza.components import Div, Img, SVG, P

from web.vars.svg_list import svg_list
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
    for item in svg_list:
        data = await get_data_txt(f"assets/icons/{item}.svg")
        await tech_ico(about_container, item, data)
    
    return about_container

# ----------------------
async def tech_ico(container, id:str ,svg_data:str):
    SVG(
        container,
        id,
        svg_image=svg_data
    )

