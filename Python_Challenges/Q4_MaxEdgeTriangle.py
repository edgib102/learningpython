print("finds the maximum range of a triangle's third edge")
print("Type side one length")
num1 = int(input())
print("Type side two length")
num2 = int(input())

def next_edge(side1, side2):
    answr = (side1 + side2)-1
    print(answr)
    return answr

next_edge(num1, num2)

# Very easy
# Finds the maximum range of a triangle's third edge
# challenge reference: https://edabit.com/challenge/Zerwo2AENbvRZTe83