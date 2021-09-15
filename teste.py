nome = input("Nome: ")
idade = int(input("Idade: "))



if idade <= 0:
    print("Idade invalida...")
elif idade < 18:
    print(f"Ola {nome}, você possui {idade} anos")
    print("Você é menor de idade")
else:
    print(f"Ola {nome}, você possui {idade} anos")
    print("Voce é maior de idade")
    
    
