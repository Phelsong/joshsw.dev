"""This file contains global site context variables"""

import os
from pyscript.web import page, div

from senza.components.div import Div

page.body.append(div(id="root"))


class Site:
    body: Div = page.find("#root")[0]
    base_url: str
    dock: Div


site = Site()

print(site.body.id)
