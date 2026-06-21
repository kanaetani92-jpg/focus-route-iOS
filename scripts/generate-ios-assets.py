from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
ICON_PATH = ROOT / "ios/App/App/Assets.xcassets/AppIcon.appiconset/AppIcon-512@2x.png"
SPLASH_DIR = ROOT / "ios/App/App/Assets.xcassets/Splash.imageset"


def draw_mark(size: int, background: tuple[int, int, int]) -> Image.Image:
    image = Image.new("RGB", (size, size), background)
    draw = ImageDraw.Draw(image)
    scale = size / 1024

    def box(values):
        return tuple(int(value * scale) for value in values)

    draw.rounded_rectangle(box((0, 0, 1024, 1024)), radius=int(220 * scale), fill="#0f766e")
    draw.ellipse(box((212, 212, 812, 812)), outline="#dff4f1", width=int(96 * scale))
    draw.arc(box((212, 212, 812, 812)), start=270, end=330, fill="#2563eb", width=int(96 * scale))

    stations = ((512, 212), (772, 362), (772, 662), (512, 812), (252, 662), (252, 362))
    radius = int(38 * scale)
    for x, y in stations:
        cx, cy = int(x * scale), int(y * scale)
        draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill="#ffffff")

    width = max(1, int(48 * scale))
    draw.line(box((451, 512, 621, 512)), fill="#ffffff", width=width)
    draw.line(box((559, 450, 621, 512)), fill="#ffffff", width=width)
    draw.line(box((621, 512, 559, 574)), fill="#ffffff", width=width)
    return image


def main() -> None:
    ICON_PATH.parent.mkdir(parents=True, exist_ok=True)
    draw_mark(1024, (15, 118, 110)).save(ICON_PATH)

    splash = Image.new("RGB", (2732, 2732), "#f8faf9")
    mark = draw_mark(768, (15, 118, 110))
    splash.paste(mark, ((2732 - 768) // 2, (2732 - 768) // 2))
    for filename in (
        "splash-2732x2732.png",
        "splash-2732x2732-1.png",
        "splash-2732x2732-2.png",
    ):
        splash.save(SPLASH_DIR / filename)


if __name__ == "__main__":
    main()
