from senza.components import Rest, Element


class LinkIcon(Rest):
    """Base component builder for an HTML button component.
    __Contains__
    id
    class
    inner_text
    """

    _type = "div"
    _class_list: set = {"link-ico"}

    def __init__(
        self,
        parent: Element,
        id: str = "",
        icon: str = "",
        href: str = "",
        *,
        class_list: set = set(),
    ):
        super().__init__(parent, id, class_list=class_list)
        self.innerHTML = f"{icon}"
        self.__setattr__("href", href)