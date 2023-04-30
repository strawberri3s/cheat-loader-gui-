from PyQt5 import QtWidgets
from functools import partial
from ui_app import Ui_MainWindow
from widgets.CustomCheckBox import CustomCheckBox


class Login:
    def __init__(self, main_window ):
        self.main_window = main_window
        self.ui: Ui_MainWindow = self.main_window.ui
        self.init_gui()
        self.page_buttons_action()

    def init_gui(self):
        pass


    def page_buttons_action(self):
        self.ui.login_pushButton.clicked.connect(
            partial(self.login)
        )

    def login(self):

        user_name = self.ui.username_lineEdit.text()

        password = self.ui.password_lineEdit.text()

        self.ui.stackedWidget_main.setCurrentIndex(1)