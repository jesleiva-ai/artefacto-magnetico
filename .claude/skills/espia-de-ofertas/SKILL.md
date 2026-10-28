---
name: "espia-de-ofertas"
description: "Busca en la Biblioteca de anuncios de Meta ofertas de productos digitales low-ticket que ya están vendiendo en otro mercado/idioma y que cumplen los requisitos del usuario para modelarlas (20–30+ anuncios activos, más de 15 días al aire, sin marca personal). Usar cuando se pida 'buscar ofertas', 'espiar ofertas', 'qué puedo modelar', 'ofertas ganadoras', 'buscar productos para lanzar' o un nicho/idioma para investigar."
model: sonnet
effort: medium
---

# Espía de ofertas

Encuentra ofertas que ya funcionan para modelarlas en otro mercado. Criterios y proceso de Mat: `D:\segundo-cerebro\05_PROCESOS\ELEGIR_Y_MODELAR_OFERTAS.md` (leerlo primero; si dice algo distinto a esta skill, manda ese archivo).

## Requisitos de una oferta "modelable" (todos)

1. **20 o 30 anuncios activos o más** del mismo anunciante/producto.
2. Anuncios corriendo **hace más de 15 días** (fecha de inicio del anuncio más viejo activo).
3. **Sin marca personal:** no depende de la cara, nombre o fama de una persona.
4. **Producto digital low-ticket** que se pueda vender a USD 5–40 (curso, ebook, plantilla, imprimible, recurso, herramienta, app).
5. Se puede lanzar en un **mercado/idioma distinto** al original.

## Cómo buscar

1. **Preguntar (una sola vez, proponiendo):** nicho o palabras clave, idioma/país donde buscar, idioma/país donde se lanzaría. Si no hay preferencia, proponer 3 nichos low-ticket probados (ej.: espiritualidad, manualidades, cocina, oficios, fitness, crianza, plantillas) y 2 mercados de búsqueda (ej.: portugués BR, inglés US).
2. **Primero el robot Nexus Profit** (si está conectado): skill `cazador-de-ofertas` / herramienta `descubrir_ofertas` con `min_copias: 20` y `min_dias: 15` (reglas de Mat), más `tendencias`. Guía: `D:\segundo-cerebro\05_PROCESOS\ROBOT_NEXUS_PROFIT.md`. Después confirmar las mejores en Meta.
3. **Buscar en la Biblioteca de anuncios de Meta** (para confirmar, o si el robot no está):
   - Si está la herramienta de Meta Ads con búsqueda en la biblioteca (`ads_library_search`), usarla.
   - Si no, usar el navegador en `https://www.facebook.com/ads/library/` con "Todos los anuncios", el país y la palabra clave.
   - Buscar en el idioma del mercado de origen (ej.: "ebook", "guia", "curso", "plantilla", "pdf", "imprimible" traducido).
4. **Agrupar por anunciante/página** y contar anuncios activos de la misma oferta.
5. **Revisar fecha de inicio** de los anuncios activos: quedarse con los que tienen anuncios de más de 15 días.
6. **Descartar** marca personal, productos físicos, apps de entretenimiento (series cortas, novelas), high-ticket, apuestas, salud con promesas médicas, dinero fácil, y todo lo que viole políticas de Meta.
7. **Abrir la landing** de las que quedan (link del anuncio o `analizar_landing` del robot) y anotar: producto, precio, moneda, formato, bonos, order bumps visibles, garantía, plataforma de cobro si se ve. Pasar `detector-cloaker`.
8. **Chequear que no exista ya** en el mercado destino (buscar el mismo producto en el idioma destino): si ya hay muchos anunciantes ahí, marcarlo como "mercado destino competido".

## Entrega

Tabla ordenada de mejor a peor:

| # | Oferta / anunciante | Nicho | Mercado origen | Anuncios activos | Días del más viejo | Precio | Formato | ¿Marca personal? | Mercado destino propuesto | Competencia en destino | Link biblioteca | Link landing |

Debajo, para las 3 mejores: por qué es buena, qué se modelaría (estructura, no textos) y qué escalera de valor podría tener (skill `escalera-de-valor`).

**Guardar** el resultado en `D:\segundo-cerebro\06_PROYECTOS\ofertas\AAAA-MM-DD_espia_[nicho].md` (crear la carpeta si no existe).

## Reglas

- Los números (anuncios activos, días) se anotan **tal cual se vieron, con la fecha de la búsqueda**. Si no se pudo contar, `desconocido`, no un número inventado.
- **Modelar no es copiar:** se toma la estructura y el ángulo; textos, imágenes, marca y testimonios se hacen propios. No descargar ni guardar creativos ajenos salvo capturas de referencia en `08_REFERENCIAS`.
- No abrir ni completar formularios ni checkouts de terceros.
- Siguiente paso sugerido: skill `modelar-ofertas` con la oferta elegida.
