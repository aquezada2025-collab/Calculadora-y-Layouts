
# EJERCICIO 1 — GUIADO — SESIÓN 11
## Diseño de Interfaces Gráficas: Calculadora y Layouts

---

## 1. Propósito de la Actividad
El objetivo de esta sesión es diseñar e implementar una interfaz gráfica de usuario (GUI) funcional en Python utilizando la librería **Kivy**. El estudiante aplicará el uso combinado de contenedores de diagramación (`BoxLayout` y `GridLayout`), la gestión de eventos de interacción y las buenas prácticas de organización de código y repositorios en GitHub.

---

## 2. Requerimientos Técnicos y de Diseño

### 2.1. Arquitectura de la Interfaz (`Layouts`)
* **Contenedor Raíz (`root_layout`):** `BoxLayout` de orientación vertical (`orientation='vertical'`), con padding de `10px` y espaciado de `10px`.
* **Sección Superior (Visor y Control):**
  * `BoxLayout` horizontal (`orientation='horizontal'`) con `size_hint_y=0.2` y `spacing=5`.
  * `TextInput` para el visor (`text="0"`, `readonly=True`, `halign="right"`, `font_size=32`, `size_hint_x=0.75`).
  * `Button` de limpiado **`C`** con `size_hint_x=0.25` y `font_size=24`.
* **Sección Inferior (Teclado):**
  * `GridLayout` de **4 columnas × 4 filas** (`cols=4`, `rows=4`, `size_hint_y=0.8`).
  * Distribución exacta de los 16 botones en la cuadrícula (17 botones en total contando el botón `C` superior):
    * **Fila 1:** `7`, `8`, `9`, `*`
    * **Fila 2:** `4`, `5`, `6`, `/`
    * **Fila 3:** `1`, `2`, `3`, `-`
    * **Fila 4:** `0`, `.`, `=`, `+`

### 2.2. Lógica de Negocio y Manejo de Eventos
* **Enlace de Eventos:** Uso del método `.bind(on_press=self.on_button_press)` asignado dinámicamente a cada botón.
* **Procesamiento de Expresiones:** Manejo dinámico de caracteres y cálculo final con `eval()` al presionar `=`.
* **Manejo de Errores:** Bloque `try-except` para capturar errores de sintaxis o división por cero, mostrando la palabra `"Error"` en el visor.
* **Comportamiento del Visor:**
  * Al pulsar `C`, la pantalla vuelve a `"0"`.
  * Si el visor muestra `"0"`, la pulsación de un nuevo dígito reemplaza el cero inicial.

---
