# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    
    if sorted(word) == sorted(anagram):

        return True
    return False
    
    # [assignment] Add your code here

    # return True

print(find_anagram('listen', 'silent'))
print(find_anagram('say', 'yes'))
# print(find_anagram())