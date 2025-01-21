import os

def create_main_file():
    base_name = "analitycs"
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

    while True:
        last_index += 1
        file_name = f"{base_name}_{last_index}"
        file_path = os.path.join(output_dir, file_name)

        # Code to create the file
        with open(file_path, 'w') as file:
            file.write("")

        break

create_main_file()  
