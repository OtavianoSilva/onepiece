from one_piece_timeline_project.wsgi import *
from core.models import *


with open("lista_capítulos.txt", mode="r", encoding="UTF8") as lista:

    contador = 0
    for line in lista.readlines():
        contador += 1
        ponto = line.find(".")
        numero = line[:ponto]
        titulo = line[ponto+1:]

        if contador < 9: ano = 1997
        elif contador < 54: ano =1998
        elif contador < 100: ano = 1999
        elif contador < 146: ano = 2000
        elif contador < 196: ano = 2001
        elif contador < 248: ano = 2002
        elif contador < 296: ano = 2003
        elif contador < 337: ano = 2004
        elif contador < 389: ano = 2005
        elif contador < 431: ano = 2006
        elif contador < 471: ano = 2007
        elif contador < 513: ano = 2008
        elif contador < 552: ano = 2009
        elif contador < 595: ano = 2010
        elif contador < 637: ano = 2011
        elif contador < 679: ano = 2012
        elif contador < 722: ano = 2013
        elif contador < 764: ano = 2014
        elif contador < 807: ano = 2015
        elif contador < 839: ano = 2016
        elif contador < 880: ano = 2017
        elif contador < 922: ano = 2018
        elif contador < 965: ano = 2019
        elif contador < 985: ano = 2020
        elif contador < 1026: ano = 2021
        elif contador < 1056: ano = 2022
        else: ano = 2023

        if contador < 8: busca = "Romance Down"
        elif contador < 18: busca = "Orange Town"
        elif contador < 42: busca = "Vila Syrup"
        elif contador < 69: busca = "Baratie"
        elif contador < 100: busca = "Arlong Park"
        elif contador < 106: busca ="Montanha reversa"
        elif contador < 115: busca ="Whisky peak"
        elif contador < 130: busca ="Little garden"
        elif contador < 155: busca ="Ilha Drum"
        elif contador < 218: busca ="Alabasta"
        elif contador < 237: busca ="Jaya"
        elif contador < 303: busca ="Skypiea"
        elif contador < 322: busca ="Long ring long land"
        elif contador < 375: busca ="Water 7"
        elif contador < 431: busca ="Enies Lobby"
        elif contador < 442: busca ="Pós-Enies Lobby"
        elif contador < 490: busca ="Thriller Bark"
        elif contador < 514: busca ="Sabaody"
        elif contador < 525: busca ="Amazon Lily"
        elif contador < 550: busca ="Impel Down"
        elif contador < 581: busca ="Marineford"
        elif contador < 598: busca ="Pós-guerra"
        elif contador < 603: busca ="Retorno a Sabaody"
        elif contador < 654: busca ="Ilha dos tritões"
        elif contador < 700: busca ="Punk Hazard"
        elif contador < 802: busca ="Dressrosa"
        elif contador < 825: busca ="Zou"
        elif contador < 903: busca ="Whole Cake"
        elif contador < 909: busca ="Reverie"
        elif contador < 1058: busca ="Wano"
        else: busca ="Egg-Head"

        arco = arco = Arc.objects.filter(name=busca)

        c = Chapter(
            number=numero,
            title=titulo.lower(),
            year=ano,
            arc=arco[0],
            spoiler=False)
        
        c.save()
        



