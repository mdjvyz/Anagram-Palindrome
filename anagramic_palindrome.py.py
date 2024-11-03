

def anagramic_palindrome(firststring, secondstring):
    
    #Tells us that if the length of the first string doesnt match the length of the second string than the function returns false
    if len(firststring) != len(secondstring):
        return False
    
    #initalizes the character count to an empty list
    character_count = {}

    #double for loop for setting a counter for so we can compare both strings
    for char in firststring:
        character_count[char] = character_count.get(char, 0) + 1
    
    for char in secondstring:
        if char in character_count:
            character_count[char] = character_count[char] - 1
        else:
            return False

    #for loop to check if the counters value is zero if it is it returns false    
    for count in character_count.values():
        if count != 0:
            return False
    
    #this sets right to the length of the first string - 1 and left to 0
    #while right is greater than the left and if the left string and the second string do not equal it returns false
    right, left = len(firststring) - 1, 0
    while right > left:
        if firststring[left] != secondstring[right]:
            return False
    #right is set to right -1
    #left is set to left + 1 and then returns true
        right = right - 1
        left = left + 1

    return True

print(anagramic_palindrome("racecar", "racecar"))
print(anagramic_palindrome("Kristofferson", "nosreffotsirK"))
print(anagramic_palindrome("Taste", "State"))
      
