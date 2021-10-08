alfabeto = "abcdefjhijklmnopqrstuvwxyz"

deslocamento= 25

frase= "teste"

def cifraCesar(deslocamento, alfabeto):
    cifra = ""
    for i in alfabeto[deslocamento-1:]:
        cifra += i 
        if i == "z":
            for i in alfabeto[:deslocamento-1]:
                cifra += i
     
    return cifra

       
def decodificar(frase, cifra):
      codigo = ''
      cifra = cifra
      for i in frase:
            if i == ' ':
                  codigo+=i
            else:
                  codigo += cifra[alfabeto.index(i)]
      return codigo
        


print(cifraCesar(deslocamento, alfabeto))

print(decodificar(frase, cifraCesar(deslocamento, alfabeto)))


