def biggest(a, b):
    if a>b:
        return a
    else:
        return b

def somatory(lista, x=0):
    somatory = 0
    for number in lista:
        somatory += number
    somatory += x
    return somatory

def average(lista):
    length = 0
    somatory = 0
    for number in lista:
        length += 1
        somatory += number
    average = somatory / length
    return average

def equal_values(listaA, listaB):
    listaR = []
    for numberA in listaA:
        for numberB in listaB:
            if numberA == numberB:
                listaR.append(numberA)
    return listaR

def position_first_equal_value(listaA, listaB):
    counter = 0
    for numberA in listaA:
        for numberB in listaB:
            if numberA == numberB:
                return counter
        counter += 1
    return None

if __name__ == "__main__":
    print("Testando funcao biggest entre 1 e 2: " + str(biggest(1, 2)))
    listaA = [1, 2, 3, 4, 5]
    listaB = [0 ,2, 4, 6, 8]
    print("Soma dos elementos da lista A: " + str(somatory(listaA)))
    print("Soma dos elementos da lista B: " + str(somatory(listaB)))
    print("Media dos elementos da lista A: " + str(average(listaA)))
    print("Media dos elementos da lista B: " + str(average(listaB)))
    print("Lista dos elementos iguais entre as listas A e B: " + str(equal_values(listaA, listaB)))
    print("Posicao do primeiro elemento igual entre as listas A e B: " + str(position_first_equal_value(listaA, listaB)))