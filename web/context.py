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

if SITE_ENV == "PRODUCTION":
    site.base_url = "https://www.joshsw.dev"
else:
    site.base_url = "https://dev.local:8062"
