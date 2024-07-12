"""This file contains global site context variables"""
import os
from pyscript import py_import
from pyscript.web import dom

from senza.components.div import Div


class Site:
    body: Div = Div(dom["body"][0], id="root", class_list={"root"})
    base_url:str
    dock: Div


site = Site()

if os.getenv("SITE_ENV") == "PROD":
    site.base_url = ""
else:
    site.base_url = "https://dev.local:8062"
