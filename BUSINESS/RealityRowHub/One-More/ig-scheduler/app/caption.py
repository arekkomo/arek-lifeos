"""Caption generator for One More posts. Tries OpenAI, falls back to template."""
from __future__ import annotations
import logging
from pathlib import Path

logger = logging.getLogger("one-more.caption")

# Brand voice defaults (can be overridden via .env)
BRAND_NAME = "One More"
BRAND_TAGLINE = "Good food • Good people. Somewhere on the Sunshine Coast."

CAPTION_SYSTEM_PROMPT = f"""\
You are the social media writer for **{BRAND_NAME}**, an emerging hospitality/food brand on Instagram.
{BRAND_TAGLINE}

Write captions that are:
- Warm and inviting (no corporate speak)
- 1–3 short sentences max — people scroll fast
- Food-forward but hint at place/people/experience when it fits
- End with ONE line for hashtags (#one more #sunshinecoast + dish-specific tags)
- No emoji overload — 0–2 only if they feel natural

Return ONLY the caption text. No meta, no JSON."""

def fallback_caption(dish_name: str, assets: list[Path]) -> str:
    """Template-based caption when LLM isn't available."""
    dish_display = dish_name.replace("-", " ").title()  # cauliflower-lasagna → Cauliflower Lasagna
    has_video = any(a.suffix.lower() in {".mp4", ".mov", ".webm"} for a in assets)
    video_hint = "" if not has_video else "\n\n📹 Watch it come together."
    return (
        f"{dish_display}. "
        f"Part of the {BRAND_NAME} project.\n"
        f"#onemore #sunshinecoast #{dish_name.replace('-', '')}"
        f"{video_hint}"
    )

async def generate_caption(dish_name: str, assets: list[Path], *, api_key: str | None = None):
    """Generate a caption — tries LLM if key exists, otherwise falls back."""
    asset_list = "\n".join(f"- {a.name} ({a.suffix})" for a in assets)

    if not api_key:
        logger.info("No OpenAI API key — using fallback caption for %s", dish_name)
        return fallback_caption(dish_name, assets)

    try:
        import httpx
        client = httpx.AsyncClient(timeout=15)
        resp = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "temperature": 0.7,
                "messages": [
                    {"role": "system", "content": CAPTION_SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": f"Dish: {dish_name.replace('-', ' ').title()}\nAssets:\n{asset_list}",
                    },
                ],
            },
        )
        resp.raise_for_status()
        data = resp.json()
        caption = data["choices"][0]["message"]["content"].strip()
        await client.aclose()
        logger.info("Generated caption for %s via LLM", dish_name)
        return caption
    except Exception as exc:
        logger.warning("LLM caption failed (%s), falling back", exc)
        await client.aclose()  # type: ignore[possibly-undefined]
        return fallback_caption(dish_name, assets)
