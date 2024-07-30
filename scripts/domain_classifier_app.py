import streamlit as st
import pandas as pd
import io
from io import BytesIO
import langdetect

def detect_language(text):
    try:
        return langdetect.detect(text)
    except:
        return 'unknown'

def classify_domain(domain, categories):
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in domain.lower():
                return category
    return 'NON CLASSÉ'

def main():
    st.title("Classification de noms de domaine")

    uploaded_file = st.file_uploader("Déposez votre fichier Excel ici", type=["xlsx"])

    if uploaded_file is not None:
        df_input = pd.read_excel(uploaded_file)

        thematique_dict = {
            'ANIMAUX': ['animal', 'pet', 'zoo', 'farm', 'deer', 'chiens', 'chats', 'animaux'],
            'CUISINE': ['cook', 'recipe', 'cuisine', 'food', 'bon plan', 'equipement', 'minceur', 'produit', 'restaurant'],
            'ENTREPRISE': ['business', 'enterprise', 'company', 'corporate', 'formation', 'juridique', 'management', 'marketing', 'services'],
            'FINANCE / IMMOBILIER': ['finance', 'realestate', 'investment', 'property', 'assurance', 'banque', 'credits', 'immobilier'],
            'INFORMATIQUE': ['tech', 'computer', 'software', 'IT', 'high tech', 'internet', 'jeux-video', 'marketing', 'materiel', 'smartphones'],
            'MAISON': ['home', 'house', 'garden', 'interior', 'deco', 'demenagement', 'equipement', 'immo', 'jardin', 'maison', 'piscine', 'travaux'],
            'MODE / FEMME': ['fashion', 'beauty', 'cosmetics', 'woman', 'beaute', 'bien-etre', 'lifestyle', 'mode', 'shopping'],
            'SANTE': ['health', 'fitness', 'wellness', 'medical', 'hospital', 'grossesse', 'maladie', 'minceur', 'professionnels', 'sante', 'seniors'],
            'SPORT': ['sport', 'fitness', 'football', 'soccer', 'basketball', 'tennis', 'autre sport', 'basket', 'combat', 'foot', 'musculation', 'velo'],
            'TOURISME': ['travel', 'tourism', 'holiday', 'vacation', 'bon plan', 'camping', 'croisiere', 'location', 'tourisme', 'vacance', 'voyage'],
            'VEHICULE': ['vehicle', 'car', 'auto', 'bike', 'bicycle', 'moto', 'produits', 'securite', 'voiture']
        }

        domaines = df_input.iloc[:, 0].tolist()

        progress_bar = st.progress(0)
        status_text = st.empty()

        classified_domains = []
        unclassified_domains = []

        for i, domain in enumerate(domaines):
            category = classify_domain(domain, thematique_dict)
            language = detect_language(domain)
            
            if category != 'NON CLASSÉ':
                classified_domains.append((domain, category, language))
            else:
                unclassified_domains.append(domain)
            
            progress = (i + 1) / len(domaines)
            progress_bar.progress(progress)
            status_text.text(f"{i+1}/{len(domaines)} domaines traités")

        # Créer un DataFrame pour les domaines classifiés
        df_classified = pd.DataFrame(classified_domains, columns=['Domain', 'Category', 'Language'])
        
        # Créer un DataFrame pour les domaines non classifiés
        df_unclassified = pd.DataFrame(unclassified_domains, columns=['Unclassified Domain'])

        # Créer le DataFrame final
        max_rows = max(len(df_classified), len(df_unclassified))
        df_final = pd.DataFrame({
            'Domain': df_classified['Domain'].reindex(range(max_rows)),
            'Category': df_classified['Category'].reindex(range(max_rows)),
            'Language': df_classified['Language'].reindex(range(max_rows)),
            'Unclassified Domain': df_unclassified['Unclassified Domain'].reindex(range(max_rows))
        })

        # Réorganiser les colonnes pour avoir la colonne 'Unclassified Domain' en colonne E
        df_final = df_final[['Domain', 'Category', 'Language', 'Unclassified Domain']]
        df_final.columns = ['A', 'B', 'C', 'E']  # Renommer les colonnes

        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_final.to_excel(writer, index=False)
        
        st.download_button(
            label="Télécharger le fichier Excel",
            data=output.getvalue(),
            file_name="domaines_classes.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        st.success("Classification terminée. Vous pouvez maintenant télécharger le fichier.")

if __name__ == "__main__":
    main()