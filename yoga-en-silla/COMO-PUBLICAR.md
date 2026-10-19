# Cómo publicar Yoga en Silla

Esta carpeta es la app completa. No necesita servidor, base de datos ni programación:
son archivos estáticos que cualquier hosting puede servir.

```
yoga-en-silla/
├── index.html             la app
├── manifest.webmanifest   nombre e ícono al instalarla en el celular
├── sw.js                  permite usarla sin internet después de la primera vez
├── _headers               configuración para Netlify y Cloudflare Pages
└── icons/                 íconos de la app
```

**Requisito único: HTTPS** (el candado). Todas las opciones de abajo lo dan gratis.

## Dónde alojarla

| Opción | Costo | Dificultad | Ideal para |
|---|---|---|---|
| **Netlify Drop** | Gratis | Arrastrar y soltar | Empezar hoy mismo |
| **Cloudflare Pages** | Gratis, sin límite de visitas | Arrastrar y soltar | Cuando escales con anuncios |
| GitHub Pages | Gratis | Media | Si ya usas GitHub |
| Tu hosting (Hostinger, etc.) | El que ya pagas | Subir por el administrador de archivos | Si ya tienes dominio y hosting |

**No sirven**: Google Drive, Dropbox ni Canva (no ejecutan apps), ni subir el zip a Hotmart como archivo descargable (la compradora tendría que descomprimirlo y no podría instalarla).

### Opción recomendada: Netlify Drop (5 minutos)

1. Descomprime el zip.
2. Entra a **app.netlify.com/drop** y crea una cuenta gratis.
3. Arrastra la carpeta `yoga-en-silla` a la página.
4. Netlify te da un link tipo `https://nombre-raro.netlify.app`. Ya funciona.
5. En *Site configuration → Change site name* ponle un nombre, por ejemplo `yogaensilla-biblioteca.netlify.app`.
6. Para actualizar: *Deploys* → arrastra la carpeta nueva.

### Cloudflare Pages

1. Entra a **dash.cloudflare.com** → *Workers y Pages* → *Crear* → *Pages* → *Subir recursos*.
2. Ponle un nombre al proyecto y arrastra la carpeta.
3. Queda en `https://nombre.pages.dev`.

### Dominio propio (opcional)

Por ejemplo `app.mibibliotecadeinfoproductos.com`. Se conecta desde Netlify o Cloudflare
en la sección *Domains*. El dominio cuesta unos USD 10 a 15 por año. Da más confianza a la compradora.

## Cómo distribuirla

1. **Cobro**: Mercado Pago (link de pago, ARS 9.999) para Argentina; Hotmart, PayPal o Stripe (USD 7) para el resto.
2. **Entrega**: al confirmarse el pago, envías por WhatsApp (o automático por mail desde Hotmart) el link de la app y este mensaje:

> ¡Bienvenida a Yoga en Silla! Tu app: [LINK]
> Para tenerla como app en tu celular:
> • **Android**: ábrela en Chrome → menú ⋮ → *Instalar app* o *Agregar a la pantalla principal*.
> • **iPhone**: ábrela en Safari → botón *Compartir* → *Agregar a inicio*.
> Después la abres desde el ícono, como cualquier app.

3. **Área de miembros (opcional)**: si vendes con Hotmart o Kiwify, pega el link dentro de una lección del curso. Así queda guardado en su cuenta.

## Protección del acceso: qué esperar

Hoy la app no pide usuario ni contraseña: quien tiene el link puede usarla.
Es lo habitual en productos de este precio, pero conviene saberlo:

- **Nivel 1 (actual)**: link no público. La app ya tiene `noindex`, así que Google no la muestra. Usa un nombre difícil de adivinar.
- **Nivel 2**: link dentro del área de miembros de Hotmart o Kiwify. La compradora necesita su cuenta para encontrarlo, aunque podría compartirlo.
- **Nivel 3**: login real por email (por ejemplo Cloudflare Access o Supabase). Lo armamos más adelante si ves que se comparte mucho.

## Datos de las compradoras

El progreso (días del reto, nombre, ajustes) se guarda **en el celular de cada compradora**.
No tienes que administrar nada. Si cambia de celular o borra los datos del navegador, empieza de cero.

## Antes de publicar

- [ ] Revisión de los movimientos por una instructora de yoga certificada.
- [ ] Aviso legal en la página de venta: "movimientos suaves de bienestar, no reemplaza atención médica".
- [ ] Probar la instalación en un Android y en un iPhone.
