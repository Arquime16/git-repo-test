def double(number):
    return number / 2

new_number = double(100)
print(new_number)


def uppercase(word):
    return word.upper()

print(uppercase("Arquimedes"))
print(uppercase("Python"))

names = ["Arquimedes", "Jesus", "Maria", "Jose", "Luis", "Carlos", "Ricardo", "Rosa", "Luz", "Lourdes"]

for name in names:
    print(uppercase(name))
