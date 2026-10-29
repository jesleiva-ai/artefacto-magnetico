// Convierte ebook.html en el PDF final y saca capturas de control de algunas páginas.
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const dir = __dirname;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 560, height: 794 } });
  await page.goto('file://' + path.join(dir, 'ebook.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: path.join(dir, '30-dias-con-dios.pdf'), width: '148mm', height: '210mm', printBackground: true, preferCSSPageSize: true });

  // Capturas de control: páginas con desborde de contenido.
  const desbordes = await page.$$eval('.pag', (ps) => ps.map((p, i) => (p.scrollHeight > p.clientHeight + 1 ? i + 1 : null)).filter(Boolean));
  console.log('Páginas con desborde:', desbordes.length ? desbordes.join(', ') : 'ninguna');
  const muestra = process.argv.slice(2).map(Number);
  const pags = await page.$$('.pag');
  for (const n of muestra) await pags[n - 1].screenshot({ path: path.join(dir, `control-${n}.png`) });
  await browser.close();
})();
