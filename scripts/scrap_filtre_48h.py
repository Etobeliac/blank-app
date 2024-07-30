import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd
import streamlit as st
from datetime import datetime

def scrap_filtre_48h():
    st.title('Scraping de Domaines Expirés')
    
    url = 'https://member.expireddomains.net/domains/pendingdelete/?savedsearch_id=482709&ftlds[]=2&ftlds[]=3&ftlds[]=4&flimit=200&fdomainnot=kamagra+stromectol+pharmacy+levitra+cialis+outlet+viagra+sex+xanax+porn+nike+cheap+jersey+slot+casino&fenddays=1&fenddaysmax=2&fmseocf=8&fmseotf=8&fmseorefdomlive=21&fmseorefdomlivemax=99&o=adddate&r=d'
    
    if st.button('Lancer le scraping'):
        st.write("Envoi de la requête à l'URL...")
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        domain_cells = soup.select('table.base1 > tbody > tr > td:nth-child(2)')

        domains = []
        total_domains = len(domain_cells)
        progress_text = "Scraping en cours. Veuillez patienter..."
        my_bar = st.progress(0)
        
        for i, cell in enumerate(domain_cells):
            domains.append(cell.text.strip())
            # Ajouter un délai aléatoire entre 5 et 20 secondes
            time_to_wait = random.uniform(5, 20)
            st.text(f"Attente de {time_to_wait:.2f} secondes...")
            time.sleep(time_to_wait)
            # Mettre à jour la barre de progression
            my_bar.progress((i + 1) / total_domains)
        
        # Créer un DataFrame pandas
        df = pd.DataFrame(domains, columns=["Domain"])
        df['FILTRE 48H'] = 'FILTRE 48H'

        # Nommer le fichier avec la date du jour
        date_str = datetime.now().strftime("%Y-%m-%d")
        output_path = f'domains_{date_str}.xlsx'
        df.to_excel(output_path, index=False)

        st.write(f"Les domaines ont été sauvegardés dans le fichier {output_path}")
        st.dataframe(df)

        # Permettre le téléchargement du fichier
        def convert_df(df):
            # IMPORTANT: Convertir le dataframe en CSV pour le téléchargement.
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Télécharger le fichier",
            data=csv,
            file_name=f'domains_{date_str}.csv',
            mime='text/csv',
        )

if __name__ == "__main__":
    scrap_filtre_48h()
