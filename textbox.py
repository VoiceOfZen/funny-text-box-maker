sus = input("Put ur word here: \n")


# +---+
# | 0 |
# +---+
# for every LETTER print box
# A. store it in 2 lists
# one thing will print up and down +---+ for every letter
# between | L | 
new = []
up = []
for letter in sus:
    up += ["+---"]
    new += ["| " + letter + " "]

up += ["+"]
new += ["|"]

up = "".join(up)
new = "".join(new)
down = up

print(up + "\n" + new + "\n" + down)
