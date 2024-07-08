from senza.components import Div, Img, SVG, P, Label

from web.context import site
from web.vars.static_assets import svg_logos, png_logos
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
        inner_text="""d
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
    for key,val in svg_logos.items():
        data:str = await get_data_txt(f"{site.base_url}/assets/tech_icons/{val}.svg")
        await tech_ico(about_container, key, data)

    for key,val in png_logos.items():
        data:str = await get_data_txt(f"{site.base_url}/assets/png_icons/{val}.png")
        await tech_ico_img(about_container, key, data)


    return about_container

# ----------------------
async def tech_ico(container, id: str ,svg_data: str):
    Label(container, f"{id}-label", inner_text=id)
    SVG(
        container,
        id,
        svg_image=svg_data
    )

async def tech_ico_img(container, id: str , img_data: str):
    Label(container, f"{id}-label", inner_text=id)
    Img(
        container,
        id,
        src=img_data
    )
