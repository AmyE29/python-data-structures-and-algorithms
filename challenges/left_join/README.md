## Hashmap LEFT JOIN
Write a function that LEFT JOINs two hashmaps into a single data structure.

#### Challenge

The first parameter is a hashmap that has word strings as keys, and correspoding words as values.
The second parameter is a hashmap that has word strings as keys,and different corresponding words as values.
Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NONE should be appended to the result row.

#### Approach & Efficiency
The appoach we took was to write a function that took in table1. Then if there was a matching key in table2 return a list with that appended the key and the value sets of table1 and the correspoding value of table2 to it.  If there was no matching key in table2, we appended the key and value of table1 and NONE as the value of table2. Then returned the completed list of corresponding key:value sets.  

Time Efficiency: O(n)
Space Efficiency: O(n)

#### Solution
[left_join]https://github.com/AmyE29/python-data-structures-and-algorithms/blob/master/challenges/assets/left_join.jpg