from one_piece_timeline_project.wsgi import *
from core.models import *


with open("lista_episódios.txt", mode="r", encoding="UTF8") as lista:

    filler = [
        54, 55, 56, 57, 58, 59, 60, 98, 99, 102, 131, 132, 133, 134, 135, 136, 137, 138, 139, 
        140, 141, 142, 143, 196, 197, 198, 199, 200 ,201, 202, 203, 204, 205, 206, 220, 221,
        222, 223, 224, 225, 226, 279, 280, 281, 282, 283, 291, 292, 303, 317, 318, 319, 326,
        327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 382, 383, 384, 406, 407, 426, 427, 
        428, 429, 457, 458, 492, 542, 575, 576, 577, 578, 590, 626, 627, 747, 748, 749, 750, 
        780, 781, 782, 895, 896, 907, 1029, 1030 ]

    contador = 0
    for line in lista.readlines():
        contador += 1
        ponto = line.find(".")
        numero = line[:ponto]
        titulo = line[ponto+1:]

        ano = 1999 if contador < 9 else 2000 if contador < 53 else 2001

        filler_arc = Arc.objects.filter(id=6)
        arco = arco = Arc.objects.filter(id=(1 if contador < 4 else 2 if contador < 9 else 3 if contador < 19 else 4 if contador < 31 else 5 if contador < 54 else 6))


        if contador in filler:
            e = Episode(
                number=numero,
                title=titulo,
                year=ano,
                arc=filler_arc[0],
                filler=True)
        else: 
            e = Episode(
                number=numero,
                title=titulo,
                year=ano,
                arc=arco[0],
                filler=False)
        
        e.save()
        