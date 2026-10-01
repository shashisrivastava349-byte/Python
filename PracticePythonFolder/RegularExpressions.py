import re

# pattern="[Ss]hashi"
# pattern="ye[sp]"
# pattern="[skf]it"
# pattern="[9157]it"
# pattern="[a-zA-Z]it"
# pattern="[0-9]it"
# pattern="[a-zA-Z0-9]it"
pattern="[^0-9]it"

print("Enter a string to check if it contains the pattern 'Shashi':")

text=input()

if re.search(pattern,text):
    print("The pattern 'Shashi' is present in the string.")

else:
    print("The pattern 'Shashi' is not present in the string.")
