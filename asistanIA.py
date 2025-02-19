import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env_key
load_dotenv(dotenv_path='.env_key')
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def analyze_data_with_openai(value):
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": """
                    Ese un experto analítico de datos, puedes analisar los datos compartidos en formato JSON.
                    Siempre vas a dar la respuesta directa, sin explicar de donde vienen los datos o que hiciste.
                    puedes responder en un maximo de 500 caracteres.
                    """
                },
                {
                    "role": "user", 
                    "content": f"{value}"
                }
        ]
    )
    return response.choices[0].message.content


def analyze_plot(data, x, y):
    # crea una nueva data solo con los valores de x y y
    new_data = data[[x] + y]

    # convierte la data a un formato que analyze_data_with_openai pueda entender
    value = new_data.to_string(index=False)

    # llama a la función analyze_data_with_openai para obtener la respuesta
    response = analyze_data_with_openai(value)

    return response




