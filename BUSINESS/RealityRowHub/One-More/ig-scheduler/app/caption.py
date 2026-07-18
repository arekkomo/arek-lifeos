"""One More caption generator — template based (no LLM needed)."""
from pathlib import Path

BRAND_NAME = "One More"
BRAND_TAGLINE = "Good food • Good people. Somewhere on the Sunshine Coast."

CAPTION_TEMPLATES = [
    "{dish}. Part of the {brand} project. #onemore #sunshinecoast #{hashtag}",
    "{dish}. Because sometimes good cooking starts by asking one simple question: what's one more we can try? #{hashtag} #onemore #goodfood",
    "From our {brand} kitchen. {dish}. #{hashtag}",
    "{dish}.{video_hint}\n\n#onemore #eatmore #sunshinecoast #goodfood #vanlife #{hashtag}",
]

def generate_caption(dish_name: str, assets: list[Path]) -> str:
    """Generate a warm brand-aligned caption from templates."""
    dish_display = dish_name.replace("-", " ").title()
    has_video = any(a.suffix.lower() in {".mp4", ".mov", ".webm"} for a in assets)

    # Pick template based on content type
    if has_video:
        return CAPTION_TEMPLATES[3].format(
            dish=dish_display,
            brand=BRAND_NAME,
            hashtag=dish_name.replace("-", ""),
            video_hint="Watch it come together.",
        )
    idx = hash(dish_name) % (len(CAPTION_TEMPLATES) - 1)  # cycle first 3 templates
    return CAPTION_TEMPLATES[idx].format(
        dish=dish_display,
        brand=BRAND_NAME,
        hashtag=dish_name.replace("-", ""),
    )
