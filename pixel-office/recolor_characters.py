"""Recolorea pelo y ropa de los personajes de Pixel Agents con una paleta neón.

Uso:
    python recolor_characters.py <carpeta_con_char_0..5.png> [carpeta_salida]

- Los colores se detectan por HEX (no por posición): cada personaje tiene su
  lista de hex de pelo y de ropa. Todo lo demás (piel, contornos, ojos,
  zapatos, accesorios) queda intacto.
- Dentro de cada grupo se respeta el orden de luminosidad original
  (sombras -> luces), así el sombreado del pixel art se conserva.
- Genera previews/characters_x3.png (NEAREST) para revisar antes de copiar.
"""
import sys
from pathlib import Path

from PIL import Image

NEON = {
    "magenta": "#FF2BD6",
    "cian": "#00F0FF",
    "lima": "#B6FF00",
    "naranja": "#FF8A00",
    "violeta": "#8B5CFF",
    "amarillo": "#FFE600",
}

# Por personaje: hex originales de pelo / ropa y el color neón que reciben.
CHARACTERS = {
    0: {
        "hair": ["#32191D", "#6D4726", "#B18649", "#8F6439", "#341F20", "#6F4A2A"],
        "clothes": ["#1164A9", "#114978", "#071C2E", "#0F406A"],
        "hair_to": "cian", "clothes_to": "magenta",
    },
    1: {
        "hair": ["#F1C084", "#E39F5A", "#7E4B29", "#BE7743"],
        "clothes": ["#252525", "#2B2B2B", "#101010"],
        "hair_to": "magenta", "clothes_to": "lima",
    },
    2: {
        "hair": ["#2B2827", "#252120", "#181616", "#221E1E", "#282423", "#1B1A19"],
        "clothes": ["#E1721D", "#F67D20", "#FF8B31", "#E8741B", "#E87218", "#592700",
                    "#741713", "#A91D18", "#8B1A16", "#56110E"],
        "hair_to": "lima", "clothes_to": "violeta",
    },
    3: {
        "hair": ["#FFF1EF", "#E9D7D4", "#B0A6A3", "#DACCC9", "#F0E1DE", "#BFB6B3"],
        "clothes": ["#BDBDBD", "#EEEEEE", "#D4D4D4"],
        "hair_to": "naranja", "clothes_to": "cian",
    },
    4: {
        "hair": ["#69451B", "#57351A", "#2F160F", "#432415", "#442414", "#421B19"],
        "clothes": ["#BDBDBD", "#EEEEEE", "#D4D4D4"],
        "hair_to": "violeta", "clothes_to": "amarillo",
    },
    5: {
        "hair": ["#131313", "#202020", "#282828", "#373737", "#0E0E0E", "#414141", "#303030"],
        "clothes": ["#9F3F31", "#E16451", "#B24737", "#640026"],
        "hair_to": "amarillo", "clothes_to": "naranja",
    },
}


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def luminance(rgb):
    r, g, b = rgb
    return 0.299 * r + 0.587 * g + 0.114 * b


def mix(a, b, t):
    return tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def ramp(base_hex, n):
    """n tonos del más oscuro al más claro alrededor del color neón."""
    base = hex_to_rgb(base_hex)
    dark = mix(base, (20, 10, 30), 0.65)
    light = mix(base, (255, 255, 255), 0.45)
    if n == 1:
        return [base]
    out = []
    for i in range(n):
        t = i / (n - 1)
        out.append(mix(dark, base, t * 2) if t <= 0.5 else mix(base, light, (t - 0.5) * 2))
    return out


def group_map(hexes, neon_name):
    """Ordena los hex del grupo por luminosidad y les asigna la rampa neón."""
    rgbs = sorted({hex_to_rgb(h) for h in hexes}, key=luminance)
    return dict(zip(rgbs, ramp(NEON[neon_name], len(rgbs))))


def recolor(src, dst, spec):
    im = Image.open(src).convert("RGBA")
    mapping = {**group_map(spec["hair"], spec["hair_to"]),
               **group_map(spec["clothes"], spec["clothes_to"])}
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a and (r, g, b) in mapping:
                px[x, y] = (*mapping[(r, g, b)], a)
    im.save(dst)
    return im


def preview(images, out, scale=3):
    gap = 8
    w = sum(i.width for i in images) + gap * (len(images) + 1)
    h = max(i.height for i in images) + gap * 2
    sheet = Image.new("RGBA", (w, h), (40, 40, 52, 255))
    x = gap
    for im in images:
        sheet.paste(im, (x, gap), im)
        x += im.width + gap
    sheet.resize((w * scale, h * scale), Image.NEAREST).save(out)


def main():
    src_dir = Path(sys.argv[1])
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).parent / "assets" / "characters"
    out_dir.mkdir(parents=True, exist_ok=True)
    prev_dir = Path(__file__).parent / "previews"
    prev_dir.mkdir(exist_ok=True)

    originals, results = [], []
    for i, spec in CHARACTERS.items():
        src = src_dir / f"char_{i}.png"
        originals.append(Image.open(src).convert("RGBA"))
        results.append(recolor(src, out_dir / f"char_{i}.png", spec))
    preview(results, prev_dir / "characters_x3.png")
    preview(originals, prev_dir / "characters_original_x3.png")
    print(f"Listo: {out_dir} y vistas previas en {prev_dir}")


if __name__ == "__main__":
    main()
