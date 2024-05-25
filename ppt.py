u1 = input(print("digite pedra, papel ou tesoura:"))
u2 = input(print("digite pedra,papel ou tesoura:"))


if (u1 == "pedra" and u2== "tesoura" or u2 == "pedra" and u1== "tesoura"):
    print("pedra ganhou")


elif (u1== "tesoura" and u2== "papel " or u1== "papel" and u2== "tesoura"):
    print("papel ganhou")

elif(u1=="papel" and u2== "pedra" or u1== "pedra" and u2== "papel"):
    print("papel ganhou")

else :
    print("empate")