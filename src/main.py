from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

def test():
    print("test")

if __name__ == "__main__":
    main()
