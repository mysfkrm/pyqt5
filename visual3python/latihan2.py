import PySimpleGUI as sg
sg.theme("DarkGrey1")
sg.theme_text_color("#E3CF57")

layout = [
    [sg.Text("Mengubah font,teks dan begron",text_color="#7FFFD4",font=("Arial,25"))],
    [sg.Text("NPM      : 2210010339")],
    [sg.Text("Nama     : Muhammad yusuf karimi")],
    [sg.Text("Kelas    : 5O Reguler Banjarmasin")],
    [sg.Text("Matkul   : Pemrograman Visual 3")]
]

window = sg.Window("Latihan Python", layout, size=(400, 200))
window()
window.close()