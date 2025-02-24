def letter_combinations(digits):
    if not digits:
        return []

    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = ['']

    for digit in digits:
        new_combinations = []

        for combination in result:
            for letter in mapping[digit]:

                new_combinations.append(combination + letter)

        result = new_combinations

    return result


digits = "23"
combinations = letter_combinations(digits)
print(combinations)
