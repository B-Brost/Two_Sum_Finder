# Two_Sum_Finder

This Python program contains a class named Solution with three methods: twoSum, bruteForce, and dictSum. All methods are designed to find two numbers in a list that add up to a specific target number.

twoSum(nums, target): This method uses a dictionary to store the numbers from the list as it iterates through them. For each number, it calculates the complement (target - current number) and checks if the complement exists in the dictionary. If it does, it returns the indices of the complement and the current number. If no such pair is found, it returns an empty list.
bruteForce(nums, target): This method uses a brute force approach to find the two numbers. It iterates through the list of numbers twice with two nested loops, checking all possible pairs of numbers. If it finds a pair that adds up to the target and the indices are not the same, it returns the indices of the two numbers.
dictSum(nums, target): This method is similar to twoSum. It also uses a dictionary to store the numbers from the list. For each number, it calculates the complement and checks if it exists in the dictionary. If it does, it returns the indices of the complement and the current number. If no such pair is found, it returns an empty list.
These methods provide efficient ways to solve the two-sum problem, which is a common problem in coding interviews and has various applications in different fields. Please note that all methods return an empty list or tuple if no pair is found that adds up to the target.
