import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd
import streamlit as st

def scrap_filtre_48h():
    st.title('Scraping de Domaines Expirés')
    url = 'https://member.expireddomains.net/domains/pendingdelete/?savedsearch_id=482709&ftlds[]=2&ftlds[]=3&ftlds[]=4&flimit=200&fdomainnot=kamagra+stromectol+pharmacy+levitra+cialis+outlet+viagra+sex+xanax+porn+nike+cheap+jersey+slot+casino&fenddays=1&fenddaysmax=2&fmseocf=8&fmseotf=8&fmseorefdomlive=21&fmseorefdomlivemax=99&o=adddate&r=d'

    st.write("Envoi de la requête à l'URL...")
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    domain_cells = soup.select('table.base1 > tbody > tr > td:nth-child(2)')

    domains = []
    for cell in domain_cells:
        domains.append(cell.text.strip())
        time.sleep(random.uniform(5, 20))

    df = pd.DataFrame(domains, columns=["Domain"])

    output_path = 'domains.xlsx'
    df.to_excel(output_path, index=False)

    st.write(f"Les domaines ont été sauvegardés dans le fichier {output_path}")
    st.dataframe(df)

if __name__ == "__main__":
    scrap_filtre_48h()
