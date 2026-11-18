# Instrucciones para Claude

## Caza de ofertas (Nexus Profit · skill cazador-de-ofertas)

- Antes de mostrar ofertas, leé `ofertas-vistas.md` y **no repitas** ninguna oferta (id) ni anunciante que ya figure ahí, salvo que el usuario lo pida.
- Si `descubrir_ofertas` devuelve repetidas, pedí un `limite` mayor (hasta 30) y saltealas.
- Al terminar cada informe, agregá al final de `ofertas-vistas.md` una fila por oferta mostrada (fecha, id, anunciante, producto, decisión) y hacé commit + push.
- Esta sesión en la nube **no puede escanear la Biblioteca de Meta**: Meta bloquea las IP de servidores (403). Para confirmar en Meta, el usuario tiene que correr la skill desde la app de escritorio de Claude con navegador. No lo intentes de nuevo desde la nube; avisá y seguí con los datos de Nexus.
