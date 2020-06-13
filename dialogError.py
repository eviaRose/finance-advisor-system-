
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogError(object):
    def setupUi(self, DialogError):
        DialogError.setObjectName("DialogError")
        DialogError.resize(259, 198)
        DialogError.setStyleSheet("")
        self.labelError = QtWidgets.QLabel(DialogError)
        self.labelError.setGeometry(QtCore.QRect(40, 60, 191, 51))
        self.labelError.setStyleSheet("font: 87 12pt \"Arial Black\";")
        self.labelError.setObjectName("labelError")
        self.OKButton = QtWidgets.QPushButton(DialogError)
        self.OKButton.setGeometry(QtCore.QRect(90, 140, 93, 28))
        self.OKButton.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"font: 87 8pt \"Arial Black\";")
        self.OKButton.setObjectName("OKButton")

        self.retranslateUi(DialogError)
        QtCore.QMetaObject.connectSlotsByName(DialogError)
        self.OKButton.clicked.connect(DialogError.close)

    def retranslateUi(self, DialogError):
        _translate = QtCore.QCoreApplication.translate
        DialogError.setWindowTitle(_translate("DialogError", "Dialog"))
        self.labelError.setText(_translate("DialogError", "Symbol not found"))
        self.OKButton.setText(_translate("DialogError", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogError = QtWidgets.QDialog()
    ui = Ui_DialogError()
    ui.setupUi(DialogError)
    DialogError.show()
    sys.exit(app.exec_())
