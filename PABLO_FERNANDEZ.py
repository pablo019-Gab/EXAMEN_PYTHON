peliculas_iniciales = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
}

cartelera_inicial = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
}


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def cupos_genero(peliculas, cartelera, genero):
    total_cupos = 0
    genero_buscado = genero.strip().lower()
    
    for codigo, datos in peliculas.items():
        genero_pelicula = datos[1].strip().lower()
        if genero_pelicula == genero_buscado:
            if codigo in cartelera:
                total_cupos += cartelera[codigo][1]
                
    print(f"El total de cupos disponibles es: {total_cupos}")


def busqueda_precio(peliculas, cartelera, p_min, p_max):
    resultados = []
    
    for codigo, datos_cartelera in cartelera.items():
        precio = datos_cartelera[0]
        cupos = datos_cartelera[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            if codigo in peliculas:
                titulo = peliculas[codigo][0]
                resultados.append(f"{titulo}--{codigo}")
                
    if not resultados:
        print("No hay películas en ese rango de precios.")
    else:
        resultados.sort()
        print(f"Las películas encontradas son: {resultados}")


def buscar_codigo(peliculas, codigo):
    codigo_buscado = codigo.strip().upper()
    for key in peliculas.keys():
        if key.upper() == codigo_buscado:
            return True
    return False


def actualizar_precio(peliculas, cartelera, codigo, nuevo_precio):
    if buscar_codigo(peliculas, codigo):
        codigo_formateado = codigo.strip().upper()
        for key in cartelera.keys():
            if key.upper() == codigo_formateado:
                cartelera[key][0] = nuevo_precio
                return True
    return False


def validar_codigo_no_existe(peliculas, codigo):
    cod = codigo.strip()
    if not cod:
        return False
    return not buscar_codigo(peliculas, cod)


def validar_titulo(titulo):
    return bool(titulo.strip())


def validar_genero(genero):
    return bool(genero.strip())


def validar_duracion(duracion_str):
    try:
        val = int(duracion_str)
        return val > 0
    except ValueError:
        return False


def validar_clasificacion(clasificacion):
    return clasificacion.strip() in ['A', 'B', 'C']


def validar_idioma(idioma):
    return bool(idioma.strip())


def validar_es_3d(es_3d_str):
    return es_3d_str.strip().lower() in ['s', 'n']


def validar_precio(precio_str):
    try:
        val = int(precio_str)
        return val > 0
    except ValueError:
        return False


def validar_cupos(cupos_str):
    try:
        val = int(cupos_str)
        return val >= 0
    except ValueError:
        return False


def agregar_pelicula(peliculas, cartelera, codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    if buscar_codigo(peliculas, codigo):
        return False
        
    codigo_key = codigo.strip().upper()
    val_es_3d = True if es_3d.strip().lower() == 's' else False
    
    peliculas[codigo_key] = [titulo.strip(), genero.strip(), int(duracion), clasificacion.strip(), idioma.strip(), val_es_3d]
    cartelera[codigo_key] = [int(precio), int(cupos)]
    return True


def eliminar_pelicula(peliculas, cartelera, codigo):
    if buscar_codigo(peliculas, codigo):
        codigo_formateado = codigo.strip().upper()
        clave_a_eliminar = None
        for key in peliculas.keys():
            if key.upper() == codigo_formateado:
                clave_a_eliminar = key
                break
        
        if clave_a_eliminar:
            peliculas.pop(clave_a_eliminar)
            cartelera.pop(clave_a_eliminar, None)
            return True
            
    return False


def main():
    peliculas = dict(peliculas_iniciales)
    cartelera = dict(cartelera_inicial)
    
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")
        
        opcion = leer_opcion()
        
        if opcion == 1:
            genero_buscado = input("Ingrese género a consultar: ")
            cupos_genero(peliculas, cartelera, genero_buscado)
            
        elif opcion == 2:
            while True:
                try:
                    p_min_str = input("Ingrese precio mínimo: ")
                    p_min = int(p_min_str)
                    p_max_str = input("Ingrese precio máximo: ")
                    p_max = int(p_max_str)
                    
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                    else:
                        print("Debe ingresar rangos válidos (min <= max y mayores o iguales a 0).")
                except ValueError:
                    print("Debe ingresar valores enteros")
            
            busqueda_precio(peliculas, cartelera, p_min, p_max)
            
        elif opcion == 3:
            while True:
                codigo = input("Ingrese código de película: ")
                
                while True:
                    try:
                        nuevo_precio_str = input("Ingrese nuevo precio: ")
                        nuevo_precio = int(nuevo_precio_str)
                        if nuevo_precio > 0:
                            break
                        else:
                            print("El precio debe ser un número entero positivo.")
                    except ValueError:
                        print("Debe ingresar un valor entero válido.")
                
                if actualizar_precio(peliculas, cartelera, codigo, nuevo_precio):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                
                rep = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if rep != 's':
                    break
                    
        elif opcion == 4:
            codigo = input("Ingrese código de película: ")
            titulo = input("Ingrese título: ")
            genero = input("Ingrese género: ")
            duracion = input("Ingrese duración (minutos): ")
            clasificacion = input("Ingrese clasificación: ")
            idioma = input("Ingrese idioma: ")
            es_3d = input("¿Es 3D? (s/n): ")
            precio = input("Ingrese precio: ")
            cupos = input("Ingrese cupos: ")
            
            valido = True
            
            if not validar_codigo_no_existe(peliculas, codigo):
                print("Error: Código inválido o ya existente.")
                valido = False
            elif not validar_titulo(titulo):
                print("Error: El título no debe estar vacío.")
                valido = False
            elif not validar_genero(genero):
                print("Error: El género no debe estar vacío.")
                valido = False
            elif not validar_duracion(duracion):
                print("Error: La duración debe ser un entero mayor que cero.")
                valido = False
            elif not validar_clasificacion(clasificacion):
                print("Error: La clasificación debe ser exactamente 'A', 'B' o 'C'.")
                valido = False
            elif not validar_idioma(idioma):
                print("Error: El idioma no debe estar vacío.")
                valido = False
            elif not validar_es_3d(es_3d):
                print("Error: Indique si es 3D ingresando 's' o 'n'.")
                valido = False
            elif not validar_precio(precio):
                print("Error: El precio debe ser un número entero mayor que cero.")
                valido = False
            elif not validar_cupos(cupos):
                print("Error: Los cupos deben ser un entero mayor o igual a cero.")
                valido = False
                
            if valido:
                resultado = agregar_pelicula(
                    peliculas, cartelera, codigo, titulo, genero, 
                    duracion, clasificacion, idioma, es_3d, precio, cupos
                )
                
                if resultado:
                    print("Película agregada")
                else:
                    print("El código ya existe")
                    
        elif opcion == 5:
            codigo = input("Ingrese código de la película a eliminar: ")
            
            if eliminar_pelicula(peliculas, cartelera, codigo):
                print("Película eliminada")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            break


if __name__ == "__main__":
    main()
