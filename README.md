# 🤖 Jarvis AI Assistant - Bubble

A smooth-functioning AI assistant with an interactive orb visualization. Built with Python, featuring real-time animation feedback and conversational capabilities.

## 🌟 Features

- **Smooth AI Assistant**: Natural language processing with intelligent responses
- **Orb Visualization**: Animated orb with multiple states (Idle, Listening, Processing, Responding, Error)
- **Conversation History**: Track all interactions
- **Interactive Commands**: Help, history, clear, and more
- **Graceful Error Handling**: Robust error management with visual feedback
- **Zero External Dependencies**: Uses only Python standard library

## 📋 Requirements

- Python 3.7+
- No external dependencies required (optional ones listed in `requirements.txt`)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/rajkumarsoni2788-cmd/Jarvis-bubble.git
cd Jarvis-bubble
```

### 2. Run the Main Program
```bash
python main.py
```

### 3. Interact with Jarvis
```
You: hello
Jarvis: Hello! I'm Jarvis. How can I assist you today?

You: what can you do
Jarvis: I'm Jarvis, your AI assistant. I can help with:
- Answering questions
- Processing commands
- Managing tasks
- Providing information
- And much more! What would you like to know?

You: exit
```

## 📁 File Structure

```
Jarvis-bubble/
├── main.py                  # Main entry point (run this!)
├── jarvis_assistant.py      # Core AI assistant logic
├── orb_visualization.py     # Animated orb visualization
├── requirements.txt         # Optional dependencies
└── README.md               # This file
```

## 🎯 Available Commands

| Command | Description |
|---------|-------------|
| `hello`, `hi`, `hey` | Greet Jarvis |
| `help` | See what Jarvis can do |
| `status` | Check Jarvis status |
| `time` | Get current time |
| `history` | View conversation history |
| `clear` | Clear conversation history |
| `exit` | Exit the program |

## 🎨 Orb States

The orb animates to show current state:

- **Idle** (◯): Waiting for input
- **Listening** (◯ expanding): Processing audio/input
- **Processing** (● rotating): Analyzing input
- **Responding** (● pulsing): Generating output
- **Error** (✗): Error state indication

## 🧪 Test Individual Modules

### Test Assistant Only
```bash
python jarvis_assistant.py
```

### Test Orb Visualization
```bash
python orb_visualization.py
```

## 🔧 Extending Jarvis

### Add Custom Responses
Edit the `_generate_response()` method in `jarvis_assistant.py`:

```python
elif "your_keyword" in user_input_lower:
    return "Your custom response here"
```

### Customize Orb Animation
Create new frames in `orb_visualization.py`:

```python
def _get_custom_frame(self, frame: int) -> str:
    frames = [
        "your frame 1",
        "your frame 2",
    ]
    return frames[frame % len(frames)]
```

## 📊 System Architecture

```
JarvisSystem (main.py)
├── JarvisAssistant (jarvis_assistant.py)
│   ├── initialize()
│   ├── process_input()
│   ├── _generate_response()
│   └── conversation_history
└── JarvisOrb (orb_visualization.py)
    ├── animate()
    ├── pulse()
    └── flash_error()
```

## 🎓 Example Usage

```python
from jarvis_assistant import JarvisAssistant
from orb_visualization import JarvisOrb, OrbState

# Create instances
assistant = JarvisAssistant("Jarvis")
orb = JarvisOrb()

# Initialize
assistant.initialize()

# Process input
orb.animate(OrbState.LISTENING)
response = assistant.process_input("Hello")
orb.animate(OrbState.RESPONDING)
print(response)
```

## 🐛 Troubleshooting

### If the orb animation doesn't display properly
- Ensure your terminal supports Unicode characters
- Try running with `PYTHONIOENCODING=utf-8`
- Windows users: Use Windows Terminal or enable UTF-8 support

### If imports fail
- Verify all files are in the same directory
- Python path should include the current directory

## 🚀 Future Enhancements

- [ ] Natural Language Understanding (NLU) with transformers
- [ ] Voice input/output integration
- [ ] Database persistence
- [ ] Web UI dashboard
- [ ] Machine learning responses
- [ ] Multi-language support
- [ ] Plugin system for custom skills

## 📝 License

This project is open source. Feel free to use, modify, and distribute.

## 👨‍💻 Author

Created by [@rajkumarsoni2788-cmd](https://github.com/rajkumarsoni2788-cmd)

## 💬 Support

For issues or suggestions, please open a GitHub issue in the repository.

---

**Made with ❤️ for smooth AI assistants**
