import QtQuick
import QtQuick.Controls

Rectangle {
    id: main
    width: 900 / 2
    height: 575 / 2
    color: "white"

    Button {
        text: "Hello World"
        anchors.centerIn: main
    }
}