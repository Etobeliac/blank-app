import streamlit as st
import os

# Fonction pour lire le contenu d'un fichier
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Titre de l'application
st.title('My Script Viewer App')

# Récupérer la liste des scripts
scripts_dir = 'scripts'
scripts = [f for f in os.listdir(scripts_dir) if f.endswith('.py')]

# Ajouter une sélection de script dans la barre latérale
selected_script = st.sidebar.selectbox('Sélectionnez un script', scripts)

# Afficher le contenu du script sélectionné
if selected_script:
    script_path = os.path.join(scripts_dir, selected_script)
    script_content = read_file(script_path)
    
    # Utiliser un expander pour le code source
    with st.expander("Code source du script sélectionné"):
        st.code(script_content, language='python')
