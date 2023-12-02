x = int(input("qual o valor de x? "))

match x:
    case 1:
        print("um")
    case 2:
        print("dois")
    case _:
        print("nenhum")
