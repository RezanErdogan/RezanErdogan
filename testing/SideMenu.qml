import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    ColumnLayout {
        anchors.fill: parent
        spacing: 10

        Button {
            text: "Video generieren"
            onClicked: contentStack.currentIndex = 0
        }

        Button {
            text: "Video hochladen"
            onClicked: contentStack.currentIndex = 1
        }

        Button {
            text: "Entwürfe"
            onClicked: contentStack.currentIndex = 2
        }
    }
}
