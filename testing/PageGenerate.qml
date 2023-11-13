import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.15

Item {
    width: parent.width
    height: parent.height

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20
        width: parent.width * 0.8

        Label {
            text: "Video generieren"
            font.pointSize: 24
            font.bold: true
        }

        TextArea {
            placeholderText: "Geben Sie Ihren Text ein"
            Layout.fillWidth: true
            height: 100
            font.pointSize: 16
        }

        ComboBox {
            model: ["720p", "1080p", "4K"]
            Layout.fillWidth: true
            font.pointSize: 16
        }

        Rectangle {
            Layout.fillWidth: true
            height: 5
            color: "#0077cc"
            radius: 2.5

            // Animierter Ladebalken
            Rectangle {
                id: progressBar
                width: 0
                height: parent.height
                color: "#00cc77"
                radius: 2.5

                SequentialAnimation on width {
                    loops: Animation.Infinite
                    PropertyAnimation { to: parent.width; duration: 2000 }
                    PropertyAnimation { to: 0; duration: 2000 }
                }
            }
        }

        Button {
            text: "Generieren starten"
            Layout.fillWidth: true
            font.pointSize: 16
        }
    }

    // Zusätzliche Effekte oder Funktionen hier hinzufügen
}

