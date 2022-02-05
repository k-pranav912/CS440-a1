from random import randint, random, randrange

def generate_grid(x, y, path):
    f = open(path, "w")
    f.write(str(randint(1, x+1)) + " " + str(randint(1, y+1)))
    f.write("\n" + str(randint(1, x+1)) + " " + str(randint(1, y+1)))
    f.write("\n" + str(x) + " " + str(y))
    for i in range(x):
        for j in range(y):
            if random() <= 0.1:
                f.write("\n" + str(i+1) + " " + str(j+1) + " 1")
            else:
                f.write("\n" + str(i+1) + " " + str(j+1) + " 0")