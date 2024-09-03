from senza.components import Div, A, Label, Img, SVG
from web.elements.link_icon import LinkIcon


# https://github.com/pjjwGraceShopper/GraceShopper
async def project_page(parent):
    """projects"""
    projects_container = Div(parent, "project-page-container")

    # -------------
    senza_container = Div(
        projects_container, "senza-project-container", class_list={"project-container"}
    )
    Label(senza_container, "senza-label", inner_text="senza")
    Img(
        senza_container,
        "senza-img",
        src="assets/imgs/senza_ss.png",
        class_list={"project-img"},
    )
    senza_gh = LinkIcon(
        senza_container,
        "senza-gh-link",
        icon="""<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="200px" width="200px" xmlns="http://www.w3.org/2000/svg"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
        """,
        href="https://github.com/Phelsong/senza",
    )
    # -------------
    micro_cam_container = Div(
        projects_container,
        "microcam-project-container",
        class_list={"project-container"},
    )
    Label(micro_cam_container, "microcam-label", inner_text="micro_cam")
    Img(
        micro_cam_container,
        "microcam-img",
        src="assets/imgs/camstl_sample1.png",
        class_list={"project-img"},
    )
    Img(
        micro_cam_container,
        "microcam-img",
        src="assets/imgs/cam_sample1.png",
        class_list={"project-img"},
    )
    A(
        micro_cam_container,
        "microcam-gh-link",
        href="https://github.com/Phelsong/micro_cam",
        inner_html="""<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="200px" width="200px" xmlns="http://www.w3.org/2000/svg"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
        """,
    )
    # -------------
    bluebox_container = Div(
        projects_container,
        "bluebox-project-container",
        class_list={"project-container"},
    )
    Label(bluebox_container, "bluebox-label", inner_text="bluebox")
    Img(
        bluebox_container,
        "bluebox-img",
        src="assets/imgs/blueboxsplash.jpg",
        class_list={"project-img"},
    )
    A(
        bluebox_container,
        "bluebox-gh-link",
        href="https://github.com/Phelsong/Arcade-Connect-4",
        inner_html="""<span><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="200px" width="200px" xmlns="http://www.w3.org/2000/svg"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg></span>
        """,
    )

    # ------------
    connect4_container = Div(
        projects_container,
        "connect4-project-container",
        class_list={"project-container"},
    )
    Label(connect4_container, "connect4-label", inner_text="Connect4")
    Img(
        connect4_container,
        "connect4-img",
        src="/assets/imgs/connect-four-splash.jpg",
        class_list={"project-img"},
    )
    A(
        connect4_container,
        "connect4-gh-link",
        inner_html="""<span><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="200px" width="200px" xmlns="http://www.w3.org/2000/svg"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg></span>
        """,
        href="https://github.com/Phelsong/Arcade-Connect-4",
    )
    A(
        connect4_container,
        "connect4-link",
        href="https://sharp-varahamihira-32ec8e.netlify.app/",
        inner_text="link",
    )

    # ------------

    return projects_container
