"""base template"""

from pyscript.web import Element
from senza.components.abase import Rest


class H2(Rest):
    """Base component builder for a HTML component.
    _type: str
    _class_list: set
    _parent: pydom.Element
    _js: pydom.Element
    id: str
    html: str
    """

    _type = "h2"
    _class_list: set = {"h2"}
