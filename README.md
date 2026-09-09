# Audio & Video Transcription Tool (`to_text`)

A simple, interactive command-line Python application that transcribes both audio and video files into text using OpenAI's [Whisper](https://github.com/openai/whisper) model locally on your machine.

---

## 🌟 Features

- **Multi-Format Support**: Works with audio files (`.mp3`, `.wav`, `.m4a`, `.flac`, `.aac`, etc.) and video files (`.mp4`, `.mkv`, `.mov`, `.avi`, `.webm`, etc.).
- **Interactive CLI**: Prompts for file input directly in the terminal with drag-and-drop file path support.
- **Local Processing**: Transcribes media completely on your machine without relying on external cloud APIs or usage fees.
- **Export to File**: Option to save transcribed text directly as a `.txt` file.

---

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

1. **Python 3.8 or higher**
2. **FFmpeg** (Required by Whisper for processing media files)
   - **macOS** (via Homebrew):
     ```bash
     brew install ffmpeg
     ```
   - **Ubuntu / Debian**:
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   - **Windows** (via Chocolatey):
     ```bash
     choco install ffmpeg
     ```

---

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/charanteja-k/to_text.git
   cd to_text
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

   # On Windows:
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install openai-whisper
   ```

---

## 🎯 Usage

Run the main script:
```bash
python main.py
```

Follow the interactive prompts:
1. Select whether you want to transcribe an audio or video file.
2. Enter or drag-and-drop the file path into the terminal.
3. View the generated transcription on screen.
4. Optionally save the transcription to a `.txt` file.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
