# utils.py — helpers
import re
from datetime import datetime

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9áéíóúñü\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text

def parse_datetime(date_str, time_str):
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
