# pass/fail algorithm

# vowels = "aioue"
# print("u" in vowels)
# print("o" in vowels)
# print("i" in vowels)
# print("a" in vowels)
# print("e" in vowels)

with open("../ExampleInputs/Prob02.in.txt", 'r') as filehandle:
    count = int(filehandle.readline())
    for x in range(count):
        line = filehandle.readline()
        vowel_count = 0
        for character in line:
            vowels = "aioue"
            if character in vowels:
                vowel_count += 1
        print(vowel_count)