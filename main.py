def main() -> None:
    opcion = ""
    while opcion != "3":
        print("\n***TRANSFORMADOR DE BASES NUMÉRICAS")
        print("\n[1] Binario a decimal\n[2] Decimal a binario\n[3] Salir")
        opcion = str(input("\nElija una opción: "))
        if opcion not in ['1', '2', '3']:
            print("\n Por favor elija una opcion válida (1, 2, 3).")
        
        elif opcion == '1':
            bin = str(input("\nIngrese un número binario: "))
            es_binario = True
            for n in bin:
                if n not in ['0', '1']:
                    es_binario = False
            if es_binario:
                dec = binario_a_decimal(int(bin))
                print(f"\n({bin})2 = ({dec})10")
            else:
                print("\nPor favor, ingrese un número binario válido.")
        
        elif opcion == '2':
            dec = str(input("\nIngrese un número decimal: "))
            if dec.isdigit():
                bin = decimal_a_binario(int(dec))
                print(f"\n({dec})10 = ({bin})2")
            else:
                print("\nPor favor, ingrese un número decimal válido.")
    
    print("\nAdiós :)")

def binario_a_decimal(binario: int) -> int:
    decimal = 0
    exp = 0
    while binario != 0:
        decimal += (binario % 10) * (2 ** exp)
        exp += 1
        binario = binario // 10
    return decimal

def decimal_a_binario(decimal: int) -> str:
    lista_bin = []
    while decimal != 0:
        decimal = decimal / 2
        if str(decimal)[-1] != '0':
            lista_bin.append(1)
        else:
            lista_bin.append(0)
        decimal = int(decimal)
    while len(lista_bin) < 8:
        lista_bin.append(0)
    lista_bin.reverse()
    binario = ""
    for bit in lista_bin:
        binario += str(bit)
    return binario

main()