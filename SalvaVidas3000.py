"""
--------------------
| Salva Vidas 3000 |
--------------------
Desarrollado por: Lucía Gutiérrez Cano

"""

import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox


def convertidor3000():

    #seleccionar el archivo Excel
    archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])

    if not archivo:
        return  # Si no se selecciona un archivo, salir 
    
    # Si el archivo no es .xlsx muestra mensaje de error 
    if not archivo.endswith(".xlsx"):
        messagebox.showerror("Error", "Seleccione un archivo con extensión .xlsx")
        return
    
    try:
        #pandas se usa para leer el archivo. Tipo excel es con openpyxl y no tiene encabezados
        datos = pd.read_excel(archivo, engine="openpyxl", header=None)
        
        # Seleccionar solo las columnas A (0) y C (2) 
        datos = datos.iloc[:, [0, 2]]
        
        # dropna es un metodo de pandas para eliminar filas o columnas vacias
        datos = datos.dropna(how='all')
        
    
        lista_datos = []
        for _, fila in datos.iterrows(): #iterrows() en Pandas -> iterar sobre las filas de un DataFrame. 
            for valor in fila: 
                if pd.notna(valor):  
                    if isinstance(valor, str):
                        lista_datos.extend(valor.split(","))  #Como el valor es str agrega ese dato a la lista con ,
                    else:
                        lista_datos.append(str(valor))  #Si no es str lo convierte 
        
        # Crear un DataFrame con una sola fila y todas las columnas necesarias
        df_final = pd.DataFrame([lista_datos])
        
        # Cuadro de diálogo para guardar el archivo .csv
        guardar_como = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
        if guardar_como:
            # Guardar el DataFrame en formato .csv con separador de punto y coma
            df_final.to_csv(guardar_como, index=False, header=False, encoding="utf-8-sig", sep=";")
            messagebox.showinfo("Listo", "Archivo guardado correctamente")
            
    except Exception as e:
        # Mostrar un mensaje de error en caso de que ocurra un problema
        messagebox.showerror("Error", f"Ocurrió un problema: {str(e)}")


# Se usa Tkinter para crear interfaces gráficas de usuario (GUI) 
def lanzar_interfaz():
    ventana = tk.Tk()
    ventana.title("Salva Vidas 3000")
    ventana.geometry("320x150")

    tk.Label(ventana, text="Convertir archivo .xlsx a .csv", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana, text="Seleccionar archivo .xlsx", command=convertidor3000).pack(pady=20)

    ventana.mainloop()


if __name__ == "__main__":
    lanzar_interfaz()