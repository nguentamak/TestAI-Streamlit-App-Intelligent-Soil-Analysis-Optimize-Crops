import streamlit as st
import joblib
import pandas as pd

# Titre de l'application
st.title("🌱 Analyse Intelligente du Sol pour Optimiser les Cultures")

# Description
st.write("""
Cette application utilise un modèle d'apprentissage automatique pour prédire le rendement des cultures 
en fonction des caractéristiques du sol. Entrez les valeurs ci-dessous et cliquez sur **Prédire** pour obtenir une estimation.
""")

# Charger le modèle sauvegardé
model = joblib.load('soil_analysis_model.pkl')

# Formulaire pour saisir les valeurs
st.sidebar.header("Entrez les caractéristiques du sol")

# Fonction pour saisir les valeurs
def user_input_features():
    pH = st.sidebar.slider('pH du sol', 4.0, 8.5, 6.5)
    nitrogen = st.sidebar.slider('Teneur en azote (kg/ha)', 0, 150, 50)
    phosphorus = st.sidebar.slider('Teneur en phosphore (kg/ha)', 0, 100, 30)
    potassium = st.sidebar.slider('Teneur en potassium (kg/ha)', 0, 200, 100)
    moisture = st.sidebar.slider('Humidité du sol (%)', 10, 60, 35)
    temperature = st.sidebar.slider('Température moyenne (°C)', 10, 35, 25)
    rainfall = st.sidebar.slider('Précipitations annuelles (mm)', 200, 1200, 800)
    
    # Créer un dictionnaire avec les valeurs saisies
    data = {
        'pH': pH,
        'Nitrogen': nitrogen,
        'Phosphorus': phosphorus,
        'Potassium': potassium,
        'Moisture': moisture,
        'Temperature': temperature,
        'Rainfall': rainfall
    }
    
    # Convertir en DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Afficher le formulaire et récupérer les valeurs
input_df = user_input_features()

# Afficher les valeurs saisies
st.subheader("Valeurs saisies")
st.write(input_df)

# Bouton pour lancer la prédiction
if st.button('Prédire le rendement des cultures'):
    # Faire la prédiction
    prediction = model.predict(input_df)
    
    # Afficher le résultat
    st.subheader("Résultat de la prédiction")
    st.write(f"Le rendement prédit des cultures est : **{prediction[0]:.2f} kg/ha**")