import pygame
import sys

#Iniciar pygame
pygame.init()

# Configurar la ventana
ancho = 500
alto = 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Hola Mundo!')

# Configurar colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Configurar el tipo de letra
tamanio = 48
fuente = pygame.font.SysFont(None, tamanio)

# Configurar el texto
texto = fuente.render('Hello world!', True, BLANCO, AZUL)
textoRect = texto.get_rect()
textoRect.centerx = ventana.get_rect().centerx
textoRect.centery = ventana.get_rect().centery
ventana.blit(texto, textoRect)

# Pintar el fondo de la ventana
ventana.fill(BLANCO)

# Pintar un poligono
pygame.draw.polygon(ventana, VERDE, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Pintar lineas
tamanio = 4
pygame.draw.line(ventana, AZUL, (60, 60), (120, 60), tamanio)
pygame.draw.line(ventana, AZUL, (120, 60), (60, 120))
pygame.draw.line(ventana, AZUL, (60, 120), (120, 120), tamanio)

# Pintar circulo en la ventana
xcentro = 300
ycentro = 50
radio = 20
linea = 0
pygame.draw.circle(ventana, AZUL, (xcentro, ycentro), radio, linea)

# Pintar Elipse
linea = 0
pygame.draw.ellipse(ventana, ROJO, (300, 250, 40, 80), linea)

# Pintar Rectangulo alrededor del texto
izquierda = textoRect.left - 20
arriba = textoRect.top - 20
ancho = textoRect.width + 40
alto = textoRect.height + 40
pygame.draw.rect(ventana, ROJO, (izquierda, arriba, ancho, alto ))

# Pintar el texto en la ventana
ventana.blit(texto, textoRect)

# Mostra la ventana en pantalla
pygame.display.update()

# Bucle de eventos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
