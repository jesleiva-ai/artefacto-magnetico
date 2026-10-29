# 30 Días con Dios

Ebook devocional para mujeres (cristiano general, voseo argentino). Versículos: Reina-Valera 1960.

- `contenido.py`: todo el texto (30 días, 21 días por los hijos y libros para el plan anual).
- `plantilla.html`: diseño A5 (tipografías y colores).
- `build.py`: genera `ebook.html`.
- `render.js`: convierte `ebook.html` en `30-dias-con-dios.pdf` (Playwright).
- `img/`: fotos opcionales `portada.jpg`, `rincon.jpg`, `hijos.jpg`, `camino.jpg`. Si faltan, se usa un degradado.

Regenerar:

    python3 build.py && node render.js
