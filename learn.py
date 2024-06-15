def same_start_letter(text):
    words = text.split()  # Split the text into a list of words
    if len(words) != 2:   # Check if there are exactly two words
        return False
    return words[0][0].lower() == words[1][0].lower()  # Compare the first letters

# Check
print(same_start_letter("Crazy Kangaroo"))  # Expected output: True
