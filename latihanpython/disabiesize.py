from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget

class MyWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.label = QLabel(self)
            self.label.setText("label1")
            self.label.move(200, 0)
            self.button = QPushButton(self)
            self.button.setGeometry(0,0,500,500)
            self.setWindowTitle("Belajar pyQt5")
            cwa =self.frameGeometry() # cek ukuran main window app kita
            cwc = QDesktopWidget().availableGeometry().center() # pada screen saya: (682,363)
            #print(cwc)
            cwa.moveCenter(cwc)
            self.move(cwa.topLeft())
            self.setFixedSize(500,500) # agar tidak bisa di-resizel juga akan otomatis hilang
            
app = QApplication([])
Window = MyWindow()
Window.show()
app.exec_