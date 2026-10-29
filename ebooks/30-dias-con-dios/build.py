"""Genera ebook.html a partir de contenido.py. Luego render.js lo convierte a PDF."""
import html
import re
import os

from contenido import DIAS, HIJOS, LIBROS, MARCA, SEMANAS, SUBTITULO, TITULO

AQUI = os.path.dirname(os.path.abspath(__file__))


def e(t):
    t = re.sub(r'"([^"]+)"', "\u201c\\1\u201d", t)
    return html.escape(t, quote=False)


def parrafos(t):
    return "".join(f"<p>{e(p)}</p>" for p in t.split("\n\n"))


def img(nombre, clase):
    ruta = os.path.join(AQUI, "img", nombre + ".jpg")
    if os.path.exists(ruta):
        return f'<div class="{clase}" style="background-image:url(img/{nombre}.jpg)"></div>'
    return f'<div class="{clase} sin-foto"></div>'


def plan_semanal(semanas=52):
    caps = [(libro, c) for libro, n in LIBROS for c in range(1, n + 1)]
    total = len(caps)
    filas, inicio = [], 0
    for s in range(semanas):
        fin = round(total * (s + 1) / semanas)
        tramo = caps[inicio:fin]
        inicio = fin
        partes, i = [], 0
        while i < len(tramo):
            libro, a = tramo[i]
            j = i
            while j + 1 < len(tramo) and tramo[j + 1][0] == libro:
                j += 1
            b = tramo[j][1]
            partes.append(f"{libro} {a}" if a == b else f"{libro} {a}–{b}")
            i = j + 1
        filas.append((s + 1, ", ".join(partes), len(tramo)))
    return filas


def pagina(contenido, clase="", folio=True):
    pie = f'<footer><span>{e(MARCA)}</span><span class="folio"></span></footer>' if folio else ""
    return f'<section class="pag {clase}">{contenido}{pie}</section>'


paginas = []

# Portada
paginas.append(pagina(f"""
{img('portada', 'portada-foto')}
<div class="portada-velo"></div>
<div class="portada-texto">
  <div class="sello">Devocional para mujeres</div>
  <h1>{e(TITULO)}</h1>
  <p class="sub">{e(SUBTITULO)}</p>
  <ul class="badges"><li>30 lecturas diarias</li><li>Oración y diario</li><li>3 bonos incluidos</li></ul>
  <div class="marca">{e(MARCA)}</div>
</div>""", "portada", folio=False))

# Créditos
paginas.append(pagina(f"""
<div class="creditos">
  <h2>{e(TITULO)}</h2>
  <p>{e(SUBTITULO)}</p>
  <p class="chico">© {e(MARCA)}. Todos los derechos reservados. Este material es de uso personal. No está permitida su reventa ni su distribución total o parcial sin autorización.</p>
  <p class="chico">Texto bíblico tomado de la Santa Biblia, versión Reina-Valera © 1960 Sociedades Bíblicas en América Latina; © renovado 1988 Sociedades Bíblicas Unidas. Utilizado con permiso. Reina-Valera 1960™ es una marca registrada de la American Bible Society y puede ser usada solamente bajo licencia.</p>
</div>""", "centrada"))

# Bienvenida
paginas.append(pagina(f"""
<div class="eyebrow">Bienvenida</div>
<h2>Un lugar para volver a encontrarte con Dios</h2>
<p>Querida amiga: si tenés este devocional en tus manos, es porque algo en vos está buscando volver. Volver a la paz, volver a la oración, volver a ese lugar donde el alma descansa.</p>
<p>No importa si hace años que no abrís la Biblia o si la leés todos los días. Estos treinta días fueron pensados para mujeres reales, con agendas llenas, cansancio acumulado y muchas preguntas. No hace falta tener todo resuelto. Solo hace falta aparecer.</p>
<p>Cada día vas a encontrar una lectura corta, un versículo para guardar en el corazón, una oración para hacer tuya y una pregunta para escribir en tu diario. Diez o quince minutos alcanzan.</p>
<p class="firma">Con cariño,<br>el equipo de {e(MARCA)}</p>""", "texto"))

# Cómo usar
paginas.append(pagina("""
<div class="eyebrow">Antes de empezar</div>
<h2>Cómo usar este devocional</h2>
<ol class="pasos">
  <li><b>Elegí un momento fijo.</b> A la mañana con el primer mate, en la siesta o antes de dormir. Lo importante es que sea siempre el mismo.</li>
  <li><b>Leé sin apuro.</b> Primero la lectura del día, después el versículo. Si podés, leelo dos veces en voz alta.</li>
  <li><b>Hacé tuya la oración.</b> Es una guía: cambiá las palabras, agregá nombres, contale a Dios lo que te pasa.</li>
  <li><b>Escribí.</b> Respondé la pregunta del día en las líneas o en un cuaderno. Al final de los 30 días vas a poder ver tu recorrido.</li>
  <li><b>Si te salteás un día, seguí.</b> No es una carrera. Retomá donde quedaste, sin culpa.</li>
</ol>
<div class="caja"><b>Tus bonos:</b> al final encontrás 30 tarjetas de versículos para imprimir, 21 días de oración por tus hijos y un plan para leer la Biblia completa en un año.</div>""", "texto"))

# Apertura del devocional
paginas.append(pagina(f"""
{img('rincon', 'foto-plena')}
<div class="velo-abajo"></div>
<div class="apertura-texto"><div class="eyebrow claro">Parte 1</div><h2>Los 30 días</h2><p>Cuatro semanas para descansar, soltar, recordar quién sos y seguir con fuerza.</p></div>""", "apertura", folio=False))

for i, (titulo, lectura, cita, versiculo, oracion, pregunta) in enumerate(DIAS, start=1):
    for num, nombre, rango in SEMANAS:
        if i == [1, 8, 15, 22][num - 1]:
            paginas.append(pagina(f"""
<div class="semana-num">Semana {num}</div>
<h2 class="semana-titulo">{e(nombre)}</h2>
<p class="semana-rango">{e(rango)}</p>""", "semana", folio=False))
    paginas.append(pagina(f"""
<div class="dia-cabecera"><span class="dia-num">Día {i}</span><span class="check">☐ Leído</span></div>
<h2 class="dia-titulo">{e(titulo)}</h2>
<blockquote class="versiculo"><p>“{e(versiculo)}”</p><cite>{e(cita)}</cite></blockquote>
<div class="lectura">{parrafos(lectura)}</div>
<div class="oracion"><span class="rotulo">Oración</span><p>{e(oracion)}</p></div>
<div class="diario"><span class="rotulo">Para tu diario</span><p>{e(pregunta)}</p><div class="lineas"></div></div>""", "dia"))

# Bono 1: tarjetas
paginas.append(pagina("""
<div class="eyebrow">Bono 1</div>
<h2>30 tarjetas de versículos</h2>
<p>Imprimí estas páginas, recortá por las líneas punteadas y llevá las tarjetas con vos: en la billetera, pegadas en el espejo, en la heladera o como señalador de tu Biblia. Una para cada día del devocional.</p>
<div class="caja">Consejo: imprimí en papel de 180 g o más para que duren.</div>""", "texto"))
for k in range(0, 30, 4):
    tarjetas = "".join(
        f'<div class="tarjeta"><span class="t-num">{n + 1}</span><p>“{e(DIAS[n][3])}”</p><cite>{e(DIAS[n][2])}</cite></div>'
        for n in range(k, min(k + 4, 30)))
    paginas.append(pagina(f'<div class="tarjetas">{tarjetas}</div>', "tarjetas-pag"))

# Bono 2: hijos
paginas.append(pagina(f"""
{img('hijos', 'foto-plena')}
<div class="velo-abajo"></div>
<div class="apertura-texto"><div class="eyebrow claro">Bono 2</div><h2>21 días de oración por mis hijos</h2><p>Una oración corta para cada día. Podés decirla en voz alta, con tus hijos o mientras duermen.</p></div>""", "apertura", folio=False))
for k in range(0, 21, 3):
    bloques = "".join(
        f'<div class="hijo"><div class="hijo-cab"><span class="dia-num">Día {n + 1}</span> · {e(HIJOS[n][0])}</div>'
        f'<p class="hijo-vers">“{e(HIJOS[n][2])}” <cite>{e(HIJOS[n][1])}</cite></p><p>{e(HIJOS[n][3])}</p></div>'
        for n in range(k, min(k + 3, 21)))
    notas = '<div class="notas"><span class="rotulo">Mis pedidos por mis hijos</span><div class="lineas"></div></div>'
    paginas.append(pagina(bloques + notas, "hijos-pag"))

# Bono 3: plan anual
filas = plan_semanal()
paginas.append(pagina("""
<div class="eyebrow">Bono 3</div>
<h2>La Biblia en un año</h2>
<p>Este plan recorre la Biblia completa en 52 semanas, de Génesis a Apocalipsis. Son unos 23 capítulos por semana: entre 3 y 4 por día. Marcá cada semana cuando la termines. Si te atrasás, no pasa nada: seguí desde donde quedaste.</p>
<div class="caja">Consejo: sumá un salmo por día como oración aparte. Los Salmos y los Proverbios son ideales para eso.</div>""", "texto"))
for k in range(0, 52, 18):
    trs = "".join(f"<tr><td class='sem'>{s}</td><td>{e(t)}</td><td class='cap'>{c}</td><td class='box'>☐</td></tr>"
                  for s, t, c in filas[k:k + 18])
    paginas.append(pagina(f"<table class='plan'><thead><tr><th>Sem.</th><th>Lectura</th><th>Cap.</th><th></th></tr></thead><tbody>{trs}</tbody></table>", "plan-pag"))

# Cierre
paginas.append(pagina(f"""
{img('camino', 'foto-plena')}
<div class="velo-abajo"></div>
<div class="apertura-texto"><h2>Esto recién empieza</h2><p>Lo que Dios empezó en vos, lo va a terminar. Gracias por caminar estos 30 días con nosotras.</p><p class="marca-cierre">{e(MARCA)}</p></div>""", "apertura", folio=False))

with open(os.path.join(AQUI, "plantilla.html"), encoding="utf-8") as f:
    plantilla = f.read()
with open(os.path.join(AQUI, "ebook.html"), "w", encoding="utf-8") as f:
    f.write(plantilla.replace("{{PAGINAS}}", "\n".join(paginas)).replace("{{TITULO}}", e(TITULO)))
print(f"{len(paginas)} páginas generadas")
