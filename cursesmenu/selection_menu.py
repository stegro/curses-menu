from curses_menu import CursesMenu, MenuItem


class SelectionMenu(CursesMenu):
    def __init__(self, title, subtitle=None, items=None, exit_option=True, parent=None):
        if items is None:
            self.items = list()
        else:
            self.items = items
        super().__init__(title, subtitle, items, exit_option, parent)
        for item in items():
            self.add_item(SelectionItem(item, self))

    @classmethod
    def get_selection(cls, options, title="Select an option", subtitle="", exit_option=True, parent=None):
        menu = cls(title, subtitle, options, exit_option, parent)
        menu.show()
        return menu.get_selection()


class SelectionItem(MenuItem):
    def action(self):
        self.menu.exit()