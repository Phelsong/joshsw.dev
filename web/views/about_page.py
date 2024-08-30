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

    Label(about_container, "skills-label", inner_text="Skills")
    skills_container = Div(about_container, "skills-container")
    # ::::::::-------
    lang_ico_container_root = Div(
        skills_container,
        "lang-ico-container-root",
        class_list={"group-ico-container-root"},
    )
    await tech_ico_group(lang_ico_container_root, "Languages", "lang", lang_logos)
    # ::::::::-------
    lib_ico_container_root = Div(
        skills_container,
        "lib-ico-container-root",
        class_list={"group-ico-container-root"},
    )
    await tech_ico_group(
        lib_ico_container_root, "Libraries & Frameworks", "lib", framework_logos
    )
    # :::::::--------
    tool_ico_container_root = Div(
        skills_container, "tool-ico-container", class_list={"group-ico-container-root"}
    )
    await tech_ico_group(tool_ico_container_root, "Tools & Tech", "tool", tool_logos)
    # :::::::--------

    return about_container


# ----------------------
async def tech_ico_group(container, title: str, identifier: str, source_map: dict):
    Label(container, f"{identifier}-ico-container-title", inner_text=title)
    group_ico_container = Div(
        container, f"{identifier}-ico-container", class_list={"group-ico-container"}
    )
    for id, name in source_map.items():
        img_data: str = await get_data_txt(
            f"{site.base_url}/assets/tech_icons/{name}.svg"
        )
        x_container = Div(
            group_ico_container, f"{id}-container", class_list={"ico-container"}
        )
        SVG(x_container, id, class_list={"tech-ico"}, svg_image=img_data)
        Label(
            x_container, f"{id}-tooltip", class_list={"tech-ico-tooltip"}, inner_text=id
        )
