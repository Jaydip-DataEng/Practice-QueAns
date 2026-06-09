uppercase = 0
lowercase = 0
numeric = 0
special = 0
for char in s:
    if ord(char) >= 65 and ord(char) <= 90:
        uppercase += 1
    elif ord(char) >= 97 and ord(char) <= 122:
        lowercase += 1
    elif ord(char) >= 48 and ord(char) <= 57:
        numeric += 1
    else:
        special += 1

return uppercase, lowercase, numeric, special

#================================================================================

char1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
char2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for char in s:
    if char in char1:
        uppercase += 1
    elif char in char2:
        lowercase += 1
    elif char in char3:
        numeric += 1
    else:
        special += 1

return uppercase, lowercase, numeric, special

# ===========================================================================================

for char in s:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        numeric += 1
    else:
        special += 1

return uppercase, lowercase, numeric, special
