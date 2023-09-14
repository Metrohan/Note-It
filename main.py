# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import string
import sys
import os.path
import os

import NotesUI


class NotesGUI(QtWidgets.QMainWindow, NotesUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("no title")

        self.setupUi(self)
        self.show()
        self.setFixedSize(350, 350)

        self.pushButton.setStyleSheet("background-color : crimson")
        self.pushButton.clicked.connect(self.saveNote)
        self.pushButton.clicked.connect(self.terminateProgram)

        self.createFolder()
        self.createNoteFile()
        self.showNote()


    def createFolder(self):
        note_folder = os.path.expanduser("~\\noteit")
        if not os.path.exists(note_folder):
            os.mkdir(note_folder)

    def createNoteFile(self):
        note_folder = os.path.expanduser("~\\noteit")
        path = os.path.join(note_folder, 'notes.txt')
        global completeName
        completeName = os.path.join(path)

        if not os.path.exists(path):
            with open(completeName, "x", encoding="utf-8") as f:
                f.write("")
        else:
            pass

    def writeNote(self):
        notes = self.textEdit.toPlainText()
        with open(completeName, "w", encoding="utf-8") as f:
            f.write(notes)

    def saveNote(self):
        notes = self.textEdit.toPlainText()
        with open(completeName, "w", encoding="utf-8") as f:
            f.write(notes)

    def showNote(self):
        with open(completeName, "r", encoding="utf-8") as f:
            notes = f.read()
            self.textEdit.setPlainText(notes)

    def terminateProgram(self):
        exit()


def main():
    app = QApplication(sys.argv)
    main_widget = NotesGUI()
    main_widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
