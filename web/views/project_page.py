from senza.components import Div, A


async def project_page(parent):
    """projects"""
    projects_container = Div(parent, "project-page-container", inner_text="projects")
    
    senza_container = Div(projects_container, "senza-project-container")
    A(senza_container, "senza-gh-link", inner_text="https://github.com/Phelsong/senza")
    
    micro_cam_container = Div(projects_container, "micro_cam-project-container")
    A(micro_cam_container, "micro_cam-gh-link", inner_text="https://github.com/Phelsong/micro_cam")
    return projects_container
