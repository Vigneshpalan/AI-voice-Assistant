# JARVIS Voice Assistant

JARVIS is a simple voice assistant implemented in Python. It uses speech recognition and natural language processing to understand and respond to voice commands.

## Features

- Speech recognition: JARVIS listens to voice commands and converts them into text using the `speech_recognition` library.
- Natural language processing: The assistant uses intent prediction to understand the user's command and generate appropriate responses.
- Text translation: JARVIS can translate the user's commands into English using the `googletrans` library.
- Text-to-speech: The assistant can respond to the user's commands by converting text into speech using the `speak` library.

## Dependencies

To run the JARVIS Voice Assistant, you need to install the following dependencies:
- `speech_recognition`: This library is used for speech recognition. Install it using `pip install SpeechRecognition`.
- `googletrans`: This library is used for text translation. Install it using `pip install googletrans==4.0.0-rc1`.
- `keyboard`: This library is used to detect key presses. Install it using `pip install keyboard`.

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies using the instructions provided above.
3. Run the' maingui.py` script using the following command:
To run the main GUI code automatically when you open the laptop, you can create a script that launches your application upon system startup. The steps to achieve this depend on your operating system. Below, I'll provide instructions for both Windows and macOS.

Windows:
Create a shortcut to your Python script:

Right-click on your main GUI code file (e.g., main.py) and select "Create Shortcut."
Drag the created shortcut to your desired location (e.g., the Desktop).
Press Win + R to open the "Run" dialog.

Type shell:startup and press Enter. This will open the "Startup" folder.

Move the shortcut you created in step 1 to the "Startup" folder.

Now, every time you start your laptop, the Python script will be executed automatically, and your GUI application will launch.

4.  run the code then you  have to say wake up a activation command .after saying the comand to activate it Press the Voice Assistant  key to give command using voice .
5. Start giving voice commands to JARVIS. It will listen for commands after you press Enter.
6. To exit the voice assistant, simply say "goodbye".
7. you open other application using JARVIS

## Note
 -makes use of a intent recognzing model
- JARVIS uses the English language for command recognition and response. However, you can speak in your preferred language, and JARVIS will translate it to English before processing.
- The accuracy of the speech recognition and natural language processing may vary depending on the environment and the user's pronunciation.
- we are still working on it to improve and add more functionalities





