import string

def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    newlist = set(lst)
    newlist = list(newlist)
    return newlist

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    uppers = 0
    lowers = 0
    for letter in string:
        if letter.isupper():
            uppers += 1
        if letter.islower():
            lowers += 1
    return (f"Uppercase count: {uppers}", f"Lowercase count: {lowers}")

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    s = ""
    for char in sentence:
        if char not in string.punctuation:
            s = s+char
    return s

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    sentence = remove_punctuation(sentence)
    count = 0 # count starts in 1 to count for the first letter
    for ind, char in enumerate(sentence):
        if char == " " and sentence[ind-1] in string.ascii_letters:
            count += 1
    return count