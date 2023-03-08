withdraw = float(input())
notes100 = withdraw/100
resto = withdraw%100
notes50 = int(resto/50)
resto = resto%50
notes20 = int(resto/20)
resto = resto%20
notes10 = int(resto/10)
resto = resto % 10
notes5 = int(resto/5)
resto = resto % 5
notes2 = int(resto/2)
resto = resto % 2


resto = int(resto * 100)
coins1 = int(resto/100)
resto = resto % 100
halfs = int(resto/50)
resto = resto % 50
quarters = int(resto/25)
resto = resto % 25
tenths = int(resto/10)
resto = resto % 10
fifths = int(resto/5)
resto = resto % 5
print("NOTAS:")
print(int(notes100), "nota(s) de R$ 100.00")
print(notes50 , "nota(s) de R$ 50.00")
print(notes20, "nota(s) de R$ 20.00")
print(notes10, "nota(s) de R$ 10.00")
print(notes5, "nota(s) de R$ 5.00")
print(notes2, "nota(s) de R$ 2.00")
print("MOEDAS:")
print(coins1, "moeda(s) de R$ 1.00")
print(halfs, "moeda(s) de R$ 0.50")
print(quarters, "moeda(s) de R$ 0.25")
print(tenths, "moeda(s) de R$ 0.10")
print(fifths, "moeda(s) de R$ 0.05")
print(resto, "moeda(s) de R$ 0.01")