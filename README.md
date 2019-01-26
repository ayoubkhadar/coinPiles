# coinPiles

# Problem

Josh and Karl have come up with a new game. The games rules is as followed, using Josh's coin collection, one player must split the coin collection into piles, remove a certain amount of coins from each pile and make a new pile. If the player's new pile contains the same amount of coins in each pile, then that player gets a point.

If the collection has piles of [4,5,8] coins and the amount to be removed from each pile is 2 then the resulting piles would be [2,3,6,2]. This new pile is different from the original pile, therefore this outcome does not get the player a point.

# Input Format

The first line contains an integer x, the amount of integers in the array arr.
The second line contains an integer n, the amount of coins removed from each pile.
The third line contains an array arr, an unsorted array of the amount of coins in each pile.


# Constraints

0 < n < 10000
0 < x < 10000
0 < arr[i] < 10000


# Output Format

return 1 if the given arr will be unchanged, return 0

# Sample Input 0

4
1
1 2 3 4
# Sample Output 0

1
# Explanation 0

When you remove one coin off of each pile, the new collection contains piles of [1,2,3,4] coins

# Sample Input 1

3
2
4 5 8
# Sample Output 1

0
