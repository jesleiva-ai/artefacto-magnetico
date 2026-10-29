// 1) Exporta páginas del ebook en alta resolución para los mockups.
// 2) Captura cada .ad de anuncios.html como PNG listo para subir a Meta.
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const dir = __dirname;
  const browser = await chromium.launch();

  const ebook = await browser.newPage({ viewport: { width: 600, height: 900 }, deviceScaleFactor: 3 });
  await ebook.goto('file://' + path.join(dir, '..', 'ebook.html'), { waitUntil: 'networkidle' });
  await ebook.evaluate(() => document.fonts.ready);
  const pags = await ebook.$$('.pag');
  for (const n of [1, 7, 41, 49, 50]) await pags[n - 1].screenshot({ path: path.join(dir, 'pags', `p${n}.png`) });

  const ads = await browser.newPage({ viewport: { width: 1200, height: 1500 } });
  await ads.goto('file://' + path.join(dir, 'anuncios.html'), { waitUntil: 'networkidle' });
  await ads.evaluate(() => document.fonts.ready);
  const nombres = {
    a1: '1-paz-4x5', a2: '2-mate-4x5', a3: '3-hijos-4x5',
    c1: '4-carrusel-1-portada', c2: '4-carrusel-2-dia', c3: '4-carrusel-3-tarjetas', c4: '4-carrusel-4-hijos', c5: '4-carrusel-5-plan',
  };
  for (const [id, nombre] of Object.entries(nombres)) {
    await (await ads.$('#' + id)).screenshot({ path: path.join(dir, nombre + '.png') });
  }
  await browser.close();
  console.log('listo');
})();
