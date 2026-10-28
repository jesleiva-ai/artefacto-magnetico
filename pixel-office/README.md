# Oficinita pixel art (Pixel Agents)

Recursos propios para [Pixel Agents](https://github.com/pablodelucca/pixel-agents) (MIT).

```
pixel-office/
  recolor_characters.py     # recolorea pelo y ropa por hex (paleta neón)
  make_furniture.py         # dibuja los muebles originales
  instalar_personajes.ps1   # respalda los de fábrica y copia los neón al caché de npx
  restaurar_personajes.ps1  # vuelve a los de fábrica
  assets/characters/        # char_0..5.png neón (112x96)
  assets/furniture/         # SERVER_RACK, NEON_ARCADE, LAVA_LAMP, NEON_CODE_SIGN
  previews/                 # vistas previas ampliadas
```

## Abrir la oficina

Desde la carpeta de tu proyecto: `npx pixel-agents`. Abrí la URL con `?token=...`
(no la compartas). Para apagarlo: `Ctrl+C` en esa terminal.

## Personajes neón

1. `powershell -ExecutionPolicy Bypass -File .\pixel-office\instalar_personajes.ps1`
   (respaldo en `%USERPROFILE%\pixel-office-backup\`).
2. Reiniciá el servidor.

El parche se pierde si se limpia el caché de npx o se actualiza pixel-agents:
volvé a correr el script. Para deshacer: `restaurar_personajes.ps1`.

Alternativa sin tocar el caché: al cargar esta carpeta con "Add Asset Directory",
Pixel Agents también lee `assets/characters/`, pero los **suma** a los 6 de fábrica
(no los reemplaza).

## Muebles

Settings → "Add Asset Directory" → elegí la carpeta `pixel-office`.
Después "Layout" → paletas Tech / Misc / Decor / Wall → colocá → Save.
Cuidado con Erase: puede borrar pared; usá Undo.

## Regenerar

```
python recolor_characters.py <carpeta con los char_N.png originales>
python make_furniture.py
```
