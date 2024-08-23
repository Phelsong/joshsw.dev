from senza.components import Div, A


async def repl_page(parent):
    """projects"""
    repl_container = Div(
        parent,
        "repl-page-container",
    )
    # repl_container.innerHTML = """
    # <script async type='py' terminal worker>
    # import code
    # code.interact()
    # </script>"""
    # return repl_container
