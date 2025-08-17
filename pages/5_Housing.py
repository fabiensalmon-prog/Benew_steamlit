
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

render_section("housing")
st.subheader(t("quiz"))
with st.form("house_quiz"):
    budget = st.number_input("Budget loyer (€/mois)", min_value=0, value=800, step=50)
    garant = st.radio("Avez-vous un garant en France ?", ["Oui","Non"], horizontal=True)
    duration = st.radio("Durée de séjour prévue ?", ["Court (<6 mois)","Long (≥6 mois)"], horizontal=True)
    submitted = st.form_submit_button(t("see_rec"))
if submitted:
    out = []
    if garant == "Non": out.append("Solutions sans garant : Studapart, Garantme, Visale.")
    if budget < 700: out.append("Ciblez colocation & résidences étudiantes (CROUS).")
    if "Court" in duration: out.append("Baux mobilités meublés (1–10 mois) ou résidences temporaires.")
    out.append("Comparer : Leboncoin, SeLoger. Prévoir dossier complet (papiers, revenus).")
    st.success(" • ".join(out))
