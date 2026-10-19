"""Genera la versión publicable (PWA) de Yoga en Silla a partir de index.html.

index.html es la fuente única (también se publica como artefacto). Este script
la envuelve en un documento HTML completo, agrega manifest, service worker e
íconos, y deja todo en dist/ y en yoga-en-silla-app.zip.

Uso: python3 build.py   (los íconos se generan con Playwright/Chromium)
"""
import json
import os
import shutil
import subprocess
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")
ZIP = os.path.join(HERE, "yoga-en-silla-app.zip")
VERSION = "1.0.0"

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Yoga en silla: tu espacio de bienestar. Reto de 21 días con rutinas guiadas.">
<meta name="robots" content="noindex, nofollow">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Yoga en Silla">
<style>
:root { padding-top: env(safe-area-inset-top, 0px); }
body { margin: 0; }
img { max-width: 100%; }
</style>
"""

SW_REGISTER = """
<script>
if ("serviceWorker" in navigator && location.protocol === "https:") {
  window.addEventListener("load", function () { navigator.serviceWorker.register("sw.js").catch(function () {}); });
}
</script>
</body>
</html>
"""

SW = """// Service worker de Yoga en Silla: la app funciona sin conexión después de la primera visita.
const CACHE = "yoga-silla-%s";
const SHELL = ["./", "index.html", "manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png", "icons/apple-touch-icon.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  // Páginas: primero la red (para recibir actualizaciones), si no hay conexión, la copia guardada.
  if (req.mode === "navigate") {
    e.respondWith(fetch(req).then(r => { const c = r.clone(); caches.open(CACHE).then(x => x.put("index.html", c)); return r; })
      .catch(() => caches.match("index.html")));
    return;
  }
  // Resto (íconos, tipografías de Google Fonts): la copia guardada y, si no está, la red.
  if (url.origin === location.origin || /fonts\\.(googleapis|gstatic)\\.com$/.test(url.hostname)) {
    e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(r => {
      if (r.ok || r.type === "opaque") { const c = r.clone(); caches.open(CACHE).then(x => x.put(req, c)); }
      return r;
    })));
  }
});
""" % VERSION

MANIFEST = {
    "name": "Yoga en Silla · Tu espacio de bienestar",
    "short_name": "Yoga en Silla",
    "description": "Reto de 21 días de yoga en silla con rutinas guiadas.",
    "lang": "es",
    "start_url": "./",
    "scope": "./",
    "display": "standalone",
    "orientation": "portrait",
    "background_color": "#F1F4F1",
    "theme_color": "#2E6F62",
    "icons": [
        {"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}

# Ícono: la misma figura de la app sobre fondo eucalipto (colores fijos, sin tokens).
ICON_JS = r"""
const { chromium } = require(process.env.PW);
(async () => {
  const [src, out] = process.argv.slice(2);
  const html = require('fs').readFileSync(src, 'utf8');
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 600, height: 600 } });
  await p.setContent(`<style>
    :root{--skin:#E8BC9E;--hair:#4B3330;--top:#F4EDE4;--legs:#20443C;--chair:#9CCBBE;--chair-dark:#7DB3A4;--line:transparent}
    body{margin:0;background:#2E6F62}
    .i{width:512px;height:512px;display:grid;place-items:center;background:#2E6F62}
  </style>${html}`);
  const sizes = [['icon-512.png',512,330],['icon-192.png',192,124],['apple-touch-icon.png',180,116],['icon-maskable-512.png',512,250]];
  for (const [name, size, fig] of sizes) {
    await p.evaluate(([size, fig]) => {
      document.querySelectorAll('.i').forEach(n => n.remove());
      const d = document.createElement('div'); d.className = 'i';
      d.style.width = d.style.height = size + 'px';
      d.innerHTML = window.__icon(fig); document.body.appendChild(d);
    }, [size, fig]);
    await p.locator('.i').screenshot({ path: out + '/' + name });
  }
  await b.close();
})();
"""


def main():
    src = open(os.path.join(HERE, "index.html"), encoding="utf-8").read()
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(os.path.join(DIST, "icons"))

    # Todo lo que sigue al primer </style> es el contenido visible: va dentro de <body>.
    head_part, body_part = src.split("</style>\n\n", 1)
    page = HEAD + head_part + "</style>\n</head>\n<body>\n" + body_part + SW_REGISTER
    open(os.path.join(DIST, "index.html"), "w", encoding="utf-8").write(page)
    open(os.path.join(DIST, "sw.js"), "w", encoding="utf-8").write(SW)
    open(os.path.join(DIST, "manifest.webmanifest"), "w", encoding="utf-8").write(json.dumps(MANIFEST, ensure_ascii=False, indent=2))
    # Netlify / Cloudflare Pages: el service worker y el manifest nunca deben quedar viejos en caché.
    open(os.path.join(DIST, "_headers"), "w").write(
        "/sw.js\n  Cache-Control: no-cache\n/index.html\n  Cache-Control: no-cache\n/*\n  X-Robots-Tag: noindex\n")

    # Íconos: se reutiliza el dibujo de la figura de index.html.
    scratch = os.environ.get("BUILD_TMP", "/tmp")
    icon_page = os.path.join(scratch, "icon-src.html")
    script = src.split("<script>", 1)[1].split("</script>", 1)[0]
    fig_code = script.split("/* ===================== Movimientos", 1)[0].replace("(function () {\n\"use strict\";", "")
    open(icon_page, "w").write(
        "<script>" + fig_code +
        "window.__icon = s => figureSVG(P({ la: [166, 6], ra: [166, 6], eyes: 0 })).replace('<svg ', `<svg width=\"${s}\" height=\"${s * 235 / 200}\" `);</script>")
    js = os.path.join(scratch, "icons.js")
    open(js, "w").write(ICON_JS)
    pw = subprocess.check_output(["npm", "root", "-g"], text=True).strip() + "/playwright"
    subprocess.check_call(["node", js, icon_page, os.path.join(DIST, "icons")], env=dict(os.environ, PW=pw))

    shutil.copy(os.path.join(HERE, "COMO-PUBLICAR.md"), os.path.join(DIST, "COMO-PUBLICAR.md"))
    if os.path.exists(ZIP):
        os.remove(ZIP)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(DIST):
            for f in files:
                full = os.path.join(root, f)
                z.write(full, os.path.join("yoga-en-silla", os.path.relpath(full, DIST)))
    print("OK", ZIP)


if __name__ == "__main__":
    main()
