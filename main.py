# create two classes one for the chatbot window and the other for the chatbot logic
import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                             QLineEdit, QPushButton, QLabel)


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatGPT Main Window")
        self.setMinimumSize(710, 480)

        # add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 540, 320)
        self.chat_area.setReadOnly(True)

        # add input widget
        input_label = QLabel("Message", self)
        input_label.setGeometry(10,340,70,20)
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(70, 340, 480, 40)

        # add persona widget
        persona_label = QLabel("Persona", self)
        persona_label.setGeometry(10, 390, 70, 20)
        self.persona_field = QLineEdit(self)
        self.persona_field.setGeometry(70, 390, 480, 40)

        # add send button
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(560, 360, 100, 40)

        self.show()


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
