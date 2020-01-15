###Insertion sort 

Sorts the list one item at a time.

If your sample list is: 
 [8,4,23,42,16,15]

The function would go through the following steps.
1. It would mark 8 as sorted
 [ 8, 4 , 23, 42, 16, 15]
      
2. It would then look at 4 
 [8, 4 , 23, 42, 16, 15]
      |
     [4]
 And compare 4 to 8, since it is less than 8 , it would insert it in the front of the list
 [4, 8, 23, 42, 16, 15]
 
 And move down the list until the items were sorted.
 <pre>
        [8, 4 , 23, 42, 16, 15]
            |
           [4] # compares 4 to 8, and inserts 4 in front of 8
        [4, 8 , 23, 42, 16, 15]
                 |
                [23] #compares 23 to 8, and leaves 23 in place
        [4, 8 , 23, 42, 16, 15] 
                     |
                    [42] #compares 42 to 23 and leaves 42 in place
        [4, 8 , 23, 42, 16, 15]  
                         |
                        [16] #compares 16 to 42, inserts it in front
        [4, 8 , 23, 16, 42, 15]                 |
                    [16] #compares 16 to 23, inserts it in front
        [4, 8 , 16, 23, 42, 15] 
                |
               [16] # compares 16 to 8 and leaves in place             
         [4, 8 , 16, 23, 42, 15]   
                              |
                             [15] #compares 15 to 42, inserts it in front
        [4, 8 , 16, 23, 15, 42]                    |
                       [15] #compares 15 to 23, inserts it in front
        [4, 8 , 16, 15, 23, 42] 
                    |
                    [15] # compares 15 to 16, inserts it in front
        [4, 8 , 15, 16, 23, 42] 
                 |
                [15] # compares 15 to 8 and leaves it in place
       
       
        return the new sorted list           
 </pre>