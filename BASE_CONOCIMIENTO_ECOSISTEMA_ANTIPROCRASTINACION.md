# Base de conocimiento · Ecosistema Anti‑Procrastinación

> Documento para entrenar a la agente comercial de WhatsApp (MaxAgente).
> Auditoría realizada el 17/10/2026 sobre los archivos reales del producto.
> Regla de uso para la agente: **si algo no está en este documento, no lo afirmes; derivá la consulta a la dueña.**

---

## 0. Fuentes auditadas y método

| Fuente | Qué es | Cómo se verificó |
|---|---|---|
| Artifact de Claude **"Ecosistema Anti‑Procrastinación"** (`claude.ai/artifact/5gQwk1iyH5RVjpp7VWqNxG`, última actualización 13/10/2026) | **La aplicación** que recibe la compradora | Lectura completa del HTML, CSS y JavaScript + prueba funcional en navegador (Chromium, pantalla de celular 390×844) |
| Artifact de Claude **"Ecosistema Anti‑Procrastinación · Acceso"** (`claude.ai/artifact/XBpacuU7EfFsMKtA5aqc7i`, última actualización 14/10/2026) | **Página de venta/acceso** (precio, pago, entrega) | Lectura completa del HTML |
| 15 archivos PDF en Google Drive enlazados desde la app | **Biblioteca** (5 guías + 10 bonos) | Se comprobó que cada enlace existe, su nombre real, tamaño y permisos de acceso |
| `leivajesica-mkt.systeme.io/acceso` | Página en systeme.io indicada por la dueña | **No se pudo abrir** desde el entorno de auditoría (red bloqueada). Su contenido no está verificado |

Notas:
- El repositorio `artefacto-magnetico` contiene otro producto (**"Monetiza YA"**). No forma parte del Ecosistema Anti‑Procrastinación y no se usa en este documento.
- No se modificó el código de la aplicación.

---

## 1. Ficha completa del producto

### 1.1 Qué es
El **Ecosistema Anti‑Procrastinación** es una **aplicación web** (se abre desde el navegador, no se descarga de ninguna tienda), pensada para usarse en el celular. Reúne en un solo lugar:

- un **camino guiado de 28 pasos** (organizado en 4 etapas de 7 pasos),
- una **biblioteca** con **5 guías y 10 bonos en PDF** (15 materiales en total),
- una sección de **Rescate** con respiración guiada de 2 minutos y un plan para días caóticos,
- una sección **Mi plan** con la planificación diaria 3‑2‑1 y un temporizador de enfoque de 25 minutos.

Lema dentro de la app: *"De la intención a la acción"*.
Mensaje central: *"Tu problema no es la falta de voluntad. Es que nadie te dio un sistema simple. Este es el tuyo: un paso por día, a tu ritmo y sin culpa."*

### 1.2 Qué problema práctico busca resolver
Ayudar a una persona que posterga sus tareas a **pasar de la intención a la acción** con:
- una indicación clara de **qué hacer hoy** ("Tu próximo paso"),
- **pasos chicos** y concretos,
- un **registro visible del avance**,
- herramientas rápidas para **bajar la ansiedad o la sobrecarga** antes de seguir.

La app se presenta a sí misma como **material educativo** que **no reemplaza la atención de un profesional de la salud** (texto literal en la sección Rescate y en la página de venta).

### 1.3 Secciones (barra de pestañas fija abajo)
La app tiene **5 pestañas**, siempre visibles en la parte inferior de la pantalla:

| Pestaña | Para qué sirve |
|---|---|
| **Inicio** | Saludo, porcentaje de avance, cuántos pasos de 28 lleva, etapa actual, **tarjeta "Tu próximo paso"** y acceso rápido a Rescate |
| **Camino** | Los 28 pasos con casilla para marcar, divididos en 4 etapas, con barra de progreso |
| **Biblioteca** | Las 5 guías con su descripción, botón "Abrir guía" y sus 2 bonos cada una |
| **Rescate** | Respiración guiada de 2 minutos, plan de 4 pasos para un día caótico, enlaces a 4 bonos de ayuda rápida y aviso de salud |
| **Mi plan** | Planificador 3‑2‑1 (6 campos que se guardan solos) y temporizador de enfoque de 25 minutos |

### 1.4 Herramientas y qué hace exactamente cada una

**a) Indicador de avance (Inicio y Camino)**
- Anillo con el **porcentaje** completado (pasos marcados ÷ 28, redondeado).
- Texto "X de 28 pasos completados" y el nombre de la **etapa en curso**.
- Barra de progreso en la pestaña Camino.
- Contador por etapa (por ejemplo "3/7").

**b) "Tu próximo paso" (Inicio)**
- Muestra automáticamente el **primer paso sin marcar** en orden (por ejemplo "Día 2 · Planificá sin complicarte") con su descripción.
- Botón **"Ir a mi camino"**.
- Al completar los 28 pasos muestra: *"¡Completaste todo el camino!"* y *"Volvé a tus herramientas favoritas cada vez que lo necesites."*

**c) Camino de 28 pasos (Camino)**
- Cada paso tiene: etiqueta "Día N", título, instrucción breve y una **casilla redonda** para marcarlo.
- Al marcarlo, el título queda **tachado** y se actualiza el avance.
- Se puede **desmarcar** tocando de nuevo.
- El **primer paso de cada etapa** tiene un botón para abrir la guía correspondiente.
- Detalle completo en la sección 2.

**d) Biblioteca (Biblioteca)**
- 5 tarjetas, una por guía, con portada de color, nombre, descripción y botón **"Abrir guía"**.
- Debajo de cada guía, sus **2 bonos** (marcados con 🎁).
- Cada enlace abre el PDF en **Google Drive en una pestaña nueva**.
- Detalle completo en la sección 3.

**e) Respiración de 2 minutos (Rescate)**
- Botón **"Empezar"**: un círculo se agranda y se achica guiando el ritmo **Inhalá 4 · Sostené 2 · Exhalá 6** (ciclos de 12 segundos, 10 ciclos = 2 minutos).
- Muestra el tiempo restante ("1:59 restantes").
- El botón cambia a **"Detener"** para cortar cuando quieras.
- Al terminar muestra **"Bien hecho 💚"**.
- Es **solo visual**: no tiene audio ni voz guía.

**f) Plan para un día caótico (Rescate)**
Cuatro pasos fijos de texto:
1. **Elegí una sola cosa.** La que, si la hacés, hace que el día cuente.
2. **Achicala a 5 minutos.** No "terminar el informe", sino "abrir el archivo y escribir el título".
3. **Poné un temporizador** y empezá antes de sentirte lista. Las ganas aparecen después de empezar.
4. **Soltá el resto sin culpa.** Mañana lo planificás con la regla 3‑2‑1.

Incluye un enlace a "Abrir el Plan de emergencia completo" (bono en PDF).

**g) Más ayuda rápida (Rescate)**
Accesos directos a 4 bonos: Kit de respiración consciente · Kit de emergencia emocional · Reset mental para días ansiosos · Dormir sin ansiedad en 7 días.

**h) Planificador 3‑2‑1 (Mi plan)**
- Basado en la regla 3‑2‑1 de la guía *Hackea tu Procrastinación*: **3 tareas principales, 2 de apoyo y 1 microacción**.
- 6 campos de texto con ejemplos de guía: Principal 1, Principal 2, Principal 3, Apoyo 1, Apoyo 2, Microacción.
- **Se guarda solo** mientras escribís (aparece "Guardado en este celular.").
- No hay botón para "nuevo día", historial de días anteriores ni casillas para tachar tareas del plan: para cambiar el plan se borra y se reescribe el texto.

**i) Bloque de enfoque de 25 minutos (Mi plan)**
- Temporizador tipo Pomodoro que arranca en **25:00**.
- Botones: **Empezar** → **Pausar** → **Seguir**, y **Reiniciar** (vuelve a 25:00).
- Al llegar a cero muestra **"¡Listo!"**.
- Sugiere "celular en modo avión" y "después, 5 de descanso", pero **no cuenta automáticamente el descanso de 5 minutos**.
- **No suena ni envía notificaciones** al terminar: hay que mirar la pantalla.

### 1.5 Cómo navega la usuaria
1. Abre el enlace de la app en el navegador del celular.
2. Llega a **Inicio**, donde ve su avance y su próximo paso.
3. Se mueve tocando las **5 pestañas de abajo** (Inicio, Camino, Biblioteca, Rescate, Mi plan).
4. Los botones "Ir a mi camino" y "Abrir Rescate" del Inicio llevan directo a esas pestañas.
5. Los materiales (PDF) se abren en **otra pestaña** del navegador (Google Drive). Para volver, se vuelve a la pestaña de la app.
6. La app **recuerda la última pestaña** usada y vuelve a abrirse ahí.
7. También se puede entrar directo a una sección agregando al final del enlace `#camino`, `#biblioteca`, `#rescate` o `#plan` (verificado: funciona al abrir el enlace).

### 1.6 Qué información guarda y cómo
La app guarda **3 datos**, usando el almacenamiento interno del navegador (`localStorage`):

| Dato | Clave interna | Contenido |
|---|---|---|
| Pasos marcados del camino | `eap_done` | Qué pasos de los 28 están tildados |
| Plan del día | `eap_plan` | El texto de los 6 campos de Mi plan |
| Última pestaña | `eap_tab` | En qué sección estaba |

Características verificadas:
- **No hay cuenta, usuario ni contraseña.** No se piden datos personales.
- Los datos **quedan solo en ese celular y en ese navegador**. No se suben a ningún servidor ni los ve la dueña.
- Al **cerrar y volver a abrir** la app en el mismo navegador, el progreso y el plan **siguen ahí** (verificado recargando la página).
- **En otro navegador u otro dispositivo, la app empieza de cero** (verificado: un navegador nuevo mostró 0 pasos).
- **No guarda**: el estado del temporizador ni de la respiración (se reinician al salir), fechas, historial ni notas por paso.

### 1.7 Funciones que dependen del navegador o del dispositivo
- **Conexión a internet:** necesaria para abrir la app y los PDF (verificado: sin conexión la página no carga). No tiene modo sin conexión.
- **Almacenamiento del navegador:** si la usuaria **borra los datos de navegación**, usa **modo incógnito/privado** o cambia de navegador, **pierde el progreso y el plan**.
- **Google Drive:** los 15 materiales se abren desde Google Drive. Su visualización depende del visor de Drive o de la app de Drive del celular.
- **Temporizadores:** funcionan con la pantalla de la app abierta. Si el celular bloquea la pantalla o la usuaria cambia de app, el navegador puede pausar o atrasar el conteo (comportamiento habitual de los navegadores; no probado en celulares reales).
- **Modo oscuro:** la app cambia sola a colores oscuros si el celular está en modo oscuro (verificado).
- **Tipografías:** se cargan desde Google Fonts; si no cargan, la app usa letras del sistema y sigue funcionando.
- **Accesibilidad:** respeta la opción de "reducir movimiento" del sistema (desactiva animaciones).

### 1.8 Funcionalidades incompletas, límites o que requieren verificación
- **No hay recordatorios ni notificaciones** (ni diarias ni al terminar el temporizador).
- **No hay sonido** en la respiración ni en el temporizador.
- **El descanso de 5 minutos** se menciona pero no está programado.
- **Mi plan no tiene historial** ni botón para empezar un día nuevo.
- **No se puede exportar ni sincronizar** el progreso entre dispositivos.
- **No hay buscador** ni notas personales por paso.
- **No hay bloqueo de contenido:** cualquier persona con el enlace de la app puede abrirla; los 15 PDF están compartidos como "cualquier persona con el enlace" (ver 3.3).
- En la Etapa 3, la guía *Ansiedad Detox* y sus bonos se usan en los pasos 18 a 20, pero el botón de la etapa abre *Stress Detox*. Ansiedad Detox se abre desde la Biblioteca.
- El paso 14 menciona el bono "¿Cuál es tu por qué?" sin enlace directo en el paso; se abre desde la Biblioteca (guía *Domina tu Crítico Interno*).
- **Pendiente verificar:**
  - si el enlace de claude.ai se abre para una persona **sin cuenta de Claude**, en distintos celulares;
  - si se puede **agregar a la pantalla de inicio** desde ese enlace (la página de venta lo promete; la app no tiene configuración específica para instalarse como app);
  - qué muestra la página de systeme.io `/acceso`.

---

## 2. Programa de 28 días ("Tu camino")

### 2.1 Cómo funciona
- **4 etapas × 7 pasos = 28 pasos.** Cada paso lleva la etiqueta "Día 1" a "Día 28".
- Instrucción que ve la usuaria: *"Hacé un paso por día. Si un día no podés, no pasa nada: retomás donde quedaste."*
- La página de venta indica que cada paso está pensado para **5 a 15 minutos**.

### 2.2 Cómo se registra el progreso
- La usuaria **marca la casilla** del paso cuando lo hizo. Se tacha y suma al avance.
- Se actualizan: el anillo de porcentaje, "X de 28", la barra, el contador de la etapa y "Tu próximo paso".
- El registro **es manual**: la app no verifica que el ejercicio se haya hecho.
- Se puede **desmarcar** un paso.

### 2.3 Qué pasa si interrumpe el recorrido
- **Nada se pierde ni se reinicia** por dejar días sin usar: los "días" son etiquetas, **no están atados al calendario**. No hay fechas, rachas ni penalizaciones.
- Al volver (mismo celular y navegador), encuentra sus pasos marcados y "Tu próximo paso" le muestra el primero pendiente.
- **Excepción:** si borró los datos del navegador o cambió de dispositivo, el progreso aparece en cero.

### 2.4 ¿Avance libre o secuencia obligatoria?
- **Avance libre.** Se puede marcar **cualquier paso en cualquier orden** (verificado: se marcó el Día 5 antes que el Día 2). No hay pasos bloqueados.
- La app **sugiere** el orden: "Tu próximo paso" siempre muestra el primer paso sin marcar, empezando por el Día 1.
- Nada obliga a hacer un paso por día: se pueden hacer varios el mismo día.

### 2.5 Contenido día por día (texto literal de la app)

**Etapa 1 · Activá tu acción** — guía asociada: *Hackea tu Procrastinación* (botón en el Día 1)

| Día | Objetivo (título) | Instrucción |
|---|---|---|
| 1 | Identificá tus bloqueos | Anotá qué hacés cuando sabés que deberías estar haciendo otra cosa, y qué excusa te repetís más. |
| 2 | Planificá sin complicarte | Usá la regla 3‑2‑1 en la pestaña Mi plan. Solo eso, nada más. |
| 3 | Creá tu ritual de la mañana | Los primeros 10 minutos sin celular: agua, estirarte y repasar tu plan. |
| 4 | Empezá con un microhábito | Elegí una acción tan chica que no puedas fallar, y atala a algo que ya hacés. |
| 5 | Vencé la resistencia | Cuando no tengas ganas, hacé solo 5 minutos. Empezar es la parte difícil. |
| 6 | Decí que no sin culpa | Elegí una cosa que hoy vas a dejar pasar para proteger tu energía. |
| 7 | Revisión de la semana | 5 minutos: qué funcionó, qué no, y qué ajustás para la próxima. |

**Etapa 2 · Cambiá tu diálogo interno** — guía asociada: *Domina tu Crítico Interno* (botón en el Día 8)

| Día | Objetivo (título) | Instrucción |
|---|---|---|
| 8 | Reconocé esa voz | Durante el día, anotá 3 frases que te dijiste a vos misma. Sin juzgarlas. |
| 9 | Ponele nombre al patrón | ¿Es perfeccionismo, comparación o miedo al error? Identificá cuál aparece más. |
| 10 | Reescribí una frase | Tomá una de tus frases y escribila como se la dirías a una amiga. |
| 11 | Una afirmación realista | Creá una frase validadora que puedas creer de verdad, y repetila a la mañana. |
| 12 | Practicá autocompasión | La próxima vez que te equivoques, respirá y decite: esto le pasa a cualquiera. |
| 13 | Menos comparación | Hoy silenciá 3 cuentas que te hacen sentir que estás atrasada. |
| 14 | Encontrá tu por qué | Leé el bono ¿Cuál es tu por qué? y escribí tu respuesta en una línea. |

**Etapa 3 · Bajá el estrés y la ansiedad** — guía asociada: *Stress Detox* (botón en el Día 15)

| Día | Objetivo (título) | Instrucción |
|---|---|---|
| 15 | Empezá Stress Detox | Leé la primera parte de la guía y marcá una idea para aplicar hoy. |
| 16 | Respiración diaria | Hacé la respiración de 2 minutos en Rescate, una vez al día. |
| 17 | Reset mental | Abrí el bono Reset mental para días ansiosos y probá un ejercicio. |
| 18 | Empezá Ansiedad Detox | Leé la primera parte y anotá qué situaciones te disparan ansiedad. |
| 19 | Noche 1 sin ansiedad | Arrancá el sistema de 7 días para dormir sin ansiedad. |
| 20 | Comé a tu favor | Elegí una receta del plan de alimentación anti‑estrés para esta semana. |
| 21 | Tu kit personal | Anotá las 3 herramientas que más te sirvieron para tus días difíciles. |

**Etapa 4 · Recuperá tu energía** — guía asociada: *Cortisol Detox* (botón en el Día 22)

| Día | Objetivo (título) | Instrucción |
|---|---|---|
| 22 | Empezá Cortisol Detox | Leé la primera parte y elegí un hábito para sumar. |
| 23 | Ritmo de descanso | Agendá pausas reales entre tus bloques de enfoque. |
| 24 | Plan de 3 días | Hacé el bono 3 días para liberarte del estrés extremo. |
| 25 | Contra la fatiga | Aplicá una idea del plan para neutralizar tu fatiga crónica. |
| 26 | Tu entorno a favor | Prepará tu espacio la noche anterior para empezar sin fricción. |
| 27 | Mirá tu progreso | Volvé a la Etapa 1 y fijate todo lo que ya cambiaste. |
| 28 | Tu nuevo sistema | Elegí los 3 hábitos que te quedás para siempre y escribilos en Mi plan. |

### 2.6 Actividades disponibles en el camino
Los pasos combinan: **escritura y reflexión** (días 1, 7, 8–10, 14, 21, 28), **planificación** (días 2, 23, 26, 28 con Mi plan), **hábitos y microacciones** (días 3–6, 11–13, 22, 25), **lectura de guías y bonos** (días 14, 15, 17–20, 22, 24, 25) y **respiración guiada** (día 16 con Rescate).

> Importante: el camino da la **consigna**; el desarrollo de cada tema está en los PDF. Para escribir o anotar, la usuaria usa papel o sus propias notas: **la app no tiene espacio para escribir dentro de cada paso** (solo los 6 campos de Mi plan).

---

## 3. Biblioteca digital

### 3.1 Recursos (nombre en la app · nombre real del archivo)
Todos son **PDF alojados en Google Drive** (cuenta propietaria: la de la dueña). Todos los enlaces fueron verificados el 17/10/2026: **existen y no hay enlaces rotos ni faltantes**.

| # | Tipo | Nombre que ve la usuaria | Archivo real en Drive | Temática (según la app) | Peso aprox. |
|---|---|---|---|---|---|
| 1 | Guía | **Hackea tu Procrastinación** (etiqueta "7 pasos") | EBOOK_ HACKEA TU PROCRASTINACIÓN.pdf | El método central: planificar sin agobio, crear el ritual diario y vencer la resistencia mental | 50 MB |
| 2 | Bono | Productividad para autodidactas | BONO 1_ GUÍA "PRODUCTIVIDAD PARA AUTODIDACTAS".pdf | Productividad | 13 MB |
| 3 | Bono | Plan de emergencia para días caóticos | BONO 2_ PLAN DE EMERGENCIA PARA DÍAS CAÓTICOS.pdf | Días desordenados | 13 MB |
| 4 | Guía | **Domina tu Crítico Interno** ("Diálogo interno") | EBOOK_DOMINA TU CRÍTICO INTERNO.pdf | Reconocer la voz que juzga y cambiarla por una que acompañe | 51 MB |
| 5 | Bono | ¿Cuál es tu por qué? Una mirada interior para vivir con sentido | BONO 1_¿CUÁL ES TÚ POR QUÉ_ UNA MIRADA INTERIOR PARA VIVIR CON SENTIDO.pdf | Propósito y motivación | 26 MB |
| 6 | Bono | Kit de emergencia emocional para días críticos | BONO 2_KIT DE EMERGENCIA EMOCIONAL PARA DÍAS CRÍTICOS.pdf | Días emocionalmente difíciles | 10 MB |
| 7 | Guía | **Stress Detox** ("Calma") | EBOOK_ STRESS DETOX.pdf | Bajar la carga del día a día y recuperar la calma | 57 MB |
| 8 | Bono | Reset mental para días ansiosos | BONO 1_ RESET MENTAL PARA DÍAS ANSIOSOS.pdf | Ansiedad cotidiana | 12 MB |
| 9 | Bono | Kit de respiración consciente para momentos de caos | BONO 2_ KIT DE RESPIRACIÓN CONSCIENTE PARA MOMENTOS DE CAOS.pdf | Respiración | 8 MB |
| 10 | Guía | **Ansiedad Detox** ("Mente en paz") | ANSIEDAD DETOX.pdf | Que la ansiedad deje de manejar los días y las noches | 54 MB |
| 11 | Bono | El sistema de 7 días para dormir sin ansiedad | BONO 1_ EL SISTEMA DE 7 DÍAS PARA DORMIR SIN ANSIEDAD.pdf | Descanso nocturno | 8 MB |
| 12 | Bono | Plan de alimentación anti‑estrés: 5 recetas | BONO 2_ PLAN DE ALIMENTACIÓN ANTI-ESTRÉS_ 5 RECETAS DELICIOSAS.pdf | Recetas | 10 MB |
| 13 | Guía | **Cortisol Detox** ("Energía") | EBOOK CORTISOL DETOX.pdf | Hábitos para salir del modo alerta y recuperar la energía | 103 MB |
| 14 | Bono | 3 días para liberarte del estrés extremo | BONO 1. 3 DÍAS PARA LIBERARTE DEL ESTRÉS EXTREMO.pdf | Estrés intenso | 23 MB |
| 15 | Bono | El plan para neutralizar tu fatiga crónica | BONO 2. EL PLAN PARA NEUTRALIZAR TU FATIGA CRÓNICA.pdf | Cansancio | 16 MB |

Total: **5 guías + 10 bonos = 15 materiales**, en **formato PDF**.

> La auditoría verificó la **existencia, nombre, formato y permisos** de cada PDF. **No se leyó el contenido interno de los PDF**, así que la agente no debe describir capítulos, técnicas ni páginas que no figuren arriba.

### 3.2 Cómo se accede
- Desde **Biblioteca**: botón "Abrir guía", tocando la portada de color o tocando el nombre de un bono 🎁.
- Desde **Camino**: botón "Abrir [guía]" en el primer paso de cada etapa.
- Desde **Rescate**: "Abrir el Plan de emergencia completo" y los 4 accesos de "Más ayuda rápida".
- Cada enlace abre el PDF en **Google Drive, en una pestaña nueva**. Desde ahí se puede leer y, con las opciones de Drive, descargar.

### 3.3 ¿Integrado o alojado externamente?
- **Alojado externamente** en Google Drive. Los PDF **no están dentro de la app**: la app solo tiene los enlaces.
- Permisos verificados en los 15 archivos: **"Cualquier persona con el enlace puede ver"**. No hace falta iniciar sesión en Google para abrirlos.
- Implicancia: quien tenga un enlace puede abrir ese PDF aunque no haya comprado.
- **Pesos altos (8 a 103 MB):** con datos móviles o mala señal pueden tardar en abrir. Recomendar wifi para la primera apertura o descarga.

### 3.4 Enlaces rotos o recursos faltantes
- **Ninguno detectado**: los 15 enlaces responden y apuntan al archivo correcto.
- Depende de la dueña mantenerlos: si mueve a la papelera, borra o cambia los permisos de un archivo en Drive, el enlace deja de funcionar para las compradoras.

---

## 4. Experiencia de la compradora

### 4.1 Proceso de compra y acceso (según la página "Acceso")
1. **Paga con Mercado Pago** desde el botón de la página (tarjeta, dinero en cuenta o efectivo, según el texto de la página).
2. **Envía el comprobante por WhatsApp** con el botón "Ya pagué: enviar comprobante" (abre un chat con el mensaje: *"Hola! Ya pagué el Ecosistema Anti‑Procrastinación, te mando el comprobante"*).
3. **Recibe el link de su app** cuando la dueña ve el mensaje. *"Si es de madrugada, te llega a primera hora."*

La entrega es **manual**: no hay envío automático tras el pago.

### 4.2 ¿Necesita instalar algo?
- **No.** Se abre desde el navegador del celular con el enlace recibido.
- No hay versión en Play Store ni App Store.
- No pide registrarse ni crear contraseña dentro de la app.
- Para leer los PDF alcanza con el visor de Google Drive (o la app de Drive si la tiene instalada).

### 4.3 Compatibilidad verificable
- **Verificado:** funciona en navegador Chromium (motor de Google Chrome y de la mayoría de los navegadores de Android) con pantalla tipo celular. Probados: las 5 pestañas, marcar y desmarcar pasos, avance, biblioteca, respiración, temporizador, guardado del plan, recarga de página y modo oscuro, **sin errores**.
- **Diseño:** pensado para celular (columna única, barra de pestañas abajo); también se ve en computadora, con el contenido centrado.
- **No verificado en dispositivos reales:** iPhone/Safari, celulares Android de gama baja, tablets.

### 4.4 Persistencia de los datos
- El progreso y el plan **se guardan solos en el celular y navegador** donde se usan.
- **Se conservan** al cerrar y reabrir.
- **Se pierden** si: se borran los datos o el historial del navegador, se usa modo incógnito o se abre el enlace en otro navegador o dispositivo.
- **No hay copia de seguridad** ni forma de recuperarlos.

### 4.5 Posibles limitaciones (para responder con honestidad)
- Necesita **internet**.
- **Sin recordatorios** ni notificaciones.
- **Sin sonido** en respiración y temporizador.
- Progreso **no sincronizado** entre dispositivos.
- Materiales **en PDF externo** (Drive), algunos pesados.
- Entrega del acceso **manual por WhatsApp**, no inmediata.
- El enlace de la app y de los PDF **no está protegido por usuario**.

### 4.6 Instrucciones de uso para una persona sin conocimientos técnicos
1. **Abrí el enlace** que te llegó por WhatsApp. Se abre en el navegador de tu celular (Chrome, Safari, etc.).
2. **Usá siempre el mismo celular y el mismo navegador.** Así tu avance queda guardado. Si tu celular lo permite, guardá el enlace en favoritos o en la pantalla de inicio para encontrarlo rápido.
3. En **Inicio** vas a ver tu avance y **"Tu próximo paso"**. Tocá **"Ir a mi camino"**.
4. En **Camino**, leé el paso del día, hacelo y **tocá el círculo** para marcarlo. Se tacha y tu avance sube.
5. Para leer las guías, entrá a **Biblioteca** y tocá **"Abrir guía"**. Se abre en Google Drive en otra pestaña. Para volver a la app, volvé a la pestaña anterior.
6. Si estás con la cabeza a mil, entrá a **Rescate** y tocá **"Empezar"** en la respiración: seguí el círculo (inhalá cuando crece, exhalá cuando se achica).
7. En **Mi plan**, escribí tus 3 tareas principales, 2 de apoyo y 1 microacción. **Se guarda solo.** Usá el temporizador de 25 minutos para concentrarte en una tarea; avisa con "¡Listo!" en pantalla (no suena).
8. Si un día no podés, **no pasa nada**: al volver seguís donde quedaste.
9. **No borres los datos del navegador** ni uses modo incógnito, o tu avance vuelve a cero.

---

## 5. Diferenciación frente a un PDF convencional

Lo que la app **hace** y un PDF suelto **no**:

| Función interactiva | En la app | En un PDF |
|---|---|---|
| Saber qué hacer hoy | "Tu próximo paso" se actualiza solo según lo que ya marcaste | Hay que buscar dónde quedaste |
| Registro de avance | Casillas, porcentaje, contador por etapa y barra de progreso | No registra nada |
| Programa ordenado | 28 pasos cortos en 4 etapas que conectan las 5 guías | Cada libro por separado |
| Retomar sin culpa | Al volver, el avance sigue ahí (mismo celular/navegador) | — |
| Respiración guiada | Círculo animado con ritmo 4‑2‑6 y cuenta regresiva de 2 minutos | Solo instrucciones escritas |
| Temporizador de enfoque | Contador de 25 minutos con pausa y reinicio | Hay que usar otra app |
| Planificador diario | Campos 3‑2‑1 que se guardan solos | Hay que imprimir o copiar a mano |
| Acceso rápido en crisis | Sección Rescate con plan de 4 pasos y 4 bonos a un toque | Hay que buscar el archivo |
| Todo en un lugar | 15 materiales organizados por tema desde una sola pantalla | Archivos sueltos |
| Lectura cómoda en el celular | Diseño para celular y modo oscuro automático | Depende del archivo |

**Cómo decirlo (sin prometer resultados):**
- ✅ "Es una app que te dice qué hacer cada día, te deja marcar tu avance y tiene herramientas como respiración guiada y temporizador, además de las 15 guías y bonos."
- ✅ "Está pensada para dar pasos chicos, de 5 a 15 minutos."
- ❌ No decir: "cura la ansiedad", "elimina la procrastinación", "resultados garantizados", "clínicamente probado", "reemplaza la terapia", "baja el cortisol". **El producto se define como material educativo que no reemplaza a un profesional.**

---

## 6. Preguntas frecuentes técnicas (respuestas verificadas)

**¿Qué es exactamente lo que compro?**
Una app web con un camino de 28 pasos, 5 guías y 10 bonos en PDF, una sección de Rescate (respiración de 2 minutos y plan para días caóticos) y Mi plan (planificador 3‑2‑1 y temporizador de 25 minutos).

**¿Tengo que descargar algo?**
No. Se abre desde el navegador del celular con el enlace que te mando.

**¿Está en Play Store o App Store?**
No. Es una app que funciona desde el navegador.

**¿Necesito crear usuario o contraseña?**
No. Abrís el enlace y ya la usás.

**¿Cómo recibo el acceso?**
Pagás por Mercado Pago, me mandás el comprobante por WhatsApp y te envío el enlace de la app.

**¿Funciona sin internet?**
No. Necesitás conexión para abrir la app y los materiales.

**¿Se guarda mi progreso?**
Sí, automáticamente, en el celular y navegador donde lo usás. Si cerrás y volvés a entrar, sigue ahí.

**¿Puedo usarlo en el celular y en la computadora?**
Podés abrirlo en los dos, pero el avance **no se comparte**: cada dispositivo guarda su propio progreso. Te recomiendo usar siempre el mismo.

**Cambié de celular / borré el historial y mi avance desapareció. ¿Lo recupero?**
No. El avance se guarda solo en ese navegador; no hay copia en ningún servidor. Podés volver a marcar los pasos que ya hiciste (se puede marcar en cualquier orden).

**¿Tengo que hacer un paso por día sí o sí?**
No. Es lo recomendado, pero podés ir a tu ritmo, hacer más de uno por día o pausar. No hay fechas ni penalizaciones.

**Si dejo varios días, ¿se reinicia?**
No. Retomás donde quedaste.

**¿Puedo saltear pasos o hacerlos en otro orden?**
Sí. Ningún paso está bloqueado. La app te sugiere el primero que tengas pendiente.

**¿Cuánto tiempo por día lleva?**
Cada paso está pensado para hacerse en 5 a 15 minutos.

**¿Las guías están dentro de la app?**
Se abren desde la app, pero están alojadas en Google Drive: al tocarlas se abren en otra pestaña. No necesitás cuenta de Google para verlas.

**¿Puedo descargar los PDF?**
Sí: se abren en Google Drive, donde podés usar la opción de descarga.

**Las guías tardan en abrir.**
Algunas son pesadas (hasta unos 100 MB). Te conviene abrirlas con wifi.

**¿Me manda recordatorios o notificaciones?**
No. La app no envía notificaciones.

**¿El temporizador suena al terminar?**
No. Al llegar a cero muestra "¡Listo!" en pantalla.

**¿La respiración tiene audio o voz?**
No. Es visual: un círculo que se agranda y se achica marcando inhalar 4, sostener 2 y exhalar 6 segundos, durante 2 minutos.

**¿Puedo escribir en la app?**
Sí, en Mi plan (3 tareas principales, 2 de apoyo y 1 microacción). Se guarda solo. Los ejercicios del camino que piden anotar se hacen en papel o en tus notas.

**¿Tiene modo oscuro?**
Sí. Se activa sola si tu celular está en modo oscuro.

**¿Es una suscripción?**
No. Es un pago único (según la página de venta).

**¿Reemplaza a un psicólogo o médico?**
No. Es material educativo para organizarte y cuidarte en el día a día. Si estás atravesando un momento muy difícil, buscá ayuda profesional.

**¿Funciona en iPhone?**
Está hecha para abrirse en cualquier navegador de celular. *(Pendiente de prueba en iPhone real: si la clienta tiene un problema, derivar a la dueña.)*

---

## 7. Datos confirmados, pendientes y decisiones comerciales

### 7.1 ✅ Confirmado (verificado en el código y en prueba funcional)
- App web de 5 pestañas: Inicio, Camino, Biblioteca, Rescate, Mi plan.
- Camino de 28 pasos (4 etapas × 7), etiquetas Día 1 a Día 28, avance libre, marcar y desmarcar.
- Indicadores de avance (porcentaje, X de 28, etapa actual, contador por etapa, barra) y "Tu próximo paso".
- Mensaje al completar los 28 pasos.
- Biblioteca de 15 PDF (5 guías + 10 bonos) en Google Drive; **los 15 enlaces funcionan** y están compartidos como "cualquiera con el enlace".
- Respiración visual de 2 minutos (4‑2‑6), con detener.
- Plan para día caótico (4 pasos) y 4 accesos de ayuda rápida.
- Planificador 3‑2‑1 con autoguardado.
- Temporizador de 25 minutos con empezar, pausar, seguir y reiniciar.
- Guardado en el navegador (pasos, plan, última pestaña); se mantiene al recargar; no se comparte entre navegadores o dispositivos.
- Modo oscuro automático; sin errores de JavaScript en la prueba.
- Sin cuenta, sin notificaciones, sin sonido, sin modo offline.
- Aviso de que es material educativo y no reemplaza a un profesional.
- Página de venta: precio **$20.000 ARS**, **pago único** con **Mercado Pago**, entrega del enlace **manual por WhatsApp**.

### 7.2 ⏳ Pendiente de prueba
- Apertura del enlace de la app (claude.ai) por una persona **sin cuenta de Claude**, en Android e iPhone reales.
- Funcionamiento en **Safari/iPhone** y en Android de gama baja.
- Comportamiento de los temporizadores con la **pantalla bloqueada** o en segundo plano.
- Posibilidad real de **"agregar a pantalla de inicio"** desde el enlace (lo promete la página de venta).
- Apertura de los PDF más pesados (Cortisol Detox, 103 MB) con datos móviles.
- Contenido y funcionamiento de **`leivajesica-mkt.systeme.io/acceso`**: no se pudo abrir en esta auditoría.
- Contenido interno de los 15 PDF (no se auditó).

### 7.3 🧭 Decisiones comerciales que debe definir la propietaria
1. **Enlace oficial de entrega:** ¿la compradora recibe el enlace de claude.ai o una página de systeme.io? Definir uno solo y confirmar que se abre sin cuenta.
2. **Precio vigente** y si hay promociones, cuotas o precio en otras monedas (la página dice $20.000 ARS).
3. **Medios de pago aceptados** además del enlace de Mercado Pago (transferencia, alias, etc.).
4. **Tiempo de entrega prometido** (hoy: "apenas veo tu mensaje"; de madrugada, "a primera hora") y horario de atención.
5. **Política de devolución o garantía**: la página de acceso **no menciona ninguna**. Definirla antes de que la agente responda sobre reembolsos.
6. **Duración del acceso**: la página dice "la app queda tuya" y "el acceso queda tuyo". Como es un enlace alojado, conviene definir qué se promete (acceso por tiempo indefinido mientras exista el enlace) y no usar palabras como "para siempre" sin respaldo.
7. **Protección del contenido**: hoy cualquiera con el enlace abre la app y los PDF. ¿Se acepta este riesgo o se quiere un acceso con usuario?
8. **Soporte**: canal y horario para problemas técnicos (por ejemplo "perdí mi avance", "no me abre el PDF").
9. **Reenvío del enlace** si la compradora lo pierde: ¿se reenvía sin costo? ¿Cómo se verifica que compró?
10. **Factura o comprobante** de compra: ¿se emite?
11. **Promesas de marketing**: alinear anuncios y carruseles con lo verificado aquí (sin notificaciones, sin audio, sin sincronización, sin resultados garantizados).
12. **Página de acceso privada**: el artifact "Ecosistema Anti‑Procrastinación · Acceso" figura como **privado** en claude.ai. Si se pensaba compartir ese enlace con clientas, hay que publicarlo; si se usa systeme.io, ignorar este punto.
13. **Datos de contacto** que la agente puede compartir (el WhatsApp de la página es +54 9 3496 46‑0829).

---

## Anexo · Reglas de comportamiento sugeridas para la agente
- Respondé solo con lo que figura en este documento. Si no está, decí que lo consultás y derivá.
- No prometas resultados de salud, productividad ni ingresos. No uses términos clínicos ("cura", "tratamiento", "terapia").
- Si una persona expresa una crisis o malestar intenso, no vendas: recomendá buscar ayuda profesional o comunicarse con la línea de salud mental de su país, y derivá a la dueña.
- Ante problemas técnicos (no abre, perdió el avance, no carga un PDF), usá las FAQ de la sección 6 y, si no se resuelve, derivá.
- No inventes precios, descuentos, garantías ni plazos: usá solo lo que la dueña confirme en la sección 7.3.
