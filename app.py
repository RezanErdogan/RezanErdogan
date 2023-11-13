import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout,
                             QWidget, QLabel, QLineEdit, QFrame, QTabWidget, QListWidget, QListWidgetItem,
                             QFileDialog, QProgressBar, QTextEdit, QComboBox)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from qt_material import apply_stylesheet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# Importieren Sie die Funktion aus tiktok_uploader.py
from testing.tiktok_uploader import upload_video_to_tiktok

DRIVER_PATH = "C:\\Users\\RezanErdogan\\Documents\\GitHub\\Automationclips\\chromedriver_win32\\chromedriver.exe"

class AutomationClipsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Automation Clips")
        self.setGeometry(100, 100, 1200, 800)

        layout = QHBoxLayout()

        self.initSideMenu(layout)

        self.main_content = QTabWidget()
        self.initMainContent()
        layout.addWidget(self.main_content)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def initSideMenu(self, layout):
        self.side_menu = QFrame()
        self.side_menu.setFixedWidth(300)
        side_menu_layout = QVBoxLayout(self.side_menu)
        side_menu_layout.setSpacing(10)

        font = QFont("Courier", 10, QFont.Bold)

        btn_generate_video = QPushButton("Video generieren")
        btn_generate_video.setFont(font)
        btn_generate_video.clicked.connect(lambda: self.main_content.setCurrentIndex(0))

        btn_upload_video = QPushButton("Video hochladen")
        btn_upload_video.setFont(font)
        btn_upload_video.clicked.connect(lambda: self.main_content.setCurrentIndex(1))

        btn_drafts = QPushButton("Entwürfe")
        btn_drafts.setFont(font)
        btn_drafts.clicked.connect(lambda: self.main_content.setCurrentIndex(2))

        side_menu_layout.addWidget(btn_generate_video)
        side_menu_layout.addWidget(btn_upload_video)
        side_menu_layout.addWidget(btn_drafts)

        layout.addWidget(self.side_menu)

    def initMainContent(self):
        self.initPageGenerate()
        self.initPageUpload()
        self.initPageDrafts()

    def initPageGenerate(self):
        page_generate = QWidget()
        layout_generate = QVBoxLayout(page_generate)

        label_generate = QLabel("Video generieren")
        label_generate.setFont(QFont("Courier", 10, QFont.Bold))
        layout_generate.addWidget(label_generate)

        self.text_input = QTextEdit("Geben Sie Ihren Text ein")
        self.text_input.setFont(QFont("Courier", 10, QFont.Bold))
        layout_generate.addWidget(self.text_input)

        self.video_settings = QComboBox()
        self.video_settings.addItems(["720p", "1080p", "4K"])
        layout_generate.addWidget(self.video_settings)

        self.generate_progress = QProgressBar()
        layout_generate.addWidget(self.generate_progress)

        btn_start_generation = QPushButton("Generieren starten")
        btn_start_generation.setFont(QFont("Courier", 10, QFont.Bold))
        btn_start_generation.clicked.connect(self.startGeneration)
        layout_generate.addWidget(btn_start_generation)

        self.main_content.addTab(page_generate, "Generieren")

    def startGeneration(self):
        text = self.text_input.toPlainText()
        print(f"Generiere Video mit Text: {text}")

    def initPageUpload(self):
        page_upload = QWidget()
        layout_upload = QVBoxLayout(page_upload)

        label_upload = QLabel("Video hochladen")
        label_upload.setFont(QFont("Courier", 10, QFont.Bold))
        layout_upload.addWidget(label_upload)

        self.input_upload = QLineEdit("Pfad zum Video")
        self.input_upload.setFont(QFont("Courier", 10, QFont.Bold))
        layout_upload.addWidget(self.input_upload)

        btn_select_file = QPushButton("Datei auswählen")
        btn_select_file.setFont(QFont("Courier", 10, QFont.Bold))
        btn_select_file.clicked.connect(self.openFileDialog)
        layout_upload.addWidget(btn_select_file)

        self.upload_progress = QProgressBar()
        layout_upload.addWidget(self.upload_progress)

        btn_start_upload = QPushButton("Hochladen starten")
        btn_start_upload.setFont(QFont("Courier", 10, QFont.Bold))
        btn_start_upload.clicked.connect(self.startUpload)
        layout_upload.addWidget(btn_start_upload)

        self.main_content.addTab(page_upload, "Hochladen")
    def startUpload(self):
        video_path = self.input_upload.text()
        # Verwenden Sie hier Ihre echten TikTok-Anmeldeinformationen
        upload_video_to_tiktok("IhrBenutzername", "IhrPasswort", video_path, DRIVER_PATH)

    def openFileDialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Datei auswählen", "", "Video Files (*.mp4 *.avi *.mov)")
        if file_name:
            self.input_upload.setText(file_name)



    def upload_video_to_tiktok(self, video_path):
        # Hier kommt Ihr Selenium-Code hin. 
        pass

    def initPageDrafts(self):
        page_drafts = QWidget()
        layout_drafts = QVBoxLayout(page_drafts)
        label_drafts = QLabel("Entwürfe")
        label_drafts.setFont(QFont("Courier", 10, QFont.Bold))
        layout_drafts.addWidget(label_drafts)

        self.drafts_list = QListWidget()
        self.drafts_list.setIconSize(QSize(100, 100))
        layout_drafts.addWidget(self.drafts_list)

        for i in range(5):
            item = QListWidgetItem(f"Entwurf {i+1}")
            item.setIcon(QIcon("path/to/preview/image.png"))  # Ersetzen Sie dies durch den korrekten Pfad
            self.drafts_list.addItem(item)

        self.main_content.addTab(page_drafts, "Entwürfe")

# Die main-Funktion und der Rest des Codes sollten auf der obersten Ebene sein (nicht eingerückt unter der Klasse)
def main():
    app = QApplication(sys.argv)
    main_window = AutomationClipsApp()
    apply_stylesheet(app, theme='dark_teal.xml')
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
