import os
from datetime import datetime
from pylatex import Document, Section, Subsection, Command, Figure
from pylatex.utils import NoEscape
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def create_latex_document(plots, pdf_file_path):
    nombre = os.getenv('NOMBRE')
    identificacion = os.getenv('IDENTIFICACION')
    empresa = os.getenv('EMPRESA')
    fecha = datetime.now().strftime('%d/%m/%Y')

    doc = Document(documentclass='article', document_options=['a4paper', '12pt'])
    doc.preamble.append(Command('title', 'Reporte de Análisis del Vehículo'))
    doc.preamble.append(Command('author', 'Generado automáticamente con Python'))
    doc.preamble.append(Command('date', fecha))
    doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
    doc.preamble.append(NoEscape(r'\usepackage{float}'))
    doc.preamble.append(NoEscape(r'\usepackage{fancyhdr}'))
    doc.preamble.append(NoEscape(r'\pagestyle{fancy}'))
    doc.preamble.append(NoEscape(r'\fancyhead[L]{Reporte de Análisis del Vehículo}'))
    doc.preamble.append(NoEscape(r'\fancyhead[R]{\leftmark}'))
    doc.preamble.append(NoEscape(r'\fancyfoot[C]{\thepage}'))
    doc.append(NoEscape(r'\maketitle'))

    with doc.create(Section('Introducción')):
        doc.append('Este documento contiene un análisis detallado de los datos del vehículo.')
        doc.append(NoEscape(r'\newline'))
        doc.append(f'Nombre: {nombre}')
        doc.append(NoEscape(r'\newline'))
        doc.append(f'Identificación: {identificacion}')
        doc.append(NoEscape(r'\newline'))
        doc.append(f'Empresa: {empresa}')
        doc.append(NoEscape(r'\newline'))
        doc.append(f'Fecha de generación del reporte: {fecha}')

    for i, plot in enumerate(plots):
        with doc.create(Section(plot['title'])):
            with doc.create(Figure(position='H')) as plot_fig:
                plot_fig.append(NoEscape(r'\centering'))
                plot_fig.append(NoEscape(r'\includegraphics[width=1\textwidth,page=%d]{%s}' % (i+1, os.path.basename(pdf_file_path))))
                plot_fig.add_caption(f'Gráfico de {plot["title"]}')

    latex_file_path = os.path.join(os.path.dirname(pdf_file_path), "vehicle_analysis_report")
    doc.generate_tex(latex_file_path)
    print(f"Archivo LaTeX generado: {latex_file_path}")
