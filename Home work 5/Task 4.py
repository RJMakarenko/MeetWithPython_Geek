string = input() + ' '
count_of_digits = 1
digit = ''
rle_string = ''
for number_of_symbol in range(len(string)):
    if string[number_of_symbol] == digit:
        count_of_digits += 1
    else:
        if digit:
            rle_string += str(count_of_digits) + str(digit)
        digit = string[number_of_symbol]
        count_of_digits = 1
print(rle_string)