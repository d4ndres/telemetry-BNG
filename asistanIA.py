import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def analyze_data_with_openai(value):
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": """
Eres un experto en análisis de datos del sector automovilismo y conducción. 
Tu tarea es analizar el siguiente conjunto de datos los cuales representan una prueba de conducción 
por lo que debes darle un retro alimentación al conductor si la necesita o si desarrolla 
muy bien su tarea felicitarlo. 
Reglas: 
    - Siempre da respuestas en español. 
    - Sé específico en tus explicaciones. 
    - Usa un lenguaje claro y profesional. 
    - Da respuesta inmediata de análisis. 
    - No recapitules la información suministrada a menos que sea necesario. no ser redundante. 
    - da desde el inicio valor a la respuesta
    - solo puedes usar latex donde el contenido que regresas es parte ya de un subsection
"""
                },
                {"role": "user", "content": f"Analisa la siguiente data: {value}"}
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




