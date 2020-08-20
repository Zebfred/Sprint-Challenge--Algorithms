#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(N) because the calculations of the while loop grows as the size of n grows. Meaning that the code will have to run at longer times as n increases, but the number of iterations will expand linearly. 


b)O(N^2). The nested loops are both related to the size of n so as n increasesk the number of iterations grow exponentially.


c)0(N). As the bunnies increase incrementally, the time associated to run the code will increase in the incremental proportion. Meaning the time will increase linearly as the number of bunnies increase.

## Exercise II

 f >= higher it breaks 

 f < doesn't break

 f == number of dropped + broken eggs is minimized


 One approach to this problem is using binary search logic. For the first attempt, drop an egg at f = n/2. If the egg breaks then you know that f = n/2 is pass the egg breaking height and lower height should be tried, such as (n/2)/2. On the other hand, if the egg didn't break f should be set higher. For example, 
 f = (n/2+n)/2 could be use. This process could be repeated recursively until the floors number are reduce to one choice. This is runtime complexity is desribed as 0(log N).
