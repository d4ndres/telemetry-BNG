from set_data import get_data
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from plot_utils import save_plot_image
import os
import re
from datetime import datetime
from matplotlib import pyplot as plt
from create_habilidades_bar import run as create_bars
from asistanIA import analyze_data_with_openai

TEMPLATES_DIR = "./templates"
OUTPUT_PDF_DIR = "./output_pdf"

def sanitize_title(title):
    """Sanitize the plot title to create a valid filename."""
    return re.sub(r'[^\w\s]', '', title).replace(' ', '_')

def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_new_session_dir(base_dir):
    """Get a new session directory based on the highest existing number."""
    last_dir = max([int(d) for d in os.listdir(base_dir) if os.path.isdir(f"{base_dir}/{d}")], default=0)
    new_dir = last_dir + 1
    new_session_dir = f"{base_dir}/{new_dir}"
    create_directory(new_session_dir)
    return new_session_dir

def generate_plot(plot, output_path):
    """Generate and save a plot based on the provided data."""
    fontsize = 16
    y = plot['y']
    data = plot['data']
    x = plot['x']
    labels = plot['labels']
    colors = plot.get('colors')
    markers = plot['markers']
    title = plot['title']
    xlabel = plot.get('xlabel', x)
    ylabel = plot.get('ylabel', title)

    for i, y_col in enumerate(y):
        plt.plot(data[x], data[y_col], 
                 label=labels[i] if labels else y_col, 
                 color=colors[i] if colors else None, 
                 marker=markers[i] if markers else None)

    plt.title(title)
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel if ylabel else f"f({xlabel})", fontsize=fontsize)
    plt.legend()
    plt.grid(True)
    plt.savefig(output_path)
    plt.close()

def static():
    """Main function to generate static analysis report."""
    create_bars()

    # Obtiene la data inicial
    plots = get_data()

    # Lee las variables de entorno
    nombre = os.getenv('NOMBRE')
    identificacion = os.getenv('IDENTIFICACION')
    empresa = os.getenv('EMPRESA')
    fecha = datetime.now().strftime('%d/%m/%Y')

    user_template_dir = f"{TEMPLATES_DIR}/user/{identificacion}"
    create_directory(user_template_dir)
    new_session_dir = get_new_session_dir(user_template_dir)

    # Agrega propiedades a los plots y genera las imágenes
    for plot in plots:
        plot['sanitized_title'] = sanitize_title(plot['title'])
        plot['image_path'] = f"{new_session_dir}/{plot['sanitized_title']}.png"
        plot['description'] = analyze_data_with_openai(plot.get('data_json'))
        # plot['description'] = 'Super descriptcion '
        generate_plot(plot, plot['image_path'])

    # Load the Jinja2 template
    env_jinja = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template_html = env_jinja.get_template('template_5.html')
    html_out = template_html.render(
        data=plots, 
        nombre=nombre, 
        identificacion=identificacion, 
        empresa=empresa, 
        fecha=fecha,
        sesion=os.path.basename(new_session_dir))

    css = '''
    @page {
        margin: 0;
    }
    body {
        margin: 0;
        padding: 0;
    }
    '''

    user_output_dir = f"{OUTPUT_PDF_DIR}/user/{identificacion}"
    create_directory(user_output_dir)
    output_dir = get_new_session_dir(user_output_dir)

    # Crea el archivo PDF
    HTML(string=html_out, base_url='.').write_pdf(f'{output_dir}/{nombre}_{os.path.basename(new_session_dir)}.pdf', stylesheets=[CSS(string=css)])

if __name__ == "__main__":
    static()