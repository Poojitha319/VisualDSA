import os
from datetime import datetime
from utils.config import OUTPUT_DIR

def create_unique_filename(base: str, ext: str = "py") -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(OUTPUT_DIR, f"{base}_{timestamp}.{ext}")

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
