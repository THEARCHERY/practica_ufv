import pandas as pd

import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_agg import RendererAgg
import plotly.express as px
import requests
import seaborn as sns
@st.cache_data
@st.cache
def load_data(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        st.error('Error al cargar datos: Estado {}'.format(r.status_code))
        return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error
    data = r.json()['contratos']
    df = pd.DataFrame(data)
    return df



def info_box (texto, color=None):
    st.markdown(f'<div style = "background-color:#4EBAE1;opacity:70%"><p style="text-align:center;color:white;font-size:30px;">{texto}</p></div>', unsafe_allow_html=True)



matplotlib.use("agg")
lock = RendererAgg.lock

df_pokemon = load_data('http://fastapi:8000/retrieve_data')


#Estadísticas básicas sobre el dataset
num_cards = str(df_pokemon.shape[0])
unique_artists = str(len(df_pokemon.artist.unique()))
unique_types = str(len(df_pokemon.types.unique()))

sns.set_palette("pastel")
plt.rcParams['figure.figsize'] = [10, 6]

st.header("Información general sobre cartas Pokémon")

col1, col2 = st.columns(2)

with col1:
    col1.subheader('# Total de Cartas')
    info_box(num_cards)

with col2:
    col2.subheader('# Artistas Únicos')
    info_box(unique_artists)

st.header("sellecciona aqui el grafico")

opciones = [
    'Media de HP por Generación de Pokémon',
    'Distribución de Rareza de las Cartas',
    'Número de Pokémon por Generación',
]

opcion_seleccionada = st.selectbox('Selecciona una opcion: ', opciones)
datos_pokemon = df_pokemon.copy()
if opcion_seleccionada == 'Media de HP por Generación de Pokémon':
    hp_media_por_generacion = datos_pokemon.groupby('generation')['hp'].mean().reset_index()
    hp_media_por_generacion.columns = ['Generación', 'HP Media']
    fig = px.line(hp_media_por_generacion, x='Generación', y='HP Media',
                  title='Media de HP por Generación de Pokémon',
                  markers=True)

elif opcion_seleccionada == 'Distribución de Rareza de las Cartas':
    rarity_counts = datos_pokemon['rarity'].value_counts().reset_index()
    rarity_counts.columns = ['Rareza', 'Cantidad']
    fig = px.pie(rarity_counts, values='Cantidad', names='Rareza', title='Distribución de Rareza de las Cartas')

elif opcion_seleccionada == 'Número de Pokémon por Generación':
    generation_counts = datos_pokemon['generation'].value_counts().reset_index()
    generation_counts.columns = ['Generación', 'Cantidad']
    fig = px.bar(generation_counts, x='Generación', y='Cantidad', title='Número de Pokémon por Generación')

# Mostrar el gráfico interactivo
st.plotly_chart(fig)