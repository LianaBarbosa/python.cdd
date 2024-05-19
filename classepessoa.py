class Pessoa:
    def __init__(self, nome, acordado = True):
         self.nome = nome
         self.acordado = acordado

    def comer(self):
        print("comendo")
    def andar(self):
        print("andar")

    def dormir(self):
     self.acordado = False
     print("Zzzzz...")

p1 = Pessoa("joão")
p1.comer()
p1.andar()
p1.dormir()
print(p1)
