# TSP con Hill Climbing
import math
import random

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

# Calcular la distancia cubierta por cada ruta
def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    ciudad1 = ruta[-1]
    ciudad2 = ruta[0]
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total

def hill_climbing(coord):
    # Crear la ruta inicial aleatoria
    ruta = list(coord.keys())
    random.shuffle(ruta)
    
    mejora = True
    while mejora:
        mejora = False
        dist_actual = evalua_ruta(ruta, coord)
        # Evaluar vecinos
        for i in range(len(ruta)):
            if mejora:
                break
            for j in range(len(ruta)):
                if i != j:
                    ruta_tmp = ruta[:]
                    # Intercambiar dos ciudades
                    ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                    dist = evalua_ruta(ruta_tmp, coord)
                    if dist < dist_actual:
                        # Se ha encontrado un vecino que mejora el resultado
                        mejora = True
                        ruta = ruta_tmp[:]
                        break
    return ruta

if __name__ == "__main__":
    coord = {
        'Jiloyork': (19.916012, -99.580580),
        'Toluca': (19.289165, -99.655697),
        'Atlacomulco': (19.799520, -99.873844),
        'Guadalajara': (20.677754472859146, -103.34625354877137),
        'Monterrey': (25.69161110159454, -100.321838480256),
        'QuintanaRoo': (21.163111924844458, -86.80231502121464),
        'Michohacan': (19.701400113725654, -101.20829680213464),
        'Aguascalientes': (21.87641043660486, -102.26438663286967),
        'CDMX': (19.432713075976878, -99.13318344772986),
        'QRO': (20.59719437542255, -100.38667040246602)
    }
    
    ruta = hill_climbing(coord)
    print(ruta)
    print("Distancia Total:", evalua_ruta(ruta, coord))
