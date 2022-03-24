import re #módulo do python para expressões regulares

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")

busca = padrao.search(endereco) #search é um método do objeto pattern criado pelo compile devolvendo um objeto Match

if busca:
    cep = busca.group() #Método qua vai devolver a string do objeto Match
    print(cep)
