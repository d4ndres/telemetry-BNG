import os
import matplotlib.pyplot as plt
import re

PLOT_CONFIG = {
    "figsize": (12, 6),
    "xlabel": "Tiempo (s)",
    "grid": True
}

def plot_and_save(pdf, data, x, y, title, xlabel=None, ylabel=None, labels=None, colors=None, markers=None):
    fontsize = 16
    xlabel = xlabel if xlabel else x
    plt.figure(figsize=(12, 6))
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
    pdf.savefig()
    plt.close()

def get_next_file_name(base_name, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    last_index = 0
    for file in os.listdir(output_dir):
        if file.startswith(base_name):
            index = int(file.split("_")[-1].split(".")[0])
            if index > last_index:
                last_index = index

    last_index += 1
    return os.path.join(output_dir, f"{base_name}_{last_index}.pdf")

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def save_plot_image(data, x, y, title, output_dir, xlabel=None, ylabel=None, labels=None, colors=None, markers=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    sanitized_title = sanitize_filename(title)
    image_path = os.path.join(output_dir, f"{sanitized_title}.png")
    fontsize = 16
    xlabel = xlabel if xlabel else x
    plt.figure(figsize=(12, 6))
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
    plt.savefig(image_path)
    plt.close()
    return image_path
