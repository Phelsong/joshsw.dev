"""This file contains global site context variables"""

from pyweb import pydom
from senza.components import Div


class Site:
    body: Div = Div(pydom["body"][0], id="root", class_list={"root"})


site = Site()
