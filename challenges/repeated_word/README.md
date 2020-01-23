### Challenge - Repeating Word Search

*** Author: Amy Evans Version: 1.0.0 ***

Write a funtion that returns the first word to occur more than once in a provided string.

#### Challenge
Take the input string and iterate through it until you find a repeated word. 

#### Approach & Efficiency
The approach is to take the string and split it into individual words. Using Regex, you take out all of the punctuation that could make the word 'fun' different than the word 'fun!'. Iterate through the words in the string and compare if it is already in the list of words, if it is you found the first repeating word and return that. If is is not already in the list append it to the list of words and continue to iterate through the words until you find the first match. If there are no matches, return None.

The efficency is O(N) for time and O(N) for space.

#### Solution
https://github.com/AmyE29/python-data-structures-and-algorithms/blob/master/challenges/assets/repeated_words.jpg
