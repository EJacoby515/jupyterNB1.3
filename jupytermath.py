def sqft():
    print("We are going to determine the general square footage of a home, come along with me")
    leng = int(input("what is the approx length of your home?: \n"))
    width = int(input("what is the approx width of your home?: \n"))

    print("as a reminder,  A = L x W \nWhere  A(area) is the square footage")
    print(f"let's plug it in, shall we? A = {leng} * {width}")

    print(f"So the Area, or Square footage would be: {leng * width}")

sqft()


def jupytercircum():
    print("we are going to find the circumference of a circle: \n")

    dia = int(input("what would you like the diameter to be?:\n"))

    print("we will be using the formual C = 2 π r | and for π we will use 3.14")
    print(f"so lets plug it in C = 2 π {dia/2}")

    print(f"so your circumference will be...  \n {2*3.14*(dia/2)}")
jupytercircum()
