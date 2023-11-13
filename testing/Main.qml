import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 1200
    height: 800
    title: "Automation Clips"

    // Hintergrund und generelles Styling
    color: "#2e3440"
    Material.theme: Material.Dark
    Material.accent: Material.Blue

    RowLayout {
        anchors.fill: parent

        // Seitliches Menü mit verbessertem Styling
        SideMenu {
            id: sideMenu
            Layout.preferredWidth: 300
            onCurrentIndexChanged: contentStack.currentIndex = currentIndex
        }

        // Inhaltsbereich mit fließendem Übergang
        StackLayout {
            id: contentStack
            Layout.fillWidth: true
            Layout.fillHeight: true
            transitions: Transition {
                NumberAnimation { properties: "opacity"; duration: 500 }
            }

            // Hier werden die verschiedenen Seiten eingefügt
            PageGenerate { }
            PageUpload { }
            PageDrafts { }
        }
    }

    // Zusätzliche UI-Elemente oder Funktionen hier einfügen
}
