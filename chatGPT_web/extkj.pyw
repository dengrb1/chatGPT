from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Browser")
        self.setGeometry(100, 100, 800, 600)

        # Create the QWebEngineView widget and set the URL to "https://chat.extkj.cn"
        self.web_view = QWebEngineView(self)
        self.web_view.load(QUrl("https://chat.extkj.cn"))
        self.setCentralWidget(self.web_view)

        # Create the QToolBar widget and add a QAction for the refresh button
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)
        refresh_action = QAction("Refresh", self)
        refresh_action.triggered.connect(self.web_view.reload)
        toolbar.addAction(refresh_action)

if __name__ == "__main__":
    app = QApplication([])
    window = BrowserWindow()
    window.show()
    app.exec_()
