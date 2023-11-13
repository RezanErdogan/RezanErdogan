import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    ColumnLayout {
        anchors.fill: parent

        Label {
            text: "Video hochladen"
        }

        TextField {
            placeholderText: "Pfad zum Video"
        }

        Button {
            text: "Datei auswählen"
        }

        ProgressBar { }

        Button {
            text: "Hochladen starten"
        }
    }
}
