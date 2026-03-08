# PALINDROME

mots = input("Entre un mot:")

mot = True

print(mots[0])   # (premier)
print(mots[1])   # (second)
print(mots[2])   # (troisième)
print(mots[-2])  # (avant-dernier)
print(mots[-1])  # (dernier)

for i in range(len(mots) // 2):
    if mots[i] != mots[-1 - i]:
        mot = False
        break

if mot == True:
    print(f"C'est un palindrome")
else:
    print(f"Ce n'est pas un palindrome")
