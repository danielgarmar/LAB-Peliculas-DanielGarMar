from pathlib import Path
from typing import NamedTuple
from datetime import date, datetime
from typing import List
import csv

Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos",List[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", List[str])
    ]
)

def lee_peliculas(archivo: str) -> list[Pelicula]:
    with open(archivo, "r", encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        peliculas = []
        next(lector)  # Saltar la cabecera si es necesario
        for fila in lector:
            fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto = fila
            pelicula = Pelicula(
                fecha_estreno=datetime.strptime(fecha_estreno, "%d/%m/%Y").date(),
                titulo=titulo,
                director=director,
                generos=generos.split(",") if generos else [],
                duracion=int(duracion),
                presupuesto=int(presupuesto),
                recaudacion=int(recaudacion),
                reparto=reparto.split(",") if reparto else []
            )
            peliculas.append(pelicula)
    return peliculas

def pelicula_mas_ganacias(peliculas: list[Pelicula], genero: str = None) -> Pelicula:
    max_ganancias = 0
    pelicula_max = ""
    for pelicula in peliculas:
        if genero in pelicula.generos:
            ganancias = pelicula.recaudacion - pelicula.presupuesto
            if ganancias > max_ganancias:
                max_ganancias = ganancias
                pelicula_max = pelicula.titulo
        elif genero == None:
            ganancias = pelicula.recaudacion - pelicula.presupuesto
            if ganancias > max_ganancias:
                max_ganancias = ganancias
                pelicula_max = pelicula.titulo
    return pelicula_max

def media_presupuesto_por_genero(peliculas: list[Pelicula]) -> dict[str, float]:
    pelis_generos = {}
    presupuesto_generos = {}
    for pelicula in peliculas:
        for g in pelicula.generos:
            if g in pelis_generos.keys() and g in presupuesto_generos.keys():
                pelis_generos[g] += 1
                presupuesto_generos[g] += pelicula.presupuesto
            else:
                pelis_generos[g] = 1
                presupuesto_generos[g] = pelicula.presupuesto

    media_presupuesto = {}
    for g in pelis_generos.keys():
        media_presupuesto[g] = presupuesto_generos[g] / pelis_generos[g]
    return media_presupuesto

def peliculas_por_actor(peliculas: list[Pelicula], anyo_inicial: int = None, anyo_final: int = None) -> dict[str, int]:
    peliculas_actor = {}
    for pelicula in peliculas:
        if anyo_final == None or (anyo_final is None or pelicula.fecha_estreno.year >= anyo_final) and (anyo_inicial is None or pelicula.fecha_estreno.year <= anyo_inicial):
            for actor in pelicula.reparto:
                if actor in peliculas_actor:
                    peliculas_actor[actor] += 1
                else:
                    peliculas_actor[actor] = 1
    if anyo_inicial is not None and anyo_final is not None and anyo_inicial > anyo_final:
        raise ValueError("El año inicial no puede ser mayor que el año final.")
    return peliculas_actor

def actores_mas_frecuentes(peliculas: list[Pelicula], n: int = 5, anyo_inicial: int = None, anyo_final: int = None) -> dict[str, int]:
    peliculas_actor = peliculas_por_actor(peliculas, anyo_inicial, anyo_final)
    actores_frecuentes = sorted(peliculas_actor.items(), key=lambda x: x[1], reverse=True)

    return dict(actores_frecuentes[:n])