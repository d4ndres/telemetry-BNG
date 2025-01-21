from data_loader import load_data
from plot_utils import plot_and_save, get_next_file_name
from matplotlib.backends.backend_pdf import PdfPages

FILE_PATHS = {
    "general": "./VSL_Demo/General.csv",
    "wheels": "./VSL_Demo/Wheels.csv",
    "engine": "./VSL_Demo/Engine.csv"
}

def create_main_file():
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
                {
            "data": general_data,
            "x": "time",
            "y": ["rotation of the steering wheel"],
            "title": "Rotación del Volante",
            "labels": ["Rotación del Volante"],
            "colors": ["green"],
            "markers": ["o"]
        },
        {
            "data": general_data,
            "x": "time",
            "y": ["vehicle x-position", "vehicle y-position", "vehicle z-position"],
            "title": "Posición del Vehículo (X, Y, Z)",
            "labels": ["Posición X", "Posición Y", "Posición Z"],
            "markers": ["", "", ""]
        },
        {
            "data": wheels_data,
            "x": "time",
            "y": ["average angular velocity of all wheels"],
            "title": "Ruedas: Velocidad Angular Promedio",
            "labels": ["Velocidad Angular Promedio"],
            "colors": ["purple"],
            "markers": [""]
        },
        {
            "data": wheels_data,
            "x": "time",
            "y": ["RR: brakeCoreTemperature", "RL: brakeCoreTemperature", "FR: brakeCoreTemperature", "FL: brakeCoreTemperature"],
            "title": "Frenos: Temperaturas",
            "labels": ["Temperatura del núcleo del freno (RR)", "Temperatura del núcleo del freno (RL)", "Temperatura del núcleo del freno (FR)", "Temperatura del núcleo del freno (FL)"],
            "colors": ["red", "red", "blue", "blue"],
            "markers": ["o", "*", ".", ""]
        },
        {
            "data": engine_data,
            "x": "time",
            "y": ["thermals: coolantTemperature", "thermals: oilTemperature", "thermals: exhaustTemperature"],
            "title": "Motor: Temperaturas",
            "labels": ["Temperatura del Refrigerante", "Temperatura del Aceite", "Temperatura del Escape"],
            "markers": ["", "", ""]
        }
    ]

    file_path = get_next_file_name("vehicle_analysis", "output")
    with PdfPages(file_path) as pdf:
        for plot in plots:
            plot_and_save(pdf, **plot)

    print(f"Archivo PDF generado: {file_path}")

if __name__ == "__main__":
    create_main_file()
