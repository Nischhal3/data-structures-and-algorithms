
# Exercise: Custom Encoder
#
# Write a function called custom_encoder that accepts a string
# and returns a list of each character's 0-based position in
# the reference string. If a character is not found, return -1.

def custom_encoder(text):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()

    return [reference_string.find(char) for char in text]
    
print(custom_encoder('My house is beautiful'))
print(custom_encoder(''))
print(custom_encoder('ä'))
print(custom_encoder('Test!'))