print("Boas meu menino, atão?.")
print("Vou começar por te apresntar o objetivo deste jogo.")
introdução = ("\nApos um naufragio acordaste em uma floresta encantada, mas tem há um problema a floresta e escura e tem sons assustadores, e o teu objetivo e tentar encontrar um tesouro com varias fortunas!!!")
print(introdução)
password =(input("Insire a password (pista tem estes numeros T6Y):"))
if password == "Y6T": 
   print("Password errada")
   exit()
if password == "6YT": 
   print("Password errada")
   exit()
if password == "TY6": 
   print("Password errada")
   exit()
if password == "6TY": 
  print("\nBoa escolha!! ")
  print("\nVamos começar por explorar a floresta.")
  escolha3 = (input("\nEncontras uma caverna com uma fogueira acessa, vamos entrar."))
  print("\nDentro da caverna encontras um caixa velha mas com varias luzes a sair dela.")
  escolha5 = (input("Queres abrir? (sim):"))
  if escolha5 == "sim":
   print("\nEncontras um mapa da floresta onde te da indicações para chegares ao tesouro!")
   print("\nAlem de encontrares o mapa, encontras tambem  uma mochila com uma lanterna, duas aguas, uma faca e curativos.")
   caminho =(input("\nTens 3 opções de prosseguir o tem caminho, em qual te queres aventurar? (direita, meio, esquerda):"))
   if caminho == "direita":
     print("\nVamos la então.")
     print("Ves um gnomo que parece ser amigavel.")
     print("\nFoste ter com ele.")
     print("Ele tem uma chave na mão, ele quer te oferecer.")
     chave = (input("\nAceitas? (sim):"))
     if chave == "sim":
      print("\nA chave que ele te deu é a do grande tesouro, tiveste sorte agora so te falta encontrar onde ele esta.")
      print("\nAndas mais um bocado e encontras um pokemon, o snorlax, ele nao te diz nada apenas aponta para um caminho obscruo.")
      aceitas = (input("Aceitas ir? (sim):"))
      if aceitas == "sim":
           print("\nEncontras uma pá e um X grande no chão, parece que tiveste sorte neste caminho.")
           print("Começas a escavar, e sim encontras o grande tesouro.")
           print("\nFIM. foste corajoso e certeiro neste caminho.\n Obrigado guerreio.")
           exit()
   if caminho == "esquerda":
    print("\nNãoooo puto, tas lixado neste caminho.")
    print("\nComeças a andar no meio da floresta escura e com cheiros horriveis, tens sorte que na tua mochila, tens uma lanterna.")
    print("\nEncontras um barabaro.")
    print("\nEle vem na tua direção.")
    print("\nBarbaro:")
    print("-Ta tudo mano, mais um a procura do grande tesouro?, tenho uma proposta para ti.")
    print("\nSe conseguires matar o rei da tribo, eu dou te chave do bau.")
    escolhabarbaro = (input("\nQueres aceitar?:"))
    if escolhabarbaro == "sim":
     print("\nO Barabro deu te um escudo de prata, e um arco e flecha")
     print("Tambem te deu as indicações certas da casa do rei da tribo.")
     print("\nSegues as indicações todas e chegas ao grande casa do rei da tribo.")
     print("\nTas prestas a atirar nele, tens tres flechas, mas uma chega para o matar, tas pronto?")

     vidadoinimigo = 100
     print(" Vida do rei da tribo é 100.") 
     print("\nAtiras a primeira flecha.")
     print("Agora a vida do rei da tribo é", vidadoinimigo - 55)
     print("\nTens só mais uma flecha.")
     print("Tens que ser certeiro")
     print("\nAgora a vida do rei da tribo é", vidadoinimigo - 100)
     print("\nBEM!!")
     print("Matas te!!!")
     print("\Voltas para o barbaro, e contas o relato.")
     print("Ele apenas da te uma agua verde e vai embora.")
     agua = (input("Vais tomar? (sim/nao):"))
     if agua == "sim": 
       print("Morreste envenenado.")
       exit()
     if agua == "nao":
       print("\nContinuas a caminhar pela floresta, ate que avistas uma casa na arvore")
       print("\nTem umas escadas.")
       print("\nDecides subir.")
       print("Dentro da casa notas que é muito velha e que tem um cheiro muito mau, mas notas que uma musica muita baixa vem dentro de uma caixa.")
       print("\nTenstas procurar a caixa.")
       print("Encontras a caixa, abres e dentro dela tem a verdadeira chave do bau.")
       print("\nSais da casa e notas que a chave tem uma bomba que tem um contador de 15 segundos, ou seja tens 15 segundos para encontrar o bau.")
       print("\nMas ao desceres da casa deparas te com a familia do rei da tribo, ja sabes oque vai acontecer.")
       print("\nComeças a correr da tribo e o temporizador começa a baixar.")
       print("\n15")
       print("\n14")
       print("\n13")
       print("\n12")
       print("\n11")
       print("\n10")
       print("TAS NUMA SITUAÇÃO MUITO COMPLICADA.")
       print("\nMas ao longe avistas um X grande no chão.") 
       correr = (input("\nDesjas correr o mais rapido possivel? (sim/nao):"))
       if correr == "sim":
        print("\nComeças a acelarar , e cais no chão, e a bomba arrebenta.")
        print("Morreste.")
        print("\nFim do jogo")
        exit()
       if correr == "nao":
         print("\nContinuas a correr normal, e chegas ao bau salvo.")
         print("Consgues abrir o bau, e vences o jogo.")
         print("\nMuito bem guerreiro!!!!")
         exit()
   if caminho == "meio":
      print("\n...")
      print("Caiste num buraco com mais de 20m, era uma armadilha de uma tribo, tiveste azar.")
      exit()
