from sigil_script.components.div import Div


async def project_page(parent):
    """projects"""
    projects_container = Div(parent, inner_text="projects")
    return projects_container
