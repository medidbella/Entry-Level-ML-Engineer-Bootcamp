kata = (19, 42, 21, 45, 6, 9)
print(f"The {len(kata)} numbers are : ", end='')
for i in range(len(kata)):
    print(f"{kata[i]}{', ' if i < len(kata) - 1 else ''}", end='')
print()
