def wrap_prompt_for_llm(scene_prompt: str) -> str:
    return (
        f"Write a self-contained Manim Scene that visualizes the following concept: {scene_prompt}. "
        "Use standard manim classes like VGroup, Text, Rectangle, Arrow, etc. "
        "No explanation or markdown fences—only code."
    )
