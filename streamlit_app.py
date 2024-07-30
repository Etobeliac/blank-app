import streamlit as st
import os

# Fonction pour lire le contenu d'un fichier
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Titre de l'application
st.title('Scripts Python')
st.sidebar.header("Les scripts")

# Répertoire des scripts
scripts_dir = 'scripts'

# Vérifier si le répertoire existe
if not os.path.exists(scripts_dir):
    st.sidebar.error(f"Le répertoire '{scripts_dir}' n'existe pas. Veuillez le créer et ajouter des scripts.")
else:
    # Récupérer la liste des scripts
    scripts = [f for f in os.listdir(scripts_dir) if f.endswith('.py')]

    # Ajouter une sélection de script avec des boutons radio dans la barre latérale
    selected_script = st.sidebar.radio('Sélectionnez un script', scripts)

    # Afficher le contenu du script sélectionné
    if selected_script:
        script_path = os.path.join(scripts_dir, selected_script)
        script_content = read_file(script_path)
        
        # Afficher le contenu du script sélectionné
        st.subheader(f"Contenu du script : {selected_script}")
        st.code(script_content, language='python')

# Footer
st.sidebar.markdown("© 2024 | by Etobeliac")
