# Salva Vidas 3000

**Salva Vidas 3000** es una herramienta desarrollada como parte de mi Trabajo de Fin de Grado en Ingeniería Informática. Su objetivo es facilitar la conversión de archivos `.xlsx` a `.csv`, extrayendo columnas específicas y generando un archivo con formato adecuado para cargas masivas, especialmente en plataformas como RSA Archer.

## 📌 Funcionalidad

- Selecciona un archivo `.xlsx` desde una interfaz gráfica.
- Extrae automáticamente las columnas **A y C** del archivo.
- Procesa los valores (eliminando vacíos, separando por comas si es necesario).
- Genera un único registro en formato `.csv`, con todos los valores separados por punto y coma.
- Guarda el archivo resultante con codificación `utf-8-sig`.

## 🚀 Tecnologías utilizadas

- **Python 3.x**
- [pandas](https://pandas.pydata.org/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

## 💻 Requisitos

Instala las dependencias necesarias ejecutando:

```bash
pip install pandas openpyxl
No necesitas instalar tkinter si usas Python en Windows. En Linux/Mac puede requerir instalación manual.

▶️ Cómo usar
Ejecuta el script:
python3 SalvaVidas3000.py
Aparecerá una ventana donde podrás seleccionar el archivo .xlsx.
La herramienta extraerá la información, la procesará y te pedirá guardar el archivo .csv en algún lugar. 

🧪 Ejemplo de uso
Archivo de entrada:
Excel con datos en varias columnas.

Archivo de salida:
Un .csv con una única fila, valores separados por ;.

👩‍💻 Autora
Lucía Gutiérrez Cano
Trabajo de Fin de Grado – Ingeniería Informática
