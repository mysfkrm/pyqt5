# ==================== Menggunakan Qmainwindow =======================
from PyQt5. QtWidgets import QApplication, QPushButton,QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()
# Label = QLabel("Label", window) # cara 1
label = QLabel(window)            # cara 2
label.setText("Labeli")
label.move(200, 0)

#button = QPushButton("Label",window) # cara 1
Button = QPushButton(window)          # cara 2
Button.setText("Button1")

window.show()
app.exec_()
