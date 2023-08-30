from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.filemanager import MDFileManager
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Designate our .kv design file
Builder.load_file('file manager.kv')

class MyLayout(Widget):
    pass

class HCPS(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager = self.exit_manager,
            select_path = self.select_path,
        )

    def build(self):
        return MyLayout()

    def file_manager_open(self):
        self.file_manager.show("/")
        self.manager_open = True

    def select_path(self, path):
        # does something to the path
        # opens the loading page
        self.exit_manager()

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

if __name__ == '__main__':
    HCPS().run()