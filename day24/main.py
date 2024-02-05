# with open("my_file.txt") as file:
#     contens = file.read()
#     print(contens)
#     file.close()

with open("my_file.txt", mode= "a") as file:
    file.write("\nNow I appending cuz of a in mode.")