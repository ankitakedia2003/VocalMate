# 🗣️ VocalMate

**VocalMate** is a simple yet powerful desktop application that allows you to **convert text to speech** and **recognize voice input using your microphone**. Built with **Tkinter** for GUI, it uses `pyttsx3` for offline TTS (Text-to-Speech) and `speech_recognition` for STT (Speech-to-Text) capabilities.

🔊 Speak typed text  
🎙️ Recognize speech from mic  
💾 Save speech to audio files  
🎛️ Control voice, rate, and volume

---

## 📌 Features

- ✅ Text-to-Speech (offline, using `pyttsx3`)
- ✅ Speech-to-Text using microphone input (`speech_recognition`)
- ✅ Adjustable:
  - Voice (Male/Female)
  - Speaking rate
  - Volume
- ✅ Save speech output as `.mp3`
- ✅ CLI support for direct speech via `--text`
- ✅ Clean Tkinter GUI with consistent design

---

## 🖼️ About the Project

VocalMate was created to demonstrate how simple it is to build assistive voice-based applications in Python. This project is ideal for beginners who want to explore:
- Python GUIs (Tkinter)
- Text-to-Speech (TTS)
- Speech Recognition (STT)
- File I/O (Saving MP3s)
- Argument parsing (`argparse`)

You can run it as a GUI app or as a quick CLI utility.

---

## 📥 Installation

```markdown
1. **Clone the repository**

   ```bash
   git clone https://github.com/ankitakedia2003/VocalMate.git
   cd VocalMate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Fix PyAudio issues (if needed on Windows)**

   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

4. **Run the application**

   - **GUI Mode**

     ```bash
     python vocalmate.py
     ```

   - **Command Line Mode**

     ```bash
     python vocalmate.py --text "Hello, VocalMate!"
     ```

## 📂 Project Structure
```bash
VocalMate/
├── vocalmate.py           # Main application script
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

## 📦 Dependencies

- pyttsx3 – Offline TTS engine
- speechrecognition – Speech-to-text from microphone
- tkinter – GUI
- pyaudio – Microphone audio input (may require special installation on Windows/Mac)

📌 Note: If you're facing issues with pyaudio, install via wheel:

```bash
pip install pipwin
pipwin install pyaudio
```

## 📬 Contact

Feel free to connect with me:  
🔗 [LinkedIn](https://www.linkedin.com/in/ankita-kedia-787343305)  
📧 kediaankita2003@gmail.com
