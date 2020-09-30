'''
You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a dictionary ↴ , 
where the keys are words and the values are the number of times the words occurred.

Think about capitalized words. For example, look at these sentences:

'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'

What do we want to do with "After", "Dana", and "add"? In this example, your final dictionary should include one "Add" or "add" with a value of 22. 
Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".


NEED TO LEVERAGE ARRAY SPLICING 

------------
 ATTEMPT 1
------------

        # Count the frequency of each word
        
        #Initialize list, dictionary, and temp_var
        self.general_punc_list = ['.', '!', ':', '?', ',',' ', ' \' ', '-']
        self.temp_string = ""
        self.words_to_counts = {}
        
        # For loop will go through the given input string
        
        for i in range(len(input_string)):
            # Check if the current letter is in the general_punc_list and,
            # Check if 
            
            # If current character isn't a punctuation, add it to temp string holder
            if (input_string[i].lower() not in self.general_punc_list ):
                self.temp_string += input_string[i].lower()
            
            # If current character is a general punctuation, skip this letter
            elif (input_string[i] in self.general_punc_list):
                
                # If temp_string's word is in the dictionary already, we'll increase its value
                if self.temp_string in self.words_to_counts:
                    self.words_to_counts[self.temp_string] += 1
                
                # If word not in the dictionary, we'll enter a new entry with a default value of 1
                else:
                    self.words_to_counts[self.temp_string] = 1
                
                temp_string = ''

--------------
 ATTEMPT TWO
--------------

 # List of given input_string
        self.list_input_string = input_string.split()
        
        # Word data dictionary
        self.words_to_counts = {}
        
        # To check if current word is a punctutation
        self.general_punc_list = ['.', '!', ':', '?', ',',' ', '-']
        
    
    
        # Loop through list
        for word in self.list_input_string:
            
            # Compare word not in general punctuation list & make word not in dictionary
            if (word not in self.general_punc_list) and (word not in self.words_to_counts):
                
                self.words_to_counts[word] = 1
            
            else:
                # If word already in dictonary, just increment its value by 1
                
                self.words_to_counts[word] += 1
        
        print(self.words_to_counts)

'''

import unittest


class WordCloudData(object):

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)
    
    def populate_words_to_counts(self, input_string):
        
        current_word_start_index = 0
        current_word_length = 0
        
        for i, character in enumerate(input_string):
            
            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index : current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
        
            # if we reach a space or emdash we know we're at the end of a word, so we add it to the dictionary & reset our current word
            elif character == ' ' or character == '\u2014':
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index : current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0
            
            # Split on ellipses, so if we get two periods in a row we add the curernt word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string) - 1 and input_string[i+1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index : current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0
            
            # If the character is a letter or an apostrophe, we add it to our current word
            elif character.isalpha() or character == '\'':
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1
            
            
            # If the character is a hyphen, we want to check if it's surrounded by letters
            elif character == '-':
                if i > 0 and input_string[i-1].isalpha() and input_string[i+1].isalpha():
                    
                    if current_word_length == 0:
                        current_word_start_index = i
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index : current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0
    
    def add_word_to_dictionary(self, word):
        
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1
        
        # If a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1
        
        
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]
        
        
        # Otherwise the word is not in the dictionary
        else:
            self.words_to_counts[word] = 1
# Tests 

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)