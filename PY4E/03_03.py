score = input("Enter Score: ")
try:
    s = float(score)
    if s > 1.0 :
        print("Score must be a number below 1.0")
        quit()
except:
    print("Score must be a number below 1.0")
    quit()
if s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    print("F")
