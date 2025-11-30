"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    years = list(range(2001, 2011))
    tv = [74, 76, 75, 72, 70, 69, 70, 68, 68, 66]
    newspaper = [45, 43, 48, 46, 40, 35, 34, 34, 30, 31]
    radio = [18, 20, 17, 18, 16, 15, 14, 13, 16, 16]
    internet = [13, 14, 17, 20, 18, 20, 22, 22, 40, 41]

    plt.figure(figsize=(8, 6))

    plt.plot(years, tv, label="Televisión", color="black")
    plt.plot(years, newspaper, label="Periódico", color="gray")
    plt.plot(years, radio, label="Radio", color="lightgray")
    plt.plot(years, internet, label="Internet", color="dodgerblue", marker='o')

    plt.text(2010, tv[-1], f"{tv[-1]}%", va='center', ha='left', color="black")
    plt.text(2010, newspaper[-1], f"{newspaper[-1]}%", va='center', ha='left', color="gray")
    plt.text(2010, radio[-1], f"{radio[-1]}%", va='center', ha='left', color="lightgray")
    plt.text(2010, internet[-1], f"{internet[-1]}%", va='center', ha='left', color="dodgerblue")

    plt.text(2001, tv[0], f"Televisión {tv[0]}%", va='center', ha='right', color="black")
    plt.text(2001, newspaper[0], f"Periódico {newspaper[0]}%", va='center', ha='right', color="gray")
    plt.text(2001, radio[0], f"Radio {radio[0]}%", va='center', ha='right', color="lightgray")
    plt.text(2001, internet[0], f"Internet {internet[0]}%", va='center', ha='right', color="dodgerblue")

    plt.title("Cómo la gente obtiene sus noticias", fontsize=14, weight='bold')
    plt.suptitle("Una proporción creciente cita Internet como su fuente principal de noticias", y=0.91, fontsize=10)

    plt.xticks(years)
    plt.yticks([])
    plt.box(False)

    os.makedirs("files/plots", exist_ok=True)

    plt.savefig("files/plots/news.png", bbox_inches="tight")
    plt.close()