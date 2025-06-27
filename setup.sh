#!/bin/bash

echo "Startar setup..."

# extsra steg för någon system skit
echo "🔧 Installerar systemberoenden..."
brew install ffmpeg

# ror steget ovan int ebehövs 

# Steg 1: Skapa virtuell miljö
echo "Skapar virtuell miljö..."
python3 -m venv .venv

# Steg 2: Aktivera miljön
source .venv/bin/activate

# Steg 3: Installera krav
echo "Installerar requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# Steg 4: Kör huvudprogram
echo " Kör AI-agenten..."
python main.py
