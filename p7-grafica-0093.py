import matplotlib.pyplot as plt
import numpy as np
# Pedro Martinez 0093
# Datos: x representa el número de lista del alumno, y1 y y2 las calificaciones por año
no_lista = [1, 2, 3, 17, 48]
califa_ML = [20, 30, 80, 100, 90]
califa_VA = [70, 90, 60, 90, 100]

# Graficar los datos
plt.plot(no_lista, califa_ML, label="Califas_ML NC.0093")
plt.plot(no_lista, califa_VA, label="Califas_VA NC.0093")


# Títulos y etiquetas ajustados
plt.title("Calificaciones materias 0093")
plt.xlabel("Número de Lista NC.0093")
plt.ylabel("Calificación NC.0093")

plt.legend() #
plt.show()