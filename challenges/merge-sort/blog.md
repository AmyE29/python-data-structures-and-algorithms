#### Merge Sort: 
Algorthim:
1. Divide the list recursively into two halves until it can no longer be divided.
2. Merge the smaller lists into new list in sorted order.

A visual example is: 
<pre>
          [8, 4, 23, 42, 16, 15]  #Input List
                /      \
        [8, 4, 23]    [42, 16, 15] #split list in half
            /   |          \     \
     [8, 4]   [23]       [42,16]  [15] #split in half again
      /  \     |          /    \    \    
    [8]  [4]  [23]      [42]  [16]  [15] #split into smallest parts
      \  /     /           \   /     /
      [4,8]  [23]         [16,42]  [15] #sort and merge lists
        \     /               \    /        
       [4 ,8, 23]          [15, 16, 42]
            \                   /           
           [4, 8, 15, 16, 23, 42] #return sorted merged array
</pre>