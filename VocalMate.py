import pyttsx3
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import speech_recognition as sr
import argparse

def speak(text, engine):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def on_speak():
    text = text_entry.get()
    if text.lower() == 'q':
        speak('bye bye friend', engine)
        root.quit()
    else:
        speak(text, engine)

def change_voice():
    voices = engine.getProperty('voices')
    voice_id = simpledialog.askinteger("Select Voice", "Enter voice number (0 or 1):")
    if voice_id is not None and voice_id in [0, 1]:
        engine.setProperty('voice', voices[voice_id].id)

def change_rate():
    rate = simpledialog.askinteger("Set Rate", "Enter speech rate (default is 200):", initialvalue=200)
    if rate:
        engine.setProperty('rate', rate)

def change_volume():
    volume = simpledialog.askfloat("Set Volume", "Enter volume level (0.0 to 1.0):", initialvalue=1.0)
    if volume is not None:
        engine.setProperty('volume', volume)

def save_audio():
    text = text_entry.get()
    if not text:
        messagebox.showerror("Error", "Please enter some text to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")])
    if file_path:
        try:
            engine.save_to_file(text, file_path)
            engine.runAndWait()
            messagebox.showinfo("Success", "Audio saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Speech Recognition", "Please speak into the microphone.")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        text_entry.delete(0, tk.END)
        text_entry.insert(0, text)
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand audio")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Could not request results; {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="VocalMate - A Text-to-Speech Application")
    parser.add_argument('--text', type=str, help="Text to speak")
    args = parser.parse_args()

    engine = pyttsx3.init()
    
    if args.text:
        speak(args.text, engine)
    else:
        # GUI Setup
        root = tk.Tk()
        root.title("VocalMate")
        root.config(bg='#002C3E')  # Set the background color of the window

        # Main frame
        main_frame = tk.Frame(root, bg='#002C3E')
        main_frame.pack(pady=20)

        # Title label
        title_label = tk.Label(main_frame, text="VocalMate", font=("Helvetica", 24, "bold"), fg='white', bg='#002C3E')
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Text entry label
        text_label = tk.Label(main_frame, text="Enter text to speak:", font=("Helvetica", 12), fg='white', bg='#002C3E')
        text_label.grid(row=1, column=0, columnspan=2)

        # Text entry
        text_entry = tk.Entry(main_frame, width=100, font=("Helvetica", 12))
        text_entry.grid(row=2, column=0, columnspan=2, pady=10, padx=20)

        # Define button color variables
        button_bg = '#788CC4'
        button_fg = 'black'
        button_width = 20  # Set a fixed width for all buttons
        button_font = ("Helvetica", 10, "bold")

        # Buttons
        speak_button = tk.Button(main_frame, text="Speak", command=on_speak, bg=button_bg, fg=button_fg, width=button_width, font=button_font)
        speak_button.grid(row=3, column=0, pady=5, padx=10)

        voice_button = tk.Button(main_frame, text="Change Voice", command=change_voice, bg=button_bg, fg=button_fg, width=button_width, font=button_font)
        voice_button.grid(row=3, column=1, pady=5, padx=10)

        rate_button = tk.Button(main_frame, text="Change Rate", command=change_rate, bg=button_bg, fg=button_fg, width=button_width, font=button_font)
        rate_button.grid(row=4, column=0, pady=5, padx=10)

        volume_button = tk.Button(main_frame, text="Change Volume", command=change_volume, bg=button_bg, fg=button_fg, width=button_width, font=button_font)
        volume_button.grid(row=4, column=1, pady=5, padx=10)

        save_button = tk.Button(main_frame, text="Save Audio", command=save_audio, bg=button_bg, fg=button_fg, width=button_width, font=button_font)
        save_button.grid(row=5, column=0, pady=5, padx=10)

        recognize_button = tk.Button(main_frame, text="Recognize Speech", command=recognize_speech, bg=button_bg, fg=button_fg, width=button_width, font=button_font)
        recognize_button.grid(row=5, column=1, pady=5, padx=10)

        quit_button = tk.Button(main_frame, text="Quit", command=root.quit, bg=button_bg, fg=button_fg, width=button_width, font=button_font)
        quit_button.grid(row=6, column=0, columnspan=2, pady=20)

        root.mainloop()