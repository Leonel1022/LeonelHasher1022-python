import os
import hashlib

def get_md5_hash(file_path):
    """Calcula el hash MD5 de un archivo."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def rename_files_with_hash(folder_path):
    """Renombra los archivos en la carpeta especificada con su hash MD5 + extensión de archivo + 'Leonel1022'."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            md5_hash = get_md5_hash(file_path)
            new_filename = f"{md5_hash}-{file_extension}-Leonel1022" #se puede cambiar el leonel1022 por otro usuario
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")


# Construir la ruta de la carpeta utilizando el nombre de usuario
folder_path = fr'C:\Users\{user}\Desktop\rename'

# Ejecuta la función para renombrar los archivos
rename_files_with_hash(folder_path)
