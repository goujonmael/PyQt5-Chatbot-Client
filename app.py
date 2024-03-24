from PyQt5 import QtWidgets, QtCore, QtGui
import requests
import jsonlines
import sys


class CurlApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chat')
        
        self.messageHistory = QtWidgets.QTextEdit(self)  # Ajout d'un QTextEdit pour l'historique des messages
        self.messageHistory.setReadOnly(True)  # Rendre l'historique des messages en lecture seule

        self.messageInput = QtWidgets.QLineEdit(self)  # Ajout d'un QLineEdit pour la saisie des messages
        self.messageInput.returnPressed.connect(self.send_request)  # Envoi du message lorsque l'utilisateur appuie sur Entrée

        self.sendButton = QtWidgets.QPushButton('Send', self)  # Ajout d'un bouton "Envoyer"
        self.sendButton.clicked.connect(self.send_request)  # Envoi du message lorsque l'utilisateur clique sur le bouton "Envoyer"

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.messageHistory)  # Ajout de l'historique des messages au layout
        layout.addWidget(self.messageInput)  # Ajout de la saisie des messages au layout
        layout.addWidget(self.sendButton)  # Ajout du bouton "Envoyer" au layout
        self.setLayout(layout)

    def send_request(self):
        url = "http://192.168.1.195:11434/api/generate"
        data = {
            "model": "dolphin-mistral",
            "prompt": self.messageInput.text()  # Utilisation du texte du QLineEdit comme prompt
        }
        self.messageHistory.append('You: ' + self.messageInput.text() + '\n')  # Ajout du message de l'utilisateur à l'historique des messages
        response = requests.post(url, json=data, stream=True)
        if response.encoding is None:
            response.encoding = 'utf-8'
        server_response = ''  # Création d'une variable pour stocker la réponse du serveur
        self.messageHistory.append('AI: ')
        for item in jsonlines.Reader(response.iter_lines(decode_unicode=True)):
            server_response += item['response']  # Ajout de la partie de la réponse à la variable
            self.messageHistory.moveCursor(QtGui.QTextCursor.End)  # Déplacement du curseur à la fin du texte
            self.messageHistory.insertPlainText(item['response'])  # Ajout de la partie de la réponse à l'historique des messages
            QtCore.QCoreApplication.processEvents()  # Traitement des événements en attente
            if 'done' in item and item['done'] == True:
                self.messageInput.clear()  # Effacement du texte du QLineEdit
                self.messageHistory.append('\n')  # Ajout d'une ligne vide après chaque message de l'IA
                break

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CurlApp()
    window.show()
    sys.exit(app.exec_())