# Yoga en Silla · notas del proyecto

Producto de **Mi Biblioteca de Infoproductos**. App web (PWA) de yoga en silla para mujeres de 45 a 65 años.
Venta: Meta Ads → WhatsApp Business. Precio: USD 7 / ARS 9.999 (pago único).

## Estado del prototipo (`index.html`)

- **Hoy**: reto de 21 días (3 semanas: Llegar, Sostener, Hacerlo tuyo), práctica del día, semana, atajos según el ánimo, consejo del día.
- **Rutinas**: 9 rutinas (3 a 15 min) y biblioteca de 25 movimientos con figura animada, pasos y versión más suave.
- **Reproductor guiado**: figura animada sincronizada con la respiración, cuenta regresiva, voz en español (speechSynthesis), pausa/anterior/siguiente, pantalla siempre encendida.
- **Progreso**: días practicados, minutos, racha, grilla del reto, calendario del mes, registro de cómo se sintió después.
- **Mi espacio**: nombre, tamaño de letra (3 niveles), voz, meta semanal, horario preferido, seguridad, reinicio.
- Aviso de seguridad obligatorio antes de la primera práctica.
- Los datos se guardan en el navegador de cada compradora (localStorage). No hay cuentas ni servidor.
- Textos 100 % originales. No se copió texto, imagen ni marca del ebook.

## Licencia (certificado PLR de PLR's Factory)

Permite: vender a cliente final con marca propia, rebrandear, modificar capítulos, usar como contenido premium en membresía paga, comunidad, afiliados.
Prohíbe: ofrecerlo gratis, como bono, empaquetado como relleno, revender derechos, contactar al autor.

Implicancias:
- La app se vende como producto propio con precio propio. No incluirla gratis ni como bono de otro producto.
- Una demo gratuita solo puede usar contenido original (como el actual), no el del ebook.
- Guardar el comprobante de compra: el certificado no tiene número de licencia ni el nombre del comprador.

## Auditoría del material original

| Material | Estado | Acción |
|---|---|---|
| Ebook principal (PDF de 53 MB) | Solo imágenes, sin texto legible | Exportar páginas como imagen para revisar los ejercicios |
| Ficha de producto | Público 22 a 55 años, enfoque oficina | Reorientar a 45 a 65 |
| Promesas de salud (inmunidad, dolor lumbar, digestión, recuperación) | Riesgo legal y rechazo en Meta | No usar. Hablar de bienestar, movimiento suave, hábito |
| Bono 1 (microhábitos) | Útil | Integrado como rutina "Para días difíciles", con texto nuevo |
| Bono 2 (oficina) | Secuencias 1 y 3 idénticas; "activación" con respiración 4-7-8 (relajante); cita una "sacudida de hombros" que no existe | Reemplazado por "Pausa de 3 minutos" |
| Bono 3 (grupo de WhatsApp) | Encaja con el embudo | Definir quién lo modera |
| Autora "Valeria Torres" | Parece un personaje ficticio | No usar. Conseguir validación de una instructora real |
| Ilustraciones del ebook | Sin revisar | El prototipo usa figuras propias generadas por código |

## Antes de vender (pendientes)

1. **Validación profesional**: que una instructora de yoga certificada revise los 25 movimientos, sus versiones suaves y las contraindicaciones (por ejemplo, el pliegue hacia adelante con presión alta).
2. **Acceso de compradoras**: hoy cualquiera con el link usa la app. Opciones: link privado por compradora, código de acceso o membresía.
3. **Hosting propio + PWA**: dominio, manifest, ícono, service worker para uso sin conexión e instalación en la pantalla de inicio.
4. **Recordatorios**: el horario se guarda, pero las notificaciones reales requieren la app instalada como PWA.
5. **Visuales**: opcionalmente, reemplazar las figuras por ilustraciones o videos cortos con un personaje consistente.
6. **Voz**: decidir entre tú (neutro, toda Latinoamérica) y vos (Argentina). El prototipo usa tú.
7. **Aviso legal** en la página de venta y en la app.
