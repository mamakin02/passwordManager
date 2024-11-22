import sys

from PyQt6.QtWidgets import QApplication
from home_page import HomePage


def main():
    app = QApplication(sys.argv)
    ex = HomePage()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
