#### Quick Sort: 

Quick Sort uses a divide and conquer method of sorting. It is based around a chosen pivot point, and then you sort the values as less than the pivot point and more than the pivot point.

A visual example is: 

1. The input list is unsorted:
[8, 4, 23, 42, 16, 15] 
               
2. The last value is chosen as pivot point:
[8, 4, 23, 42, 16, ***15*** ]
        
3. The numbers smaller than 15 are moved to the front of the list, the numbers greater than 15 are moved to the end of the list
[8 , 4]  ***15*** [23, 42, 16]

4. Now 4 is the pivot point(last number) of the [8, ***4***] list and 16 is the pivot point of the [23, 42, ***16***] list and 15 is still in the middle 
[8, ***4***] [15] [23, 42, ***16***]

5. The numbers smaller than 4 are moved to the front, and larger are moved to the rear.
[4, 8] 
 new list is [4, 8] [15] [23, 42, ***16***]

6. The numbers smaller than 16 are moved to the front, and larger are moved to the rear.
[16, 23 ,42]
new list is [4, 8, 15, 16, 23, 46]

7. The you return the newly sorted list.
