import os
import subprocess
from utils.file_utils import create_unique_filename, ensure_output_dir
from utils.config import VIDEO_RESOLUTION

def save_script(code: str, base_name: str) -> str:
    ensure_output_dir()
    path = create_unique_filename(base_name)
    with open(path, "w") as f:
        f.write(code)
    return path

def render_video(script_path: str) -> str:
    name = os.path.splitext(os.path.basename(script_path))[0]
    subprocess.run(["manim", script_path, "-ql"], check=True)
    out_dir = os.path.join("media", "videos", name, VIDEO_RESOLUTION)
    mp4_files = [f for f in os.listdir(out_dir) if f.endswith(".mp4")]
    return os.path.join(out_dir, mp4_files[0]) if mp4_files else None
