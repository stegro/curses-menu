from cursesmenu import CursesMenu
from cursesmenu.items import SelectionItem


class SelectionMenu(CursesMenu):
    """
    A menu that simplifies item creation, just give it a list of strings and it builds the menu for you
    """

    def __init__(self, strings, title=None, subtitle=None, exit_option=True, parent=None):
        """
        :param strings: The list of strings this menu should be built from
        :type title: str
        :type subtitle: str
        :type strings: list[str]
        :type exit_option: bool
        :type parent: CursesMenu
        """
        super().__init__(title, subtitle, None, exit_option, parent)
        for item in strings:
            self.append_item(SelectionItem(item, self))

    @classmethod
    def get_selection(cls, strings, title="Select an option", subtitle=None, exit_option=True, parent=None):
        """
        Simplifies everything even further. Just give this method a list of strings, and it will show the menu and
        return the selected index

        :type title: str
        :type subtitle: str
        :type strings: list[str]
        :type exit_option: bool
        :type parent: CursesMenu
        :return: the selected index
        :rtype: int
        """
        menu = cls(strings, title, subtitle, exit_option, parent)
        menu.show()
        return menu.selected_option
