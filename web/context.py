"""This file contains global site context variables"""

import os
from pyscript import py_import
from pyscript.web import page, div

from senza.components.div import Div

page.body.append(div(id="root"))


class Site:
    body: Div = page.find("#root")[0]
    base_url: str
    dock: Div


site = Site()

print(site.body.id)

if os.getenv("SITE_ENV") == "PROD":
    site.base_url = ""
else:
    site.base_url = "https://dev.local:8062"
