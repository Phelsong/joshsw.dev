from senza.components import Div, Img, SVG, P, Label

from web.context import site
from web.vars.static_assets import lang_logos, tool_logos, framework_logos
from web.queries import get_data_txt


async def about_page(parent):
    """about"""

    about_container = Div(parent, "about_page")

    bio_row = Div(about_container, "bio_row")
    profile_pic = Img(bio_row, "profile-pic", src="assets/imgs/headshot-small.jpg")
    bio = P(
        bio_row,
        "bio",
        inner_text="""
    I spent the first 10 years of my career journey as a Director of
    Photography, part of which included build video/photo encoding pipelines, LUT transforms, custom film emulation, and more. I moved into the Development world in Jan 2022. I love building
    beautiful solutions to complex problems and creating things.

    I'm inspired by automation and imaging, especially virtual cinematography related, but also anything new and interesting. I aspire to build
    projects that are well used and loved.

    I develop on Arch btw... but I've developed/deployed for Windows, Ubuntu, Rhel, etc... I maintain a "personal datacenter" for hosting, testing, and deploying my own services. This including working with: 
        
        - Docker
        - Kubernetes
        - CI/CD 
        - NFS
        - SMB/Samba
        - ZFS
        - Block Storage
        - Private Cloud
        - and more...
        """,
    )

    stack_container = Div(about_container, "stack-container")

    # ---------
    Label(stack_container, "lang-ico-container-title", inner_text="Languages")
    lang_ico_container = Div(
        stack_container, "lang-ico-container", class_list={"group-ico-container"}
    )
    for key, val in lang_logos.items():
        data: str = await get_data_txt(f"{site.base_url}/assets/tech_icons/{val}.svg")
        await tech_ico(lang_ico_container, key, data)
    # ---------
    Label(
        stack_container, "lib-ico-container-title", inner_text="Frameworks & Libraries"
    )
    framework_ico_container = Div(
        stack_container, "framework-ico-container", class_list={"group-ico-container"}
    )
    for key, val in framework_logos.items():
        data: str = await get_data_txt(f"{site.base_url}/assets/tech_icons/{val}.svg")
        await tech_ico(framework_ico_container, key, data)
    # --------
    Label(stack_container, "lang-ico-container-title", inner_text="Tools")
    tool_ico_container = Div(
        stack_container, "tool-ico-container", class_list={"group-ico-container"}
    )
    for key, val in tool_logos.items():
        data: str = await get_data_txt(f"{site.base_url}/assets/tech_icons/{val}.svg")
        await tech_ico(tool_ico_container, key, data)

    # for key,val in png_logos.items():
    #     data:str = await get_data_txt(f"{site.base_url}/assets/png_icons/{val}.png")
    #     await tech_ico_img(logo_container, key, data)

    return about_container


# ----------------------
async def tech_ico(container, id: str, svg_data: str):
    x_container = Div(container, f"{id}-container", class_list={"ico-container"})
    SVG(x_container, id, class_list={"tech-ico"}, svg_image=svg_data)
    Label(x_container, f"{id}-label", class_list={"tech-ico-label"}, inner_text=id)


async def tech_ico_img(container, id: str, img_data: str):
    x_container = Div(container, f"{id}-container", class_list={"ico-container"})
    Img(x_container, id, class_list={"tech-ico"}, src=img_data)
    Label(x_container, f"{id}-label", class_list={"tech-ico-label"}, inner_text=id)
