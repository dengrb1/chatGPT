from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create QWebEngineView widget
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # Create QAction widget for refresh button
        refresh_action = QAction('Refresh', self)
        refresh_action.triggered.connect(self.browser.reload)
        self.toolbar = self.addToolBar('Refresh')
        self.toolbar.addAction(refresh_action)

        # Load website
        self.browser.setUrl(QUrl('https://link.lbbai.com'))

        # Set window properties
        self.setWindowTitle('LBBai Browser')
        self.setGeometry(0, 0, 800, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = Browser()
    app.exec_()
