def is_pangram(s):  

    letters = [chr(i) for i in range(97, 123)]

    for letter in letters:
            if letter not in s.lower():
                return False    

    return True
