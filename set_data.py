import os
from dotenv import load_dotenv
import pandas as pd

def load_data(file_paths):
    return [pd.read_csv(path) for path in file_paths]

load_dotenv()
BASE_PATH = os.getenv("VSL_PATH")

FILE_PATHS = {
    "general": os.path.join(BASE_PATH, "General.csv"),
    "wheels": os.path.join(BASE_PATH, "Wheels.csv"),
    "engine": os.path.join(BASE_PATH, "Engine.csv")
}

def get_data():
    file_paths = [FILE_PATHS["general"], FILE_PATHS["wheels"], FILE_PATHS["engine"]]
    general_data, wheels_data, engine_data = load_data(file_paths)

    plots = [
        {
            "data": general_data[["time", "throttle", "brake", "clutch"]],
            "data_json": general_data[["time", "throttle", "brake", "clutch"]].to_dict(orient="records"),
            "x": "time",
            "y": ["throttle", "brake", "clutch"],
            "title": "Pedales: Acelerador, Freno y Clutch",
            "labels": ["Acelerador", "Freno", "Clutch"],
            "markers": [".", "o", "x"]
        },
        {
            "data": general_data[["time", "velocity (m/s)"]],
            "data_json": general_data[["time", "velocity (m/s)"]].to_dict(orient="records"),
            "x": "time",
            "y": ["velocity (m/s)"],
            "title": "Velocidad del Vehículo (m/s)",
            "labels": ["Velocidad (m/s)"],
            "colors": ["orange"],
            "markers": ["o"]
        },
        {
            "data": general_data[["time", "rotation of the steering wheel"]],
            "data_json": general_data[["time", "rotation of the steering wheel"]].to_dict(orient="records"),
            "x": "time",
            "y": ["rotation of the steering wheel"],
            "title": "Rotación del Volante",
            "labels": ["Rotación del Volante"],
            "colors": ["green"],
            "markers": ["o"]
        },
        {
            "data": general_data[["time", "vehicle x-position", "vehicle y-position", "vehicle z-position"]],
            "data_json": general_data[["time", "vehicle x-position", "vehicle y-position", "vehicle z-position"]].to_dict(orient="records"),
            "x": "time",
            "y": ["vehicle x-position", "vehicle y-position", "vehicle z-position"],
            "title": "Posición del Vehículo (X, Y, Z)",
            "labels": ["Posición X", "Posición Y", "Posición Z"],
            "markers": ["", "", ""]
        },
        {
            "data": general_data[["vehicle x-position", "vehicle y-position"]],
            "data_json": general_data[["vehicle x-position", "vehicle y-position"]].to_dict(orient="records"),
            "x": "vehicle x-position",
            "y": ["vehicle y-position"],
            "title": "Posición del Vehículo (X, Y)",
            "labels": ["Posición X", "Posición Y"],
            "markers": ["o"],
            "colors": ["purple"]
        },
        {
            "data": wheels_data[["time", "average angular velocity of all wheels"]],
            "data_json": wheels_data[["time", "average angular velocity of all wheels"]].to_dict(orient="records"),
            "x": "time",
            "y": ["average angular velocity of all wheels"],
            "title": "Ruedas: Velocidad Angular Promedio",
            "labels": ["Velocidad Angular Promedio"],
            "colors": ["purple"],
            "markers": [""]
        },
        {
            "data": wheels_data[["time", "RR: brakeCoreTemperature", "RL: brakeCoreTemperature", "FR: brakeCoreTemperature", "FL: brakeCoreTemperature"]],
            "data_json": wheels_data[["time", "RR: brakeCoreTemperature", "RL: brakeCoreTemperature", "FR: brakeCoreTemperature", "FL: brakeCoreTemperature"]].to_dict(orient="records"),
            "x": "time",
            "y": ["RR: brakeCoreTemperature", "RL: brakeCoreTemperature", "FR: brakeCoreTemperature", "FL: brakeCoreTemperature"],
            "title": "Frenos: Temperaturas",
            "labels": ["Temperatura del núcleo del freno (RR)", "Temperatura del núcleo del freno (RL)", "Temperatura del núcleo del freno (FR)", "Temperatura del núcleo del freno (FL)"],
            "colors": ["red", "red", "blue", "blue"],
            "markers": ["o", "*", ".", ""]
        },
        {
            "data": engine_data[["time", "thermals: coolantTemperature", "thermals: oilTemperature", "thermals: exhaustTemperature"]],
            "data_json": engine_data[["time", "thermals: coolantTemperature", "thermals: oilTemperature", "thermals: exhaustTemperature"]].to_dict(orient="records"),
            "x": "time",
            "y": ["thermals: coolantTemperature", "thermals: oilTemperature", "thermals: exhaustTemperature"],
            "title": "Motor: Temperaturas",
            "labels": ["Temperatura del Refrigerante", "Temperatura del Aceite", "Temperatura del Escape"],
            "markers": ["", "", ""]
        }
    ]

    return plots