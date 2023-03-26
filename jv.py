


import pygame
import random

# Definir constantes
CELDA_TAMANO = 20
FILAS = 30
COLUMNAS = 40
ANCHO = COLUMNAS * CELDA_TAMANO
ALTURA = FILAS * CELDA_TAMANO
FPS = 10

# Inicializar Pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((ANCHO, ALTURA))
pygame.display.set_caption("Juego de la Vida")

# Definir colores
VERDE_HACKER = (3, 192, 60)
NEGRO = (0, 0, 0)

# Función para crear la cuadrícula
def crear_cuadricula(filas, columnas):
    cuadricula = [[0 for j in range(columnas)] for i in range(filas)]
    return cuadricula

# Función para dibujar la cuadrícula en modo edición
def dibujar_cuadricula_edicion(cuadricula):
    ventana.fill(NEGRO)
    for i in range(FILAS):
        for j in range(COLUMNAS):
            color = VERDE_HACKER if cuadricula[i][j] == 1 else NEGRO
            pygame.draw.rect(ventana, color, (j * CELDA_TAMANO, i * CELDA_TAMANO, CELDA_TAMANO, CELDA_TAMANO))

# Función para dibujar la cuadrícula en modo juego
def dibujar_cuadricula_juego(cuadricula):
    for i in range(FILAS):
        for j in range(COLUMNAS):
            color = VERDE_HACKER if cuadricula[i][j] == 1 else NEGRO
            pygame.draw.rect(ventana, color, (j * CELDA_TAMANO, i * CELDA_TAMANO, CELDA_TAMANO, CELDA_TAMANO))

# Función para obtener el siguiente estado de la cuadrícula
def siguiente_estado(cuadricula):
    nueva_cuadricula = crear_cuadricula(FILAS, COLUMNAS)

    for i in range(FILAS):
        for j in range(COLUMNAS):
            vecinos_vivos = sum([
                cuadricula[i - 1][j - 1], cuadricula[i - 1][j], cuadricula[i - 1][(j + 1) % COLUMNAS],
                cuadricula[i][j - 1], cuadricula[i][(j + 1) % COLUMNAS],
                cuadricula[(i + 1) % FILAS][j - 1], cuadricula[(i + 1) % FILAS][j], cuadricula[(i + 1) % FILAS][(j + 1) % COLUMNAS]
            ])
            if cuadricula[i][j] == 1 and vecinos_vivos in [2, 3]:
                nueva_cuadricula[i][j] = 1
            elif cuadricula[i][j] == 0 and vecinos_vivos == 3:
                nueva_cuadricula[i][j] = 1

    return nueva_cuadricula

# Función para ejecutar el juego
def ejecutar_juego():
    # Crear la cuadrícula y establecer la configuración inicial
    cuadricula = crear_cuadricula(FILAS, COLUMNAS)
    for i in range(FILAS):
        for j in range(COLUMNAS):
            cuadricula[i][j] = random.randint(0, 1)

    editando = False

    # Definir el reloj
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if editando:
                    # Obtener la posición del clic del usuario
                    pos = pygame.mouse.get_pos()
                    fila = pos[1] // CELDA_TAMANO
                    columna = pos[0] // CELDA_TAMANO

                    # Cambiar el estado de la celda correspondiente
                    if cuadricula[fila][columna] == 0:
                        cuadricula[fila][columna] = 1
                    else:
                        cuadricula[fila][columna] = 0

        # Dibujar la cuadrícula
        dibujar_cuadricula_juego(cuadricula)

        # Obtener el siguiente estado de la cuadrícula
        cuadricula = siguiente_estado(cuadricula)

        # Actualizar la pantalla
        pygame.display.update()

        # Esperar un tiempo para ajustar la velocidad del juego
        reloj.tick(FPS)
def mostrar_menu():
    """Muestra el menú principal"""
    while True:
        # Mostrar opciones de menú
        print("------ Juego de la vida ------")
        print("Seleccione una opción:")
        print("1. Jugar")
        print("2. Editar células iniciales")
        print("3. Salir")
        
        # Obtener selección del usuario
        opcion = input("Ingrese el número de la opción que desea seleccionar: ")

        # Procesar selección del usuario
        if opcion == "1":
            ejecutar_juego()
        elif opcion == "2":
            editar_celulas()
        elif opcion == "3":
            sys.exit()
        else:
            print("Opción inválida. Intente nuevamente.\n")


# Ejecutar el juego
ejecutar_juego()


