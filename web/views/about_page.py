from sigil_script.components.div import Div


async def about_page(parent):
    """about"""

    about_container = Div(parent, inner_text="hello")
    return about_container
