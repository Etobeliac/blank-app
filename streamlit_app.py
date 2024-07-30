import streamlit as st
import os

# Titre de l'application
st.title('Page d\'Accueil des Scripts')

# Liste des scripts Python dans le dossier 'scripts'
scripts_folder = 'scripts'
scripts = [f for f in os.listdir(scripts_folder) if f.endswith('.py')]

# Sidebar pour sélectionner un script
selected_script = st.sidebar.selectbox('Sélectionnez un script', scripts)

# Affichage du script sélectionné
if selected_script:
    st.header(f'Contenu de {selected_script}')
    script_path = os.path.join(scripts_folder, selected_script)
    with open(script_path, 'r') as file:
        script_content = file.read()
    st.code(script_content, language='python')

# Option pour exécuter le script sélectionné
if st.button('Exécuter le script'):
    exec(open(script_path).read())
    st.write('Le script a été exécuté.')
