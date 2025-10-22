# config.py
# ========================
# Central configuration for Brainrot AI Chatbot
# ========================

import os

# ------------------------
# Colors / Formatting
# ------------------------
BLACK = "\033[30m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

# Brainrot levels: mild → insane
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

# Ensure directories exist
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# ------------------------
# UI / Image Prompts
# ------------------------
UI_ELEMENTS = {
    "deliver_button": "Black and white minimalistic Deliver button, pixel style, clean design",
    "jazz_icon": "Black and white abstract jazz icon, chaotic style",
    "brainrot_logo": "Brainrot AI logo, black and white, glitch art style"
}

# ------------------------
# API Keys
# ------------------------
OPENAI_API_KEY = "YOUR_OPENAI_KEY_HERE"

# ------------------------
# Misc Settings
# ------------------------
FACT_SOURCE = "wikipedia"
MAX_FACT_LENGTH = 300  # Max characters for fact summaries

