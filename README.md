# Blind AI - Real-Time Scene Narrator for the Visually Impaired

**Blind AI** is a real-time scene understanding assistant designed to help visually impaired users understand their environment. It uses a fusion of advanced computer vision and language models to provide clear, grounded, and natural scene descriptions.

---

## 🧠 Core Technologies

- **YOLOv11s** — Real-time object detection
- **BLIP** — Image captioning
- **LLaMA-2 7B via Ollama** — Local language model for reasoning and narration
- **pyttsx3** — Offline text-to-speech engine with customizable voices
- **OpenCV** — Video stream processing and display

---

## 🚀 Features

- Describes surroundings using live webcam feed
- Object-aware and spatially grounded narration
- Polite, natural language descriptions tailored for blind users
- Customizable voice (e.g. British English Female)
- Optional BLIP captioning for enriched understanding
- NO hallucinations, emojis, roleplay, or self-references

---

## 📦 Folder Structure

```
blind_ai/
├── main.py                    # Main orchestrator script
├── detectors/
│   └── yolo_detector.py       # YOLOv11 object detection
├── captioning/
│   └── blip_captioner.py      # BLIP caption generation
├── language/
│   └── llama_client.py        # Local LLaMA prompt + response
├── speech/
│   └── speaker.py             # Text-to-speech using pyttsx3
```

---

## 🛠️ Setup Instructions

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

You will need:
- Python 3.11+
- `ultralytics` (for YOLOv11)
- `transformers` (for BLIP)
- `torch`
- `pyttsx3`
- `opencv-python`
- `requests`

> ⚠️ Make sure Ollama is running locally with LLaMA-2 loaded:
```bash
ollama run llama2
```

---

### 2. Run the Assistant

```bash
python main.py
```

Press:
- `[SPACE]` — to capture and describe the current frame
- `[Q]` — to quit

---

## 🧠 How It Works

1. Captures a frame from your webcam
2. Detects objects using YOLOv11s and assigns spatial positions (left, center, right)
3. Optionally generates a caption using BLIP
4. Feeds object list + (optional) caption into LLaMA-2
5. LLaMA responds with a **grounded**, **polite**, and **helpful** narration
6. pyttsx3 converts that text into spoken output

---

## 🗣️ Custom Voice Setup (macOS)

Use a British English female voice (like `Kate`, `Serena`, or `Samantha`):

1. Open **System Settings > Accessibility > Spoken Content > System Voice > Customize**
2. Download the voice you want
3. In `speaker.py`, set:
```python
self.engine.setProperty("voice", "com.apple.voice.enhanced.en-GB.Kate")
```

---

## 🧪 Prompt Behavior (Strict Style)

- No greetings like "Sure, let me describe..."
- No questions at the end
- No roleplay, gestures, or feelings
- First-person or third-person options
- Describes only objects **actually detected**

---

## ✅ Example Output

> "To your left, I see a chair. In front of you, there is a person standing. A bottle is on the right, slightly farther away."

---

## 🔄 Want to Customize It?
- Swap `YOLOv11s` with another YOLO variant (e.g. `yolo11n.pt`)
- Turn off BLIP completely
- Add prompt logging for hallucination auditing

---

## 📩 Contributions & Feedback

This is an open project. Feel free to fork, experiment, and improve!

If you run into issues or want to suggest upgrades, reach out. Let’s build assistive tech that actually helps. 💡


