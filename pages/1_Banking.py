
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

render_section("banking")
st.subheader(t("quiz"))
with st.form("bank_quiz"):
    profile = st.selectbox("Profil", ["Étudiant","Salarié","Famille","Entrepreneur","Retraité"])
    papers = st.radio("Documents complets ?", ["Oui","Non"], horizontal=True)
    fx = st.radio("Virements internationaux fréquents ?", ["Oui","Non"], horizontal=True)
    branch = st.radio("Besoin d'une agence physique ?", ["Oui","Non"], horizontal=True)
    submitted = st.form_submit_button(t("see_rec"))
if submitted:
    rec = []
    if papers == "Non":
        rec.append("Ouverture rapide : N26 / Revolut / Wise.")
    if profile == "Entrepreneur":
        rec.append("Compte pro : Qonto / Shine / BNP Pro.")
    if fx == "Oui":
        rec.append("International : Revolut / Wise (frais FX bas).")
    if branch == "Oui":
        rec.append("Agence : BNP / Crédit Agricole / Société Générale.")
    if not rec:
        rec.append("Boursorama / Hello bank! (frais bas) selon votre région.")
    st.success(" • ".join(rec))
