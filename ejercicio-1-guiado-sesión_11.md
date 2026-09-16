```text?code_stdout&code_event_index=1
Traceback (most recent call last):
  File "<xbox-string>", line 61
    content = """# EJERCICIO 1 — GUIADO — SESIÓN 11
## Diseño de Interfaces Gráficas: Calculadora y Layouts

---

## 1. Propósito de la Actividad
El objetivo de esta sesión es diseñar e implementar una interfaz gráfica de usuario (GUI) funcional en Python utilizando la librería **Kivy**. El estudiante aplicará el uso combinado de contenedores de diagramación (`BoxLayout` y `GridLayout`), la gestión de eventos de interacción y las buenas prácticas de organización de código y repositorios en GitHub.

---

## 2. Requerimientos Técnicos y de Diseño

### 2.1. Arquitectura de la Interfaz (`Layouts`)
* **Contenedor Raíz (`root_layout`):** `BoxLayout` de orientación vertical (`orientation='vertical'`), con padding interno de `10px` y espaciado de `10px`.
* **Sección Superior (Visor y Controles):**
  * `BoxLayout` horizontal (`orientation='horizontal'`) con `size_hint_y=0.2` y `spacing=5`.
  * `TextInput` para el visor (`readonly=True`, `halign='right'`, `font_size=32`, `size_hint_x=0.75`).
  * `Button` de reinicio/limpiado (`C`) con `size_hint_x=0.25` y `font_size=24`.
* **Sección Inferior (Teclado):**
  * `GridLayout` configurado estrictamente en **4 columnas × 5 filas** (`cols=4`, `rows=5`, `size_hint_y=0.8`).
  * Matriz completa de 20 botones distribuidos funcionalmente:
    * **Fila 1:** `(`, `)`, `%`, `**`
    * **Fila 2:** `7`, `8`, `9`, `*`
    * **Fila 3:** `4`, `5`, `6`, `/`
    * **Fila 4:** `1`, `2`, `3`, `-`
    * **Fila 5:** `0`, `.`, `=`, `+`

### 2.2. Lógica de Negocio y Manejo de Eventos
* **Asignación de Eventos:** Uso del método `.bind(on_press=...)` asignado dinámicamente a cada botón para dirigir la interacción al método callback `on_button_press`.
* **Operaciones Aritméticas:** Evaluación dinámica de expresiones mediante evaluación controlada de cadenas de texto.
* **Control de Excepciones:** Captura de errores de sintaxis o división por cero, mostrando la etiqueta `"Error"` en el visor.
* **Comportamiento del Visor:** 
  * Al presionar `C`, restablecer el visor a `"0"`.
  * Si el estado actual es `"0"` o `"Error"`, la entrada de un nuevo número reemplaza el visor.

---
