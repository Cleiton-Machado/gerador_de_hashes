import hashlib

string = input("\nDigite o texto: ")

menu = int(input(''' ### MENU - ESCOLHA O TIPO DE HASH ###
             
        1 - MD5
        2 - SHA1
        3 - SHA256
        4 - SHA512
            
Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode("utf-8"))
    print(f'A hash MD5 do texto: "{string}", é: {resultado.hexdigest()}')
elif menu == 2:
    resultado = hashlib.sha1(string.encode("utf-8"))
    print(f'A hash SHA1 do texto: "{string}", é: {resultado.hexdigest()}')
elif menu == 3:
    resultado = hashlib.sha256  (string.encode("utf-8"))
    print(f'A hash SHA256 do texto: "{string}", é: {resultado.hexdigest()}')
elif menu == 4:
    resultado = hashlib.sha512(string.encode("utf-8"))
    print(f'A hash SHA512 do texto: "{string}", é: {resultado.hexdigest()}')
else:
    print(f'Opção "{menu}" INVÁLIDA!')

