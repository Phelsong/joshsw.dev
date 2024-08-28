from senza.components import Div, A, Label, Img


# https://github.com/pjjwGraceShopper/GraceShopper
async def project_page(parent):
    """projects"""
    projects_container = Div(parent, "project-page-container")

    # -------------
    senza_container = Div(projects_container, "senza-project-container")
    Label(senza_container, "senza-label", inner_text="senza")
    Img(
        senza_container,
        "senza-img",
        src="assets/imgs/senza_ss.png",
        class_list={"project-img"},
    )
    A(senza_container, "senza-gh-link", inner_text="https://github.com/Phelsong/senza")

    # -------------
    micro_cam_container = Div(projects_container, "microcam-project-container")
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
        inner_text="https://github.com/Phelsong/micro_cam",
    )

    # -------------
    bluebox_container = Div(projects_container, "bluebox-project-container")
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
        inner_text="https://github.com/Phelsong/Arcade-Connect-4",
    )

    # ------------
    connect4_container = Div(projects_container, "connect4-project-container")
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
        inner_text="https://github.com/Phelsong/Arcade-Connect-4",
    )
    A(
        connect4_container,
        "connect4-link",
        inner_text="https://sharp-varahamihira-32ec8e.netlify.app/",
    )

    # ------------

    return projects_container
