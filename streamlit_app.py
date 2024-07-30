import streamlit as st
import os
import importlib.util

# Fonction pour importer dynamiquement un module et exécuter une fonction
def run_script(script_path):
    try:
        st.write(f"Tentative d'exécution du script : {script_path}")
        spec = importlib.util.spec_from_file_location("module.name", script_path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        if hasattr(foo, 'main'):
            foo.main()
    except Exception as e:
        st.error(f"Erreur lors de l'exécution du script : {e}")

# Titre de l'application
st.title('Scripts de Pirates')
st.sidebar.header("Les scripts disponibles")

# Répertoire des scripts
scripts_dir = 'scripts'

# Vérifier si le répertoire existe
if not os.path.exists(scripts_dir):
    st.sidebar.error(f"Le répertoire '{scripts_dir}' n'existe pas. Veuillez le créer et ajouter des scripts.")
else:
    # Récupérer la liste des scripts
    scripts = [f for f in os.listdir(scripts_dir) if f.endswith('.py')]
    
    if scripts:
        selected_script = st.sidebar.radio('Sélectionnez un script', scripts)

        if st.sidebar.button('Exécuter le script'):
            st.write(f"Exécution du script {selected_script}...")
            script_path = os.path.join(scripts_dir, selected_script)
            run_script(script_path)
    else:
        st.sidebar.warning("Aucun script trouvé dans le répertoire 'scripts'.")

# Footer
st.sidebar.markdown("© 2024 | by PirateSEO")
