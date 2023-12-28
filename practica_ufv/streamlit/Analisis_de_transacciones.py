
import streamlit as st
import time

st.set_page_config(page_title='Mundo Pokemon', layout='wide',     page_icon="📈")
st.image('ufv.png')

placeholder = st.empty()
with placeholder:
    #from PIL import Image
    #image = Image.open('mired.png')
    #placeholder.image(image, caption='MiRed semantic engine',use_column_width = 'always') 
    for seconds in range(5):
        placeholder.write(f"⏳ {seconds} Cargando sistema")
        time.sleep(1)
placeholder.empty()


st.write("# Vamos a ello 👋")

st.sidebar.success("Selecciona la única página que te voy a dejar seleccionar. Eres libre de seleccionar.")

st.markdown(
    """
    Bienvenidos al mundo vibrante y dinámico de Pokémon, donde la nostalgia y la innovación tecnológica se entrelazan para crear una experiencia única.
    Este dashboard, inspirado en la poderosa simplicidad de Streamlit y la robustez de FastAPI, es más que una simple visualización de datos: es una odisea a través de la rica historia y diversidad de las cartas Pokémon.

    Al igual que un entrenador Pokémon selecciona cuidadosamente su equipo, este proyecto ha sido meticulosamente diseñado para ofrecer una interfaz intuitiva y una experiencia de usuario envolvente.
    Aquí, cada carta se revela no solo como un elemento de juego, sino como una pieza de un tapiz cultural más amplio, uniendo generaciones de aficionados y entusiastas.

    Este dashboard no es solo una herramienta; es un homenaje a la complejidad y el encanto de las cartas Pokémon. Al explorar las diversas páginas, cada una dedicada a un aspecto único de este universo,
    los usuarios podrán interactuar, analizar y sumergirse en los datos de formas que trascienden la mera funcionalidad técnica. Desde visualizaciones interactivas hasta análisis en profundidad,
    cada elemento ha sido cuidadosamente seleccionado para enriquecer la narrativa.

    Así que, con el espíritu de un verdadero entrenador Pokémon, os invito a embarcaros en esta aventura, descubriendo y explorando el universo Pokémon como nunca antes. ¡A por ello!

"""
)
