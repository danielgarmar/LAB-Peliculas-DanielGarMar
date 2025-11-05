from peliculas import *
import pathlib

def test_lee_peliculas(filename) -> list[Pelicula]:
    Peliculas = lee_peliculas(filename)
    print(f"Número de películas leídas: {len(Peliculas)}")
    print("Las dos primeras películas son:")
    for pelicula in Peliculas[:2]:
        print(pelicula)
    print("Las dos últimas películas son:")
    for pelicula in Peliculas[-2:]:
        print(pelicula)

    return Peliculas

def test_pelicula_mas_ganancias(peliculas: list[Pelicula], genero: str = None):
    pelicula = pelicula_mas_ganacias(peliculas, genero)
    if genero is not None:
        print(f"La película con más ganancias en el género '{genero}' es:")
        print(pelicula)
    else:
        print(f"La película con mayores ganancias de todas es:")
        print(pelicula)

def test_media_presupuesto_por_genero(peliculas: list[Pelicula]):
    media = media_presupuesto_por_genero(peliculas)
    for genero, presupuesto in media.items():
        print(f"La media de presupuesto para el género '{genero}' es: {presupuesto} millones")

def test_peliculas_por_actor(peliculas: list[Pelicula], anyo_inicial: int = None, anyo_final: int = None):
    peliculas_actor = peliculas_por_actor(peliculas, anyo_inicial, anyo_final)
    for pelicula, count in peliculas_actor.items():
        print(f"{pelicula}: {count} veces")

def test_actores_mas_frecuentes(peliculas: list[Pelicula], n:int, anyo_inicial: int = None, anyo_final: int = None):
    actores = actores_mas_frecuentes(peliculas, n, anyo_inicial, anyo_final)
    print(f"Los {n} actores más frecuentes son:")
    for actor in actores:
        print(actor)

if __name__ == "__main__":
    peliculas = test_lee_peliculas("data/peliculas.csv")
    #test_pelicula_mas_ganancias(peliculas)
    #test_pelicula_mas_ganancias(peliculas, "Acción")
    #test_pelicula_mas_ganancias(peliculas, "Animación")
    #test_media_presupuesto_por_genero(peliculas)
    #test_peliculas_por_actor(peliculas)
    test_actores_mas_frecuentes(peliculas, 3, None, None)
    test_actores_mas_frecuentes(peliculas, 3, 2010, 2018)
