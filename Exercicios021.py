import pygame

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega o arquivo MP3 (coloque o caminho correto do arquivo)
pygame.mixer.music.load('nome_do_arquivo.mp3')

# Reproduz o áudio
pygame.mixer.music.play()

# Espera o usuário encerrar
input("Pressione Enter para parar a música...")
pygame.mixer.music.stop()
