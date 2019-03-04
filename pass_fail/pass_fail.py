# pass/fail algorithm

with open("input.txt", 'r') as filehandle:
    count = int(filehandle.readline())
    for x in range(count):
        line = int(filehandle.readline())
        if line < 70:
            print("FAIL")
        else:
            print("PASS")
