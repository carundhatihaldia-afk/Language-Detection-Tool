# Language-Detection-Tool

## Project Overview
The Language Detection Tool is a Python-based application that identifies the likely language of user-entered text. It uses the `langdetect` library to analyze text and return a language name and language code.

## Features
- Detects multiple languages.
- Accepts sentences and paragraphs through a command-line interface.
- Displays the detected language and its language code.
- Validates empty input and requests longer text for improved accuracy.
- Allows repeated testing without restarting the program.
- Uses a free Python library without requiring an API key.

## Technologies Used
- Python
- langdetect library

## Installation and Setup

1. Install Python 3.
2. Clone or download this repository.
3. Install the required dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python main.py
   ```

## How to Use
1. Start the program.
2. Enter a sentence containing at least three words.
3. View the detected language and its language code.
4. Type `exit` to close the application.

## Example
Input: `Hello, how are you today?`

Expected output:

- Detected Language: English
- Language Code: en

## Limitations
Language identification is statistical and may be inaccurate for short, ambiguous, mixed-language, or misspelled text. Requiring three words improves input quality but does not guarantee correct detection.

## Project Type
College Mini-Project — Python Programming

## Disclaimer
This application estimates the language of the entered text. It does not translate text or guarantee perfect identification.