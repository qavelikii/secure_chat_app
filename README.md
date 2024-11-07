# Secure Chat App

## Overview

This is a simple secure chat application built using Flask for the backend and HTML for the frontend. The application allows users to send and receive encrypted messages using AES encryption. The messages are automatically deleted after 3 hours to enhance security.

## Features

- **Message Encryption**: Messages are encrypted using AES (Advanced Encryption Standard) before being stored.
- **Temporary Usernames**: Users can send and receive messages using temporary usernames.
- **Automatic Deletion**: Messages and associated usernames are deleted automatically after 3 hours.
- **Enhanced Frontend Design**: A basic HTML interface for sending and receiving messages, styled with improved CSS for a better user experience.

## How It Works

1. **Send Message**: Users provide a username and a message. The message is encrypted using AES encryption and stored in memory (`data_store`) associated with the provided username.
2. **Receive Message**: Users provide the username to retrieve the associated message. The message is decrypted before being sent back to the user.
3. **Automatic Deletion**: A background thread is created for each message to delete it after 3 hours.

## Project Structure

- `app.py`: Main application file that contains the Flask server, routes, and logic for encryption and decryption.
- `templates/index.html`: Frontend HTML file that provides the interface for sending and receiving messages.

## Dependencies

- **Flask**: A lightweight web framework for Python.
- **PyCryptodome**: A library used for AES encryption.

To install the dependencies, run:

```bash
pip install flask pycryptodome
```

## Running the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/secure_chat_app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd secure_chat_app
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open a browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the chat interface.

## Usage

- **Send Message**: Enter a username and a message, then click the "Send" button. The encrypted message will be displayed.
- **Receive Message**: Enter the username used to send the message, then click the "Receive" button to see the decrypted message.

## Design Overview

The application includes a simple yet visually appealing HTML-based interface that is easy to use and resembles common web forms for data input. Here's a summary of the visual elements used in the interface:

- **Header**: Displays the application name, "Secure Chat App", centered at the top of the page with a blue background and white text.
- **Input Sections**:
  - **Send Message Section**: A labeled input box for entering the username and a text area for the message, followed by a "Send" button to encrypt and store the message.
  - **Receive Message Section**: A labeled input box for entering the username, followed by a "Receive" button to decrypt and view the message.
- **Response Area**: Displays the results of user actions, such as the encrypted or decrypted message, within a distinct container for clarity.
- **Button Styles**: The buttons are styled to be visually prominent with a blue color, rounded edges, and a hover effect for better user experience.

## Security Notes

- **AES Encryption**: Messages are encrypted using AES with a randomly generated key (`SECRET_KEY`). This key is stored in memory and is not persistent.
- **ECB Mode**: Currently, the encryption uses ECB mode, which is not the most secure mode for sensitive data. Consider using a more secure mode like CBC for better security.

## Limitations

- **In-Memory Storage**: Messages are stored in memory (`data_store`), which means they will be lost if the server is restarted.
- **Basic Security**: The application is for educational purposes and is not intended for production use. More robust security measures are needed for a production environment..

## License

Velikii Dmitrii


