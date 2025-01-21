import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def load_data(file_paths):
    return [pd.read_csv(path) for path in file_paths]

def plot_and_save(pdf, data, x, y, title, xlabel=None, ylabel=None, labels=None, colors=None, markers=None):
    xlabel = xlabel if xlabel else x
    plt.figure(figsize=(12, 6))
    for i, y_col in enumerate(y):
        plt.plot(data[x], data[y_col], 
                 label=labels[i] if labels else y_col, 
                 color=colors[i] if colors else None, 
                 marker=markers[i] if markers else None)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel if ylabel else f"f({xlabel})")
    plt.legend()
    plt.grid(True)
    pdf.savefig()
    plt.close()


PLOT_CONFIG = {
    "figsize": (12, 6),
    "xlabel": "Tiempo (s)",
    "grid": True
}







def create_main_file():
    base_name = "vehicle_analysis"

    output_dir = "output"
    last_index = 0

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # encuentra el ultimo archivo creado
    for file in os.listdir(output_dir):
        if file.startswith(base_name):
            index = int(file.split("_")[-1].split(".")[0])
            if last_index is None or index > last_index:
                last_index = index


    last_index += 1
    file_name = f"{base_name}_{last_index}.pdf"
    file_path = os.path.join(output_dir, file_name)

    # Code to create the file
    FILE_PATHS = {
        "general": "./VSL_Demo/General.csv",
        "wheels": "./VSL_Demo/Wheels.csv",
        "engine": "./VSL_Demo/Engine.csv"
    }

    file_paths = [FILE_PATHS["general"], FILE_PATHS["wheels"], FILE_PATHS["engine"]]
    general_data, wheels_data, engine_data = load_data(file_paths)

    plots = [
        {
            "data": general_data, 
            "x": "time", 
            "y": ["throttle", "brake", "clutch"], 
            "title": "Pedales: Acelerador, Freno y Clutch", 
            "labels": ["Acelerador", "Freno", "Clutch"], 
            "markers": [".", "o", "x"]
        },
        {
            "data": general_data, 
            "x": "time", 
            "y": ["velocity (m/s)"], 
            "title": "Velocidad del Vehículo (m/s)", 
            "labels": ["Velocidad (m/s)"], 
            "colors": ["orange"], 
            "markers": ["o"]
        },
    ]


    with PdfPages(file_path) as pdf:
        for plot in plots:
            plot_and_save(pdf, **plot)

    print(f"Archivo PDF generado: {file_path}")

create_main_file()  
