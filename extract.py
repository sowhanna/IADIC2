import os

# Fonction pour extraire les 7 caractéristiques de chaque exécutable
def extract_features(executable_path):
    # Exemple de caractéristiques extraites (vous pouvez les adapter à votre cas)
    features = {
        'name': os.path.basename(executable_path),
        'size': os.path.getsize(executable_path),
        'created': os.path.getctime(executable_path),
        'modified': os.path.getmtime(executable_path),
        'is_executable': os.access(executable_path, os.X_OK),
        'is_file': os.path.isfile(executable_path),
        'extension': os.path.splitext(executable_path)[1]
    }
    return features

# Fonction pour parcourir le répertoire et extraire les caractéristiques des exécutables
def script_extract(directory):
    executables = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.exe'):  # ou tout autre type d'exécutable
                file_path = os.path.join(root, file)
                features = extract_features(file_path)
                executables.append(features)
    return executables
