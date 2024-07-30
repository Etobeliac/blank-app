import streamlit as st
import os
import importlib.util

# Fonction pour lire le contenu d'un fichier
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Fonction pour importer et exécuter dynamiquement un module
def run_script(script_path):
    spec = importlib.util.spec_from_file_location("module.name", script_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

# Titre de l'application
st.title('Scripts de Pirates')
st.sidebar.header("Les scripts")

# Répertoire des scripts
scripts_dir = 'scripts'

# Vérifier si le répertoire existe
if not os.path.exists(scripts_dir):
    st.sidebar.error(f"Le répertoire '{scripts_dir}' n'existe pas. Veuillez le créer et ajouter des scripts.")
else:
    st.sidebar.write(f"Le répertoire '{scripts_dir}' existe.")
    # Récupérer la liste des scripts
    scripts = [f for f in os.listdir(scripts_dir) if f.endswith('.py')]
    st.sidebar.write(f"Scripts trouvés : {scripts}")

    # Ajouter une sélection de script avec des boutons radio dans la barre latérale
    if scripts:
        selected_script = st.sidebar.radio('Sélectionnez un script', scripts)

        # Afficher le contenu du script sélectionné et ajouter un bouton pour l'exécuter
        if selected_script:
            script_path = os.path.join(scripts_dir, selected_script)
            script_content = read_file(script_path)
            
            st.subheader(f"Contenu du script : {selected_script}")
            st.code(script_content, language='python')

            if st.button('Exécuter le script'):
                st.write(f"Exécution du script {selected_script}...")
                run_script(script_path)
    else:
        st.sidebar.write("Aucun script trouvé dans le répertoire 'scripts'.")

# Footer
st.sidebar.markdown("© 2024 | by Etobeliac")
