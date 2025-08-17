
import streamlit as st
from data.utils import render_section, t

st.sidebar.title("Benew")
st.sidebar.page_link("app.py", label=t("menu_home"))
st.sidebar.page_link("pages/1_Banking.py", label=t("menu_banking"))
st.sidebar.page_link("pages/2_Insurance.py", label=t("menu_insurance"))
st.sidebar.page_link("pages/3_Healthcare.py", label=t("menu_healthcare"))
st.sidebar.page_link("pages/4_Taxation.py", label=t("menu_taxation"))
st.sidebar.page_link("pages/5_Housing.py", label=t("menu_housing"))
st.sidebar.page_link("pages/6_Transport.py", label=t("menu_transport"))
st.sidebar.page_link("pages/7_Work.py", label=t("menu_work"))
st.sidebar.page_link("pages/8_Life.py", label=t("menu_life"))
st.sidebar.page_link("pages/9_Tools.py", label=t("menu_tools"))

render_section("life")
st.subheader(t("quiz"))
with st.form("life_quiz"):
    mobile = st.selectbox("Opérateur mobile préféré", ["Peu importe","Orange","Free","SFR","Bouygues"])
    fiber = st.radio("Avez-vous besoin d'internet fixe ?", ["Oui","Non"], horizontal=True)
    submitted = st.form_submit_button(t("see_rec"))
if submitted:
    steps = ["Acheter une carte SIM (sans engagement).","Ouvrir un compte bancaire.","Souscrire assurance habitation si location."]
    if fiber == "Oui":
        steps.append("Tester l'éligibilité fibre et souscrire une box (Orange/Free/SFR/Bouygues).")
    st.success(" • ".join(steps))
