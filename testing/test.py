import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

def main():
    app = QApplication(sys.argv)

    # QQmlApplicationEngine wird verwendet, um die QML-Datei zu laden
    engine = QQmlApplicationEngine()
    engine.load("Main.qml")

    # Überprüfen, ob das Laden erfolgreich war
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

