import tkinter as tk
from tkinter import filedialog
from dotenv import load_dotenv, set_key
import os

class TelemetryGUI:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Telemetry BNG")

        load_dotenv()  # Load environment variables from .env file

        # Nombre
        tk.Label(root, text="Nombre").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=0, padx=5, pady=2, sticky="ew")
        self.nombre_entry.insert(0, os.getenv("NOMBRE", ""))
        self.nombre_entry.bind("<FocusOut>", self.update_env)

        # Identificación
        tk.Label(root, text="Identificación").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.identificacion_entry = tk.Entry(root)
        self.identificacion_entry.grid(row=3, column=0, padx=5, pady=2, sticky="ew")
        self.identificacion_entry.insert(0, os.getenv("IDENTIFICACION", ""))
        self.identificacion_entry.bind("<FocusOut>", self.update_env)

        # Empresa
        tk.Label(root, text="Empresa").grid(row=4, column=0, padx=5, pady=2, sticky="w")
        self.empresa_entry = tk.Entry(root)
        self.empresa_entry.grid(row=5, column=0, padx=5, pady=2, sticky="ew")
        self.empresa_entry.insert(0, os.getenv("EMPRESA", ""))
        self.empresa_entry.bind("<FocusOut>", self.update_env)

        # Path del VSL
        tk.Label(root, text="Path del VSL").grid(row=6, column=0, padx=5, pady=2, sticky="w")
        path_frame = tk.Frame(root)
        path_frame.grid(row=7, column=0, padx=5, pady=2, sticky="ew")
        self.path_entry = tk.Entry(path_frame)
        self.path_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.path_entry.insert(0, os.getenv("VSL_PATH", ""))
        self.path_entry.bind("<FocusOut>", self.update_env)
        self.path_button = tk.Button(path_frame, text="📁", command=self.select_path)
        self.path_button.pack(side="right")

        # Botones de control
        button_frame = tk.Frame(root)
        button_frame.grid(row=8, column=0, padx=5, pady=5, sticky="ew")
        self.start_button = tk.Button(button_frame, text="Iniciar Monitorizado", command=self.start_monitoring)
        self.start_button.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.stop_button = tk.Button(button_frame, text="Detener Monitorizado", command=self.stop_monitoring)
        self.stop_button.pack(side="right", fill="x", expand=True, padx=(5, 0))

        # Indicador de estado
        self.status_label = tk.Label(root, text="Estado: Detenido")
        self.status_label.grid(row=10, column=0, padx=5, pady=5, sticky="w")

    def select_path(self):
        path = filedialog.askdirectory()
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, path)
        self.update_env()

    def start_monitoring(self):
        self.status_label.config(text="Estado: Monitorizando")
        self.app.start_monitoring()

    def stop_monitoring(self):
        self.app.stop_monitoring()
        self.status_label.config(text="Estado: Detenido")

    def update_env(self, event=None):
        set_key(".env", "NOMBRE", self.nombre_entry.get())
        set_key(".env", "IDENTIFICACION", self.identificacion_entry.get())
        set_key(".env", "EMPRESA", self.empresa_entry.get())
        set_key(".env", "VSL_PATH", self.path_entry.get())
