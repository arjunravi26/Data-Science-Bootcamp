# Question 1: Find the First Non-Repeating Character
# Given a string, find the first character that does not repeat anywhere in the string. If all characters are repeating, return a message indicating that all characters repeat.

# Example:

# Input: "swiss"
# Output: 'w'
text = "aswissswi0"
non_repeat_word = ""
for char in range(len(text)):
    check_text = text[:char] + text[char+1:]
    if text[char] not in check_text:
        non_repeat_word = text[char]
        break
if non_repeat_word:
    print(non_repeat_word)
else:
    print("All characters repeat.")
