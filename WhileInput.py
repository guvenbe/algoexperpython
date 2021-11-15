min_length = 2
while True:
    name = input("enter name name: ")
    if len(name >= min_length) and name.isalpha() and name.isprintable:
        break

print("Hello functional{0}".format(name))
