import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('浏览器')
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://chat13.aitianhu.top'))
        self.setCentralWidget(self.browser)
        
        refresh_button = QAction('刷新', self)
        refresh_button.triggered.connect(self.browser.reload)
        self.toolbar = self.addToolBar('Refresh')
        self.toolbar.addAction(refresh_button)

        
# mainloop
app = QApplication(sys.argv)
browser = Browser()
browser.showMaximized()
sys.exit(app.exec_())
