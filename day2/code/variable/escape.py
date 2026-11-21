multiline = "Life is too short\nYou need python"
lines = ["Life is too short\nYou need python",
         "Life is too short\tYou need python",
         "Life is too short\\ou need python",
         "Life is too short\'You need python",
         "Life is too short\"You need python",
         "Life is too short\rYou need python",
         "Life is too short\fYou need python",
         "Life is too short\bYou need python"]

#print(multiline)
for i in lines:
    print(i)