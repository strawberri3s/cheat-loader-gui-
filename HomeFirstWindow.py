from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from functools import partial
from ui_app import Ui_MainWindow
from widgets.CustomCheckBox import CustomCheckBox
from q_css import disable_button , app_style
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class HomeFirstWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui: Ui_MainWindow = self.main_window.ui
        self.init_gui()
        self.page_buttons_action()

        self.color : tuple = (55, 144, 202)

    def init_gui(self):
        self.add_widgets_general_group()
        self.add_widgets_save_file_group()
        self.add_widgets_egs_group()

    def add_widgets_general_group(self):
        def glow_effect():
                effect = QGraphicsDropShadowEffect()
                effect.setBlurRadius(5)
                effect.setXOffset(2)
                effect.setYOffset(2)
                effect.setColor(QColor(255, 255, 255, 80))
                return effect
        # add check boxes to general tab
        self.skin_unlocker = CustomCheckBox(
            text="Skin unlocker", active_color="#ff3333"
        )
        self.dlcs_unlocker = CustomCheckBox(
            text="DLCs unlocker", active_color="#ff3333"
        )
        self.devotion_unlocker = CustomCheckBox(text="Devotion", active_color="#ff3333")
        self.queue_info = CustomCheckBox(text="Queue info", active_color="#ff3333")

        self.ui.verticalLayout_4.addWidget(self.skin_unlocker)
        self.ui.verticalLayout_4.addWidget(self.dlcs_unlocker)
        self.ui.verticalLayout_4.addWidget(self.devotion_unlocker)
        self.ui.verticalLayout_4.addWidget(self.queue_info)
        eff1=glow_effect()
        self.skin_unlocker.setGraphicsEffect(eff1)
        eff2=glow_effect()
        self.dlcs_unlocker.setGraphicsEffect(eff2)
        eff3=glow_effect()
        self.devotion_unlocker.setGraphicsEffect(eff3)
        eff4=glow_effect()
        self.queue_info.setGraphicsEffect(eff4)
        self.add_spacing(self.ui.verticalLayout_4)

    def add_widgets_save_file_group(self):
        def glow_effect():
                effect = QGraphicsDropShadowEffect()
                effect.setBlurRadius(5)
                effect.setXOffset(2)
                effect.setYOffset(2)
                effect.setColor(QColor(255, 255, 255, 80))
                return effect
        # add buttons for save file tab
        self.enable_feature = CustomCheckBox(
            text="Enable feature", active_color="#ff3333"
        )

        self.reset_default = QtWidgets.QPushButton(text="Reset to default")
        self.reset_default.setFixedSize(300, 39)
        

        self.inject = QtWidgets.QPushButton(text="Inject")
        self.inject.setFixedSize(300, 39)

        self.dump = QtWidgets.QPushButton(text="Dump")
        self.dump.setFixedSize(300, 39)

        eff1=glow_effect()
        self.enable_feature.setGraphicsEffect(eff1)
        eff2=glow_effect()
        self.reset_default.setGraphicsEffect(eff2)
        eff3=glow_effect()
        self.inject.setGraphicsEffect(eff3)
        eff4=glow_effect()
        self.dump.setGraphicsEffect(eff4)

        self.ui.verticalLayout_7.addWidget(self.enable_feature)
        self.ui.verticalLayout_7.addWidget(self.reset_default)
        self.ui.verticalLayout_7.addWidget(self.inject)
        self.ui.verticalLayout_7.addWidget(self.dump)

        self.add_spacing(self.ui.verticalLayout_7)

    def add_widgets_egs_group(self):
        def glow_effect():
                effect = QGraphicsDropShadowEffect()
                effect.setBlurRadius(5)
                effect.setXOffset(2)
                effect.setYOffset(2)
                effect.setColor(QColor(255, 255, 255, 80))
                return effect
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("Username ...")
        eff1=glow_effect()
        self.line_edit.setGraphicsEffect(eff1)
        self.ui.verticalLayout_6.addWidget(self.line_edit)

        self.add_spacing(self.ui.verticalLayout_6)

    def add_spacing(self, layout):
        spacer = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        layout.addItem(spacer)

    def page_buttons_action(self):

        self.inject.clicked.connect(partial(self.choose_inject_file))
        self.dump.clicked.connect(partial(self.choose_dump_file))
        self.ui.change_them_pushButton.clicked.connect(
            partial(self.color_chooser_dialog)
        )

    def choose_inject_file(self):
        self.inject_fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select File"
        )
        if self.inject_fileName:
            print(self.inject_fileName)

    def choose_dump_file(self):
        self.dump_fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select File"
        )
        if self.dump_fileName:
            print(self.dump_fileName)
    

    def color_chooser_dialog(self):
        color_dialog = QtWidgets.QColorDialog()
        color_hex = color_dialog.getColor()

        if color_hex.isValid():
            color = color_hex.getRgb()
            str_color_main = f"rgba({color[0]} ,{color[1]} , {color[2]} , 1)"
            str_color_80 = f"rgba({color[0]} ,{color[1]} , {color[2]} , 80)"
            str_color_30 = f"rgba({color[0]} ,{color[1]} , {color[2]} , 30)"
            app_style_ = app_style.replace("{{main_color}}", str_color_main)
            app_style_ = app_style_.replace("{{hover_color_80}}", str_color_80)
            app_style_ = app_style_.replace("{{hover_color_30}}", str_color_30)
            self.ui.stackedWidget_main.setStyleSheet(app_style_)

            # update the check boxes

            self.update_check_box_color(color_hex)
            self.color = color


    def update_check_box_color(self , color):
        self.skin_unlocker.set_active_color(str(color.name()))
        self.dlcs_unlocker.set_active_color(str(color.name()))
        self.devotion_unlocker.set_active_color(str(color.name()))
        self.queue_info.set_active_color(str(color.name()))
        self.enable_feature.set_active_color(str(color.name()))