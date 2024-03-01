from senza.components import Div


async def dp_life_page():
    """about"""
    from web.context import site

    dp_life_container = Div(site.body, inner_text="hello")

    return dp_life_container
