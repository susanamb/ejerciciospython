flag = True
while flag:
    print("Welcome, please select a select a song from this top 10 songs:")
    print("1-Ciega, Sordomuda - Shakira")
    print("2-Azúcar Amargo - Fey")
    print("3-Laura No Está - Nek ")
    print("4-Estoy Aquí - Shakira ")
    print("5-Mírame a los Ojos - Onda Vaselina")
    print("6-Rayando el Sol - Maná")
    print("7-Lamento Boliviano - Enanitos Verdes")
    print("8-Livin’ La Vida Loca – Ricky Martin")
    print("9-Antologia - Shakira")
    print("10-La Carencia - Panteon Rococo")
    cat = {1:"Ciega, Sordomuda de Shakira", 2:"Azúcar Amargo de Fey", 3:"Laura No Está de Nek", 4:"Estoy Aquí de Shakira", 5:"Mírame a los Ojos de Onda Vaselina", 6:"Rayando el Sol de Maná", 7: "Lamento Boliviano de Enanitos Verdes", 8: "Livin’ La Vida Loca de Ricky Martin", 9: "Antologia de Shakira", 10: "La Carencia de Panteon Rococo"}
    opc = int(input())
    lyr = cat[opc]
        
    print("Elegiste",lyr, " ahi te va la letra:")
    print(f"--------{lyr}----------")
    if opc == 1:
        print("Bruta, ciega, sordomuda\nTorpe, traste y testaruda\nEs todo lo que he sido\nPor ti me he convertido\nEn una cosa que no hace\nOtra cosa mas que amarte\nPienso en ti día y noche\nY no se como olvidarte")
    elif opc == 2:
        print("Eres azúcar amargo\nUn delirio y pecado\nUn cofre de sorpresas ciegas\nMe besas y...\nEres azúcar amargo\nUn ángel y un diablo\nMaldito embustero, sólo siento\nQue te estoy perdiendo")
    elif opc == 3:
        print("Eres azúcar amargo\nUn delirio y pecado\nUn cofre de sorpresas ciegas\nMe besas y...\nEres azúcar amargo\nUn ángel y un diablo\nMaldito embustero, sólo siento\nQue te estoy perdiendo")
    elif opc == 4:
        print("Y ahora estoy aquí\nQueriendo convertir\nLos campos en ciudad\nMezclando el cielo con el mar\nSé que te dejé escapar\nSé que te perdí\nNada podrá ser igual")
    elif opc == 5:
        print("Mírame a los ojos, no diré nada\nMira mis ojos, no me des la espalda\nMírame a los ojos, sobran las palabras\nMira mis ojos, lee lo que siento\nMírame a los ojos, no diré nada\nMira mis ojos, no me des la espalda\nMírame a los ojos, sobran las palabras\nMira mis ojos, dime lo que lees ahí")
    elif opc == 6:
        print("Rayando el sol, desesperación\nEs más fácil llegar al sol que a tu corazón\nMe muero por ti, viviendo sin ti\nY no aguanto, me duele tanto estar así\nRayando el sol")
    elif opc == 7:
        print("Me quieren agitar\nMe incitan a gritar\nSoy como una roca\nPalabras no me tocan\nAdentro hay un volcán\nQue pronto va a estallar\nYo quiero estar tranquilo")
    elif opc == 8:
        print("Ella que será\nShe's livin' la vida loca\nY te dolerá\nSí, de verdad te toca\nElla es tu final\nVive la vida loca\nElla te dirá\nVive la vida loca\nShe's livin' la vida loca")
    elif opc == 9:
        print("Para amarte\nNecesito una razón\nY es difícil creer\nQue no exista una más que este amor\nSobra tanto\nDentro de este corazón\nY a pesar de que dicen\nQue los años son sabios\nTodavía se siente el dolor")
    elif opc == 10:
        print("Por la mañana yo me levanto\nNo me dan ganas de ir a trabajar\nSubo a la combi voy observando\nQue toda la gente comienza a pasar\nPor la avenida va circulando\nEl alma obrera de mi ciudad\nGente que siempre esta trabajando\nY su descanso lo ocupa pa' soñar\nPa' soñar carnal")
    
    print("\n Presiona cualquier tecla para elegir otra cancion o presiona 2 para salir")
    men = input()
    if men == '2':
        flag = False


