import streamlit as st

def main():
    st.title("Classification de noms de domaine")

    st.file_uploader("Déposez votre fichier Excel ici", type=["xlsx"])

    st.button("Classifier les domaines")

    st.success("Ceci est un message de succès")

if __name__ == "__main__":
    main()