
# Benew — Streamlit (multilingue, questionnaires, outils)

## Déployer depuis un téléphone
1. Ouvre GitHub (mobile) → **New repository** → `benew-streamlit`.
2. Appuie **Add file → Upload files** et envoie **tout le contenu** de ce projet (ou le ZIP puis dézippe via une app si besoin).
3. Va sur **Streamlit Community Cloud** → **New app** → choisis le repo et le fichier principal **app.py** → **Deploy**.
4. Ouvre l’URL publique — ajoute-la à l’écran d’accueil pour une expérience type app.

## Structure
- `app.py` — accueil + sélecteur de langue.
- `pages/` — Banque, Assurance, Santé, Fiscalité, Logement, Transport, Travail, Vie quotidienne, Outils.
- `data/` — `content.py` (texte multilingue), `utils.py` (i18n & rendu).
- `.streamlit/config.toml` — thème sombre élégant.

## Modifier le contenu
Tout le texte est dans `data/content.py` (dictionnaire `CONTENT`).

## Dépendances
- `streamlit>=1.29`
