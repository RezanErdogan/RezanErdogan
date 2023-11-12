import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout,
                             QWidget, QLabel, QLineEdit, QFrame, QStackedWidget)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class AutomationClipsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Basis UI-Konfiguration
        self.setWindowTitle("Automation Clips")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background-color: #1A1A1A;")  # Anthrazit Hintergrund

        # Hauptlayout
        layout = QHBoxLayout()

        # Seitenmenü
        self.initSideMenu(layout)

        # Hauptinhalt
        self.main_content = QStackedWidget()
        self.initMainContent()
        layout.addWidget(self.main_content)

        # Zentralwidget einstellen
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def initSideMenu(self, layout):
        self.side_menu = QFrame()
        self.side_menu.setFixedWidth(200)
        self.side_menu.setStyleSheet("background-color: #333;")
        side_menu_layout = QVBoxLayout(self.side_menu)

        # Schreibmaschinenschriftart
        font = QFont("Courier", 10, QFont.Bold)

        # Buttons für verschiedene Funktionen
        btn_generate_video = QPushButton("Video generieren")
        btn_generate_video.setFont(font)
        btn_generate_video.setStyleSheet("color: white; background-color: #333; border-radius: 10px;")
        btn_generate_video.clicked.connect(self.generateVideo)

        btn_upload_video = QPushButton("Video hochladen")
        btn_upload_video.setFont(font)
        btn_upload_video.setStyleSheet("color: white; background-color: #333; border-radius: 10px;")
        btn_upload_video.clicked.connect(self.uploadVideo)

        side_menu_layout.addWidget(btn_generate_video)
        side_menu_layout.addWidget(btn_upload_video)

        layout.addWidget(self.side_menu)

    def initMainContent(self):
        # Schreibmaschinenschriftart
        font = QFont("Courier", 10, QFont.Bold)

        # Seite 1: Video generieren
        self.page_generate = QWidget()
        layout_generate = QVBoxLayout(self.page_generate)
        label_generate = QLabel("Video generieren")
        label_generate.setFont(font)
        label_generate.setStyleSheet("color: white;")
        layout_generate.addWidget(label_generate)

        self.input_generate = QLineEdit("Geben Sie Ihren Text ein")
        self.input_generate.setFont(font)
        self.input_generate.setStyleSheet("color: white; background-color: black;")
        layout_generate.addWidget(self.input_generate)

        btn_start_generation = QPushButton("Generieren starten")
        btn_start_generation.setFont(font)
        btn_start_generation.setStyleSheet("color: white; background-color: #333; border-radius: 10px;")
        btn_start_generation.clicked.connect(self.startGeneration)
        layout_generate.addWidget(btn_start_generation)

        # Seite 2: Video hochladen
        self.page_upload = QWidget()
        layout_upload = QVBoxLayout(self.page_upload)
        label_upload = QLabel("Video hochladen")
        label_upload.setFont(font)
        label_upload.setStyleSheet("color: white;")
        layout_upload.addWidget(label_upload)

        self.input_upload = QLineEdit("Pfad zum Video")
        self.input_upload.setFont(font)
        self.input_upload.setStyleSheet("color: white; background-color: black;")
        layout_upload.addWidget(self.input_upload)

        btn_start_upload = QPushButton("Hochladen starten")
        btn_start_upload.setFont(font)
        btn_start_upload.setStyleSheet("color: white; background-color: #333; border-radius: 10px;")
        btn_start_upload.clicked.connect(self.startUpload)
        layout_upload.addWidget(btn_start_upload)

        # Fügen Sie Seiten zum Hauptinhalt hinzu
        self.main_content.addWidget(self.page_generate)
        self.main_content.addWidget(self.page_upload)

    def generateVideo(self):
        self.main_content.setCurrentWidget(self.page_generate)

    def uploadVideo(self):
        self.main_content.setCurrentWidget(self.page_upload)

    def startGeneration(self):
        # Logik zum Generieren eines Videos
        text = self.input_generate.text()
        print(f"Generiere Video mit Text: {text}")

    def startUpload(self):
        # Logik zum Hochladen eines Videos
        video_path = self.input_upload.text()
        print(f"Video hochladen: {video_path}")

def main():
    app = QApplication(sys.argv)
    main_window = AutomationClipsApp()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


