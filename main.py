import os


#clearing screen
if os.name=='nt':
    os.system("cls")
else:
    os.system('clear')


print()
print()
print()
print("\t\t\t\t\t\t\t\t", "welcome to the future")
txt = "banana"
x = txt.center(30, "O")
print('{:^24s}'.format("MyString"))
print(x)
print()
print("\t\t\t\t\t\t\t\t", "MENU")
