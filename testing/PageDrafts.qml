import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.15

Item {
    width: parent.width
    height: parent.height

    ScrollView {
        anchors.fill: parent
        GridLayout {
            columns: 3
            rowSpacing: 20
            columnSpacing: 20
            width: parent.width

            Repeater {
                model: 10 // Anzahl der Entwürfe

                Card {
                    id: card
                    width: 300
                    height: 200
                    elevation: 5

                    MouseArea {
                        anchors.fill: parent
                        hoverEnabled: true
                        onEntered: card.elevation = 10
                        onExited: card.elevation = 5
                    }

                    Label {
                        text: "Entwurf " + (index + 1)
                        anchors.centerIn: parent
                        font.bold: true
                        font.pointSize: 16
                    }
                }
            }
        }
    }
}

// Benutzerdefinierte Kartenkomponente
Item {
    property int elevation: 5

    Rectangle {
        id: base
        anchors.fill: parent
        radius: 8
        color: "#ffffff"

        // Schatten für die Karte
        DropShadow {
            anchors.fill: base
            horizontalOffset: 3
            verticalOffset: 3
            radius: 8
            samples: 17
            color: "#80000000"
            source: base
        }
    }
}
