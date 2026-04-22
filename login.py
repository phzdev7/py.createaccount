   #CRIE UM SISTEMA DE EMAIL


import sys
email_duvida = input('VOCE TEM EMAIL? S/N:  ')
   
if email_duvida.lower() == 's':

    print('BEM VINDO')
    while True:
     email = input('DIGITE SEU EMAIL: ')

     if "@gmail.com" in email:
       break
     else:     
           print("EMAIL INCOMPREENDIDO! VOCÊ PRECISA COLOCAR @gmail.com")             #ATE TER "@gmail.com" NAO VAI PARAR DE REPETIR
     
    senha = input('digite sua senha: ')                           #QUANDO FALAMOS SIM, SOMOS DIRECIONADOS PARA COLOCARMOS O EMAIL E A SENHA
    print(f'OLÁ, O USER TEM O EMAIL: {email} E A SENHA: {senha}')
    sys.exit()
elif email_duvida.lower()== 'n':                                   #.lower()   faz indentificar mesmo se a resposta for maiuscula ou minuscula
   
   criar = input('DESEJA CRIAR UM? S/N: ')
   if  criar.lower() =='s':
    nome = input(str('DIGITE SEU NOME: '))
    print(f'{nome} ENTROU NO SISTEMA')
    idade = int(input('DIGITE SUA IDADE: '))

    if idade >= 18:
      print(f'VOCE TEM {idade}? ESTÁ AUTORIZADO')
    elif idade >= 15:
        print(f'VOCE TEM {idade}? SÓ COM AUTORIZAÇAO') 

        autorizacao = input('VOCE TEM AUTORIZAÇAO DOS RESPONSAVEIS? s/n: ')
        if autorizacao.lower() == 's':
           print('VOCE TEM AUTORIZAÇAO POR CONTA DO RESPONSAVEL')
        elif autorizacao.lower() == 'n':
         print('VOCE NAO PODE')
         sys.exit()
    else:
         print('VOCE NAO PODE')
         sys.exit()
    while True:
     novo = input('DIGITE UM EMAIL: ')
         
     if "@gmail.com" in novo:
        
        break
     else:
        print("SEU NOVO EMAIL DEVE CONTER @gmail.com")
      
    print("EMAIL CADASTRADO COM SUCESSO")
    print("BEM VINDO!")   
    
    
            

    nova = input ('DIGITE UMA NOVA SENHA: ')
    print(f'EMAIL E SENHA CADASTRADO!')
    print(f'EMAIL: {novo} SENHA: {nova}')
    print('EMAIL CADASTRADO! ADEUS!')
    sys.exit()
       
   elif criar.lower() == 'n':
    print('OK, ADEUS')
    sys.exit()
   else:
      sys.exit()
elif email_duvida.lower() == 'n':
     print('FECHANDO SISTEMA!')
     sys.exit()

idade = int(input('DIGITE SUA IDADE: '))

if idade >= 18:
    print(f'VOCE TEM {idade}? ESTÁ AUTORIZADO')
elif idade >= 15:
    print(f'VOCE TEM {idade}? SÓ COM AUTORIZAÇAO')

    autorizacao = input('VOCE TEM AUTORIZAÇAO DOS RESPONSAVEIS? s/n: ')

    if autorizacao.lower() == 's':
        print('VOCE TEM AUTORIZAÇAO POR CONTA DO RESPONSAVEL')
    elif autorizacao.lower() == 'n':
        print('VOCE NAO PODE')
    else:
        print('VOCE NAO PODE')

else:
    print('VOCE NAO PODE')
