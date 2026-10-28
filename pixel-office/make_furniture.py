"""Dibuja muebles originales para Pixel Agents (Settings -> Add Asset Directory).

Uso:
    python make_furniture.py

Crea assets/furniture/NOMBRE/{manifest.json,NOMBRE.png} junto a este script
y una vista previa ampliada en previews/furniture_x6.png.
"""
import json
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).parent
OUT = ROOT / "assets" / "furniture"

K = (12, 10, 20, 255)          # contorno
CYAN = (0, 240, 255, 255)
MAGENTA = (255, 43, 214, 255)
LIME = (182, 255, 0, 255)
ORANGE = (255, 138, 0, 255)
VIOLET = (139, 92, 255, 255)
YELLOW = (255, 230, 0, 255)
DARK1 = (36, 34, 52, 255)
DARK2 = (54, 50, 76, 255)
DARK3 = (78, 72, 108, 255)
GLASS = (210, 230, 255, 255)


def canvas(w, h):
    return Image.new("RGBA", (w, h), (0, 0, 0, 0))


def box(d, x0, y0, x1, y1, fill, outline=K):
    d.rectangle([x0, y0, x1, y1], fill=fill, outline=outline)


def server_rack():
    im = canvas(16, 32)
    d = ImageDraw.Draw(im)
    box(d, 1, 4, 14, 31, DARK1)
    d.line([2, 5, 13, 5], fill=DARK3)
    lights = [CYAN, LIME, MAGENTA, LIME, ORANGE, CYAN, LIME]
    for i, y in enumerate(range(7, 29, 3)):
        box(d, 2, y, 13, y + 2, DARK2, outline=None)
        d.line([3, y + 1, 8, y + 1], fill=K)           # ranura
        d.point((11, y + 1), fill=lights[i % len(lights)])
        d.point((12, y + 1), fill=lights[(i + 2) % len(lights)])
    d.line([1, 31, 14, 31], fill=K)
    return im


def arcade():
    im = canvas(16, 32)
    d = ImageDraw.Draw(im)
    # gabinete
    d.polygon([(2, 3), (13, 3), (13, 31), (2, 31)], fill=VIOLET, outline=K)
    box(d, 2, 3, 13, 7, MAGENTA)                       # marquesina
    d.line([4, 5, 11, 5], fill=YELLOW)
    box(d, 3, 9, 12, 17, K)                            # pantalla
    box(d, 4, 10, 11, 16, (10, 30, 40, 255), outline=None)
    d.point((6, 12), fill=LIME); d.point((9, 14), fill=MAGENTA)
    d.line([5, 15, 10, 15], fill=CYAN)
    box(d, 2, 18, 13, 21, DARK2)                       # panel de control
    d.point((5, 19), fill=K); d.point((5, 18), fill=ORANGE)   # joystick
    d.point((9, 19), fill=CYAN); d.point((11, 19), fill=MAGENTA)
    box(d, 5, 24, 10, 26, DARK1)                       # ranura de monedas
    d.point((7, 25), fill=YELLOW)
    return im


def lava_lamp():
    im = canvas(16, 32)
    d = ImageDraw.Draw(im)
    d.polygon([(6, 8), (9, 8), (11, 22), (4, 22)], fill=(60, 20, 90, 255), outline=K)
    box(d, 6, 5, 9, 8, DARK3)                          # tapa
    for (x, y, c) in [(7, 10, ORANGE), (8, 11, ORANGE), (6, 14, MAGENTA), (7, 14, MAGENTA),
                      (7, 15, MAGENTA), (8, 18, ORANGE), (9, 18, ORANGE), (6, 20, MAGENTA),
                      (7, 20, MAGENTA), (8, 20, MAGENTA), (9, 20, MAGENTA)]:
        d.point((x, y), fill=c)
    d.polygon([(4, 22), (11, 22), (12, 30), (3, 30)], fill=DARK3, outline=K)
    d.line([4, 26, 11, 26], fill=DARK2)
    return im


def neon_sign():
    im = canvas(32, 32)
    d = ImageDraw.Draw(im)
    box(d, 1, 4, 30, 21, (20, 14, 34, 255))            # placa
    d.rectangle([2, 5, 29, 20], outline=VIOLET)        # marco neón
    glow = (0, 240, 255, 90)
    # "</>"
    for col in (glow, CYAN):
        off = 1 if col is glow else 0
        d.line([10 + off, 8, 6, 12, 10 + off, 16], fill=col)
        d.line([18 + off, 8, 14, 16 + off], fill=col)
        d.line([22, 8, 26 - off, 12, 22, 16], fill=col)
    d.line([15, 17, 16, 17], fill=MAGENTA)
    return im


PIECES = [
    ("SERVER_RACK", "Server Rack", "electronics", server_rack, False, 1),
    ("NEON_ARCADE", "Neon Arcade", "misc", arcade, False, 1),
    ("LAVA_LAMP", "Lava Lamp", "decor", lava_lamp, False, 1),
    ("NEON_CODE_SIGN", "Neon Code Sign", "wall", neon_sign, True, 0),
]


def main():
    previews = []
    for pid, name, cat, fn, on_wall, bg in PIECES:
        im = fn()
        folder = OUT / pid
        folder.mkdir(parents=True, exist_ok=True)
        im.save(folder / f"{pid}.png")
        manifest = {
            "id": pid, "name": name, "category": cat, "type": "asset",
            "file": f"{pid}.png",
            "canPlaceOnWalls": on_wall, "canPlaceOnSurfaces": False,
            "backgroundTiles": bg,
            "width": im.width, "height": im.height,
            "footprintW": im.width // 16, "footprintH": im.height // 16,
        }
        (folder / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
        previews.append(im)

    gap = 6
    w = sum(i.width for i in previews) + gap * (len(previews) + 1)
    sheet = Image.new("RGBA", (w, 32 + gap * 2), (88, 86, 110, 255))
    x = gap
    for im in previews:
        sheet.paste(im, (x, gap), im)
        x += im.width + gap
    (ROOT / "previews").mkdir(exist_ok=True)
    sheet.resize((sheet.width * 6, sheet.height * 6), Image.NEAREST).save(ROOT / "previews" / "furniture_x6.png")
    print("Listo:", OUT)


if __name__ == "__main__":
    main()
