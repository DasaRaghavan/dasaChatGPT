# create two classes one for the chatbot window and the other for the chatbot logic
import sys

from PyQt6.QtWidgets import (QApplication,QMainWindow,QTextEdit,
                             QLineEdit, QPushButton)


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatGPT Main Window")
        self.setMinimumSize(610, 420)

        # add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)


        # add input widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # add send button
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(500, 340, 100, 40)

        self.show()


class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
