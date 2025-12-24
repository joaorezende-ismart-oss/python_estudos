import winsound
winsound.PlaySound('musica.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
input('ENTER para parar')
winsound.PlaySound(None, winsound.SND_PURGE)
