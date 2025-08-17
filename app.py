
import streamlit as st
from data.utils import LANGS, get_lang, set_lang, t

st.set_page_config(page_title="Benew", page_icon="🌍", layout="wide")

cols = st.columns([1,3,3,3])
with cols[0]:
    st.markdown("### **Benew**")
with cols[-1]:
    lang = get_lang()
    labels = {code:label for code,label in LANGS}
    sel = st.selectbox(t("choose_lang"), options=[c for c,_ in LANGS], format_func=lambda c: labels[c], index=[c for c,_ in LANGS].index(lang))
    if sel != lang:
        set_lang(sel)
        st.rerun()

st.divider()
st.markdown(f"#### {t('app_title')}")

st.markdown(
    '''
    - 👉 Utilise le **menu de gauche** pour naviguer (Banque, Assurance, Santé, etc.).  
    - 🧠 Chaque page inclut un **questionnaire** avec recommandations.  
    - 🧮 Onglet **Outils** : simulateur de budget et crédit conso.  
    - 📲 Entièrement utilisable **depuis un téléphone**.
    '''
)
st.info("Astuce : sur Streamlit Cloud, ajoute l'app à l'écran d'accueil pour une expérience type app.")
