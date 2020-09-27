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

'''


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


'''
ATTEMPT TWO
'''


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