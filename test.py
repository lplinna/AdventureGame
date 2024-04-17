colors = {
    "red" : "hot",
    "blue" : "cold",
    "orange": "juicy",
    "brown": "dirty"
}


# Output: red hot blue cold orange juicy brown dirty
#print(" ".join([thing + " " + colors[thing] for thing in colors]))
#print(" " .join([ a[0] + " "+  a[1] for a in colors.items()]))

#for color in colors:
    #print(color + " " + colocrs[color])
# Output red blue orange brown
#print(" ".join([thing for thing in colors]) )
#for color in colors:
#    print(color)
# Output hot cold juicy dirty
#print(" ".join([colors[thing] for thing in colors]) )
#for color in colors:
    #print(colors[color])
# Add a new one: yellow = happy
#colors["yellow"] = "happy"
#print(colors["yellow"])


# Output "Every juicy is hot"
dict_of = []
inputString = "Every orange is red"
subjects = [key for keys in colors.keys() if key in inputString]
print(subjects)
    

print(f"Every {colors[dict_of[0]]} is {colors[dict_of[1]]}")



def bigfunction(a,b,c):
    def smallfunction(number):
        if(number == 0):
            return 3
        else:
          return number
    sum = smallfunction(a) + smallfunction(b) + smallfunction(c)
    return sum


