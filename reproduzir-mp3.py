#abrir e reproduzir um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('C:\Users\Luciana\Documents\Curso em vídeo\Python\Python-Mundo-1\alive.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('Audio iniciado com sucesso!')
while pygame.mixer.music.get_busy():
    time.sleep(1)

    
