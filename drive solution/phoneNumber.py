dig = input()

digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

combs = [""]

for digit in dig:
    temp = []
    for comb in combs:
        for letter in digit_to_letters[digit]:
            temp.append(comb + letter)
    combs = temp

for i in combs:
    print(i,end = " ")
