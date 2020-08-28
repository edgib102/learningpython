print("finds the area of a triangle")
print("Type base")
num1 = int(input())
print("Type height")
num2 = int(input())

def tri_area(base, height):
    answr = (base * height) / 2
    print(answr)
    return answr

next_edge(num1, num2)

# challenge reference: https://edabit.com/challenge/aWLTzrRsrw7RakYrN
# pretty much copy-pasted from Q3
# finished my quota of the super easy ones