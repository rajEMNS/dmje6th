def phone_combination(digits):
    if not digits:
        return []
        
    digits_letter = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    def backtrack(index,combinations):
        if index == len(digits):
            result.append(combinations)
            return
        current = digits[index]
        for i in digits_letter[current]:
            backtrack(index+1,combinations + i)
            
    result = []
    backtrack(0,"")
    return result
    
digits = input()
result = phone_combination(digits)
for i in result:
    print(i,end = " ")
