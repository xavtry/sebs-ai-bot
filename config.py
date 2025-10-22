# config.py
# ========================
# Brainrot AI Chatbot - Full Pro Configuration
# ========================

import os
import random

# ------------------------
# Terminal Colors / Formatting
# ------------------------
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"

# ------------------------
# Brainrot Levels
# ------------------------
BRAINROT_LEVELS = {
    "mild": 0.2,
    "medium": 0.5,
    "insane": 0.8
}

# ------------------------
# Paths / Directories
# ------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Create directories if they don't exist
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# ------------------------
# UI / Image Prompts
# ------------------------
UI_ELEMENTS = {
    "deliver_button": "Black and white minimalistic Deliver button, pixel style, clean design",
    "jazz_icon": "Black and white abstract jazz icon, chaotic style",
    "brainrot_logo": "Brainrot AI logo, black and white, glitch art style",
    "loading_spinner": "Black and white minimalistic loading spinner icon"
}

# ------------------------
# API Keys
# ------------------------
OPENAI_API_KEY = "YOUR_OPENAI_KEY_HERE"

# ------------------------
# Fact Settings
# ------------------------
FACT_SOURCE = "wikipedia"
MAX_FACT_LENGTH = 300  # Max characters for fact summaries
FACT_CACHE_FILE = os.path.join(DATA_DIR, "fact_cache.json")

# ------------------------
# Brainrot Phrases & Emojis
# ------------------------
BRAINROT_PHRASES = [
    "oH yEs, lEt's gOoo!!!", "UwU what's this?", "bRaInRoT mOoD aCtIvAtEd",
    "chaotic vibes incoming...", "༼ つ ◕_◕ ༽つ", ">:3", "¯\\_(ツ)_/¯",
    "yOu cAn't sToP tHiS", "mEmEs fOr dAyS", "wHaT iS lIfE??", "brain.exe crashed"
]

BRAINROT_EMOJIS = ["🌀", "💀", "🤯", "🎉", "🧠", "✨", "⚡", "☠️", "🎵", "🎭"]

# ------------------------
# Mini-game settings
# ------------------------
MINI_GAMES = ["tic-tac-toe", "guess-number", "text-puzzle"]
MINI_GAME_ICONS = {
    "tic-tac-toe": "🎲",
    "guess-number": "🔢",
    "text-puzzle": "🧩"
}

# ------------------------
# Random Tips / Loading Messages
# ------------------------
RANDOM_TIPS = [
    "Did you know? Brainrot is a state of chaotic genius!",
    "Tip: Press /jazz for instant vibes.",
    "Fun fact: All AI-generated buttons are fully chaotic.",
    "Remember: Chaos > Order (sometimes).",
    "Keep going! Your brainrot level is rising...",
    "Pro tip: /deliver button = instant power-up."
]

LOADING_MESSAGES = [
    "Generating brainrot vibes...", "Summoning chaos...", 
    "Loading ASCII insanity...", "Thinking in black & white...",
    "Contacting jazz spirits...", "AI neurons overclocking..."
]

# ------------------------
# Utility Functions
# ------------------------
def random_brainrot_phrase():
    return random.choice(BRAINROT_PHRASES) + " " + random.choice(BRAINROT_EMOJIS)

def random_tip():
    return random.choice(RANDOM_TIPS)

def random_loading():
    return random.choice(LOADING_MESSAGES)
