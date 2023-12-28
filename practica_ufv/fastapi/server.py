import shutil

import io
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile,Form
import pandas as pd
from typing import  List

from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class Contrato(BaseModel):
    id: str
    set: str
    series: str
    publisher: str
    generation: str
    release_date: str
    artist: str
    name: str
    set_num: str
    types: str  # Puede necesitar un tipo diferente si es una lista o estructura compleja
    hp: str  # Asumiendo que es un string, pero podría ser un int si siempre es numérico
    evolvesFrom: str
    weaknesses: str  # Puede necesitar un tipo diferente para estructuras complejas
    attacks: str  # Puede necesitar un tipo diferente para estructuras complejas
    abilities: str  # Puede necesitar un tipo diferente para estructuras complejas
    retreatCost: str  # Puede necesitar un tipo diferente si es una lista
    convertedRetreatCost: float  # Cambiar a int o dejar como float según los datos
    rarity: str
    flavorText: str
    nationalPokedexNumbers: str  # Puede necesitar un tipo diferente si es una lista
    legalities: str  # Puede necesitar un tipo diferente para estructuras complejas
    resistances: str  # Puede necesitar un tipo diferente para estructuras complejas
    rules: str
    regulationMark: str
    ancientTrait: str


class ListadoContratos(BaseModel):
    contratos = List[Contrato]

app = FastAPI(
    title="Servidor de datos de cartas Pokémon",
    description="""Servimos datos de cartas de pokemon""",
    version="0.1.0",
)


@app.get("/retrieve_data/")
#def insercion_endpoint (titulo:str = Form(...), autor:str=Form(...), pais:str=Form(...),genero:str=File(...),  archivo: UploadFile=File(...)):
def retrieve_data ():
    todosmisdatos = pd.read_csv('./poke.csv', sep=',')    
    todosmisdatos = todosmisdatos.fillna(0)
    todosmisdatosdict = todosmisdatos.to_dict(orient='records')
    listado = ListadoContratos()
    listado.contratos = todosmisdatosdict
    return listado
