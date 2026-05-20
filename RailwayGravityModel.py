
def calculateGravity(a, b, distance): #a and b are locations
    if (a <= 0 or b <= 0 or distance <= 0):
        return 0
    else:
        gravity = (a*b)/pow(distance,2) #This formula calulates gravity; Pow returns power of 2
    return gravity


def main():
    return None

main()