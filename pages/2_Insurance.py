
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

render_section("insurance")
st.subheader(t("quiz"))
with st.form("ins_quiz"):
    housing = st.radio("Louez-vous un logement ?", ["Oui","Non"], horizontal=True)
    car = st.radio("Avez-vous une voiture ?", ["Oui","Non"], horizontal=True)
    mutuelle = st.radio("Souhaitez-vous une complémentaire santé ?", ["Oui","Non"], horizontal=True)
    submitted = st.form_submit_button(t("see_rec"))
if submitted:
    out = []
    if housing == "Oui": out.append("Habitation (obligatoire pour locataires).")
    if car == "Oui": out.append("Auto (obligatoire en France).")
    if mutuelle == "Oui": out.append("Mutuelle santé (conseillée).")
    if not out: out.append("Responsabilité civile recommandée (souvent incluse dans habitation).")
    st.success(" • ".join(out))
