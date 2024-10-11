from flask import Flask, request, jsonify, render_template
from Crypto.Cipher import AES
import base64
import os
import threading
import time

app = Flask(__name__)

# Генерация случайного ключа для AES шифрования
SECRET_KEY = os.urandom(16)

# Хранение сообщений и временных имен пользователей
data_store = {}

def pad_message(message):
    # Выравнивание сообщения до блока размера 16 байт
    while len(message) % 16 != 0:
        message += ' '
    return message

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(pad_message(message).encode('utf-8'))
    encrypted_message = base64.b64encode(encrypted_bytes).decode('utf-8')
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded_encrypted_message = base64.b64decode(encrypted_message)
    decrypted_message = cipher.decrypt(decoded_encrypted_message).decode('utf-8').strip()
    return decrypted_message

def delete_user_after_timeout(username, timeout=10800):
    # Удаление пользователя и его сообщения через 3 часа
    time.sleep(timeout)
    data_store.pop(username, None)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')
    username = data.get('username')
    if not message or not username:
        return jsonify({'error': 'No message or username provided'}), 400

    encrypted_message = encrypt_message(message, SECRET_KEY)
    data_store[username] = encrypted_message

    # Создаем поток для удаления сообщения и пользователя через 3 часа
    threading.Thread(target=delete_user_after_timeout, args=(username,)).start()

    return jsonify({'encrypted_message': encrypted_message})

@app.route('/receive', methods=['POST'])
def receive_message():
    data = request.get_json()
    username = data.get('username')
    if not username or username not in data_store:
        return jsonify({'error': 'No message found for this username'}), 400

    encrypted_message = data_store[username]
    decrypted_message = decrypt_message(encrypted_message, SECRET_KEY)
    return jsonify({'decrypted_message': decrypted_message})

if __name__ == '__main__':
    app.run(debug=True)

# Создаем HTML файл "templates/index.html" для интерфейса:
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Chat App</title>
# </head>
# <body>
#     <h1>Secure Chat App</h1>
#     <div>
#         <h3>Send Message</h3>
#         <input id="username" placeholder="Enter your username"><br>
#         <textarea id="message" placeholder="Enter your message"></textarea><br>
#         <button onclick="sendMessage()">Send</button>
#     </div>
#     <div>
#         <h3>Receive Message</h3>
#         <input id="receive_username" placeholder="Enter username to receive message"><br>
#         <button onclick="receiveMessage()">Receive</button>
#     </div>
#     <div id="response"></div>
#     <script>
#         function sendMessage() {
#             const message = document.getElementById('message').value;
#             const username = document.getElementById('username').value;
#             fetch('/send', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ message: message, username: username })
#             })
#             .then(response => response.json())
#             .then(data => {
#                 document.getElementById('response').innerText = 'Encrypted Message: ' + data.encrypted_message;
#             })
#             .catch(error => console.error('Error:', error));
#         }

#         function receiveMessage() {
#             const username = document.getElementById('receive_username').value;
#             fetch('/receive', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ username: username })
#             })
#             .then(response => response.json())
#             .then(data => {
#                 document.getElementById('response').innerText = 'Decrypted Message: ' + data.decrypted_message;
#             })
#             .catch(error => console.error('Error:', error));
#         }
#     </script>
# </body>
# </html>