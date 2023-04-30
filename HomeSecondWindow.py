from PyQt5 import QtWidgets
from functools import partial
from seconde_window import Ui_Seconde_window
from widgets.CustomCheckBox import CustomCheckBox
from q_css import disable_button , app_style


class HomeSecondWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui: Ui_Seconde_window = self.main_window.ui
        self.init_gui()
        self.page_buttons_action()

    def init_gui(self):
        pass


    def page_buttons_action(self):
        pass