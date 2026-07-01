import tkinter as tk
from tkinter import messagebox
import json
import os

SAVE_FILE = "tasks.json"

COLORS = {
    "bg_root": "#f0f2f5",
    "bg_header": "#1a1a2e",
    "bg_search": "#16213e",
    "bg_list": "#ffffff",
    "bg_footer": "#e8eaf6",
    "accent": "#0f3460",
    "accent_lt": "#e94560",
    "btn_done": "#2ecc71",
    "btn_edit": "#3498db",
    "btn_delete": "#e74c3c",
    "btn_clear": "#95a5a6",
    "done_fg": "#b2bec3",
    "text_main": "#2d3436",
    "text_light": "#636e72",
    "white": "#ffffff",
    "priority_high": "#e74c3c",
    "priority_normal": "#3498db",
    "priority_low": "#95a5a6",
}
PRIORITY_ICONS = {
    "بالا": "بالا",
    "معمولی": "معمولی",
    "کم": "کم",
}
