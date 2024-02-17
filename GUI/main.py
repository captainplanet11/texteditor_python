import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.initMenuBar()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Text Editor')
        self.setWindowIcon(QIcon('GUI\icon.jpg'))  

    def initMenuBar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')

        save_action = QAction(QIcon('save.png'), 'Save', self)  # Set icon for action
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.saveFile)
        file_menu.addAction(save_action)

        open_action = QAction(QIcon('open.png'), 'Open', self)  # Set icon for action
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.openFile)
        file_menu.addAction(open_action)

        edit_menu = menubar.addMenu('Edit')

    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)')
        if filename:
            with open(filename, 'w') as f:
                f.write(self.textEdit.toPlainText())

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*)')
        if filename:
            with open(filename, 'r') as f:
                self.textEdit.setPlainText(f.read())


def main():
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
