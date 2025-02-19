import matplotlib.pyplot as plt
import numpy as np


def run():
  # Datos de ejemplo
  categorias = [
      "Atención a los espejos", "Ubicación espacial", "Concentración", 
      "Toma de decisiones rápidas", "Memoria a corto plazo", 
      "Coordinación ojo mano pie", "Paciencia", "Control emocional"
  ]
  buenas = np.random.randint(1, 10, size=len(categorias))  # Características buenas aleatorias
  malas = -np.random.randint(1, 10, size=len(categorias))  # Características malas aleatorias

  x = np.arange(len(categorias))  # Posiciones en el eje X
  width = 0.3  # Ancho de las barras

  fig, ax = plt.subplots(figsize=(18, 9))  # Tamaño de la figura 18:9

  # Dibujar la línea central
  ax.axhline(0, color='black', linewidth=1)

  # Graficar las barras hacia arriba y hacia abajo
  ax.bar(x , buenas, width=width, color='skyblue', label="Buenas")
  ax.bar(x , malas, width=width, color='salmon', label="Malas")

  # Etiquetas y formato
  def split_label(label, max_length=20):
      words = label.split()
      new_label = ""
      current_length = 0
      for word in words:
          if current_length + len(word) > max_length:
              new_label += "\n"
              current_length = 0
          new_label += word + " "
          current_length += len(word) + 1
      return new_label.strip()

  ax.set_xticks(x)
  ax.set_xticklabels([split_label(label) for label in categorias])
  ax.set_ylabel("Cantidad de características")
  ax.set_title("Características Buenas y Malas por Categoría")
  ax.legend()

  # Establecer límites fijos para los ejes
  ax.set_ylim(-10, 10)

  # Guardar el plot como imagen
  plt.savefig('./templates/habilidades_bar.png')
  plt.close()