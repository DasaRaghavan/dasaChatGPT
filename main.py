# create two classes one for the chatbot window and the other for the chatbot logic
import sys
import threading

from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                             QLineEdit, QPushButton, QLabel)
from backend import Chatbot


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatGPT Main Window")
        self.setMinimumSize(710, 480)
        self.chatbot = Chatbot()

        # add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 540, 320)
        self.chat_area.setReadOnly(True)

        # add input widget
        input_label = QLabel("Message", self)
        input_label.setGeometry(10, 340, 70, 20)
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(70, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # add persona widget
        persona_label = QLabel("Persona", self)
        persona_label.setGeometry(10, 390, 70, 20)
        self.persona_field = QLineEdit(self)
        self.persona_field.setGeometry(70, 390, 480, 40)

        # add send button
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(560, 360, 100, 40)
        self.send_button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        message = self.input_field.text().strip()
        persona = self.persona_field.text().strip()
        self.input_field.clear()
        self.persona_field.clear()
        self.chat_area.setText(f"<p style='color:#333333'>Me: {message}, Respond as: {persona}</p>")
        thread = threading.Thread(target=self.get_bot_response, args=(message, persona))
        thread.start()

    def get_bot_response(self, message, persona):
        response = self.chatbot.get_response(user_input=message, persona=persona)
        self.chat_area.append(f"<p style='color:#333333; background-color:#E9E9E9'>"
                              f"Response:{response}</p>")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
