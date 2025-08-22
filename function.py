def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    uniq_char =[]
    for char in string:
        if char in vowels and char not in uniq_char:
            uniq_char.append(char)
            count += 1
    
    return count


check = 'aeAEiodfsafsafeefsfeU'       
print(count_vowels(check))     