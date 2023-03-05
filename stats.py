# Program: stats.py
# Author: Korey Cioe
# Date: January 25th, 2022
#
# Assignment 1, Intro to Data Strtures
#
# Note: you may NOT use the built-in statistical functions
#       min, max, sum, et.   Instead, create your own code to
#       calculate the answer.
#
#       You may use math.sqrt when calculating the standard deviation

import math

def get_scores():
    '''Get scores interactively from the user

    pre: None
    post: returns a list of numbers obtained from user'''

    nums = []
    while True:
        num = input("Enter a number (<return> to Quit): ")
        if num == "": break
        nums.append(eval(num))
    return nums


def min_value(nums):
    ''' find the minimum

    pre: nums is a list of numbers and len(nums) > 0
    post: returns smallest number in nums'''
    if len(nums) < 1:               #Returns none if the list is less than 1
        return None
    
    minValue = nums[0]              #set variable minValue to equal the nums list
    for i in nums:                  #loop to index into list and search for the lowest number
        if minValue > i:
            minValue = i            #updates the minValue variable to the lowest number in the list
    return minValue                 #returns the minValue variable
    

def max_value(nums):
    ''' find the maximum

    pre: nums is a list of numbers and len(nums) > 0
    post: returns largest number in nums'''
    if len(nums) < 1:               #Returns none if the list is less than 1
        return None

    maxValue = nums[0]              #set variable minValue to equal the nums list
    for i in nums:                  #loop to index into list and search for the highest number
        if maxValue < i:
            maxValue = i            #updates the maxValue variable to the highest number in the list
    return maxValue                 #returns the maxValue variable


def average(nums):
    ''' calculate the mean

    pre: nums is a list of numbers and len(nums) > 0
    post: returns the mean (a float) of the values in nums'''
    if len(nums) < 1:               #Returns none if the list is less than 1
        return None

    sumNum = 0.0                    #sets variable
    for i in nums:                  #loop to add all numbers in list
        sumNum = sumNum + i

    averageNum = sumNum / len(nums) #takes total sum off all numbers in list and divides them by the length of the list
    return averageNum               #returns the average of the list via the averageNum variable

def std_deviation(nums):
    '''calculate the standard deviation

    pre: nums is a list of numbers and len(nums) > 1
    post: returns the standard deviation (a float) of the values in nums'''
    if len(nums) < 1:               #Returns none if the list is less than 1
        return None

    xbar = average(nums)
    sum = 0.0
    for i in nums:
        sum += (xbar - i)**2
    return math.sqrt(sum / (len(nums) - 1))

def distribution(nums):
    ''' Distributes letter grades by how many of each letter grade.

    pre: nums is a list of number and len(nums) > 1
    post: returns the total amount of each letter grade from A to F'''
    
    A = 0
    B = 0
    C = 0
    D = 0
    F = 0
    if len(nums) < 1:               #Returns none if the list is less than 1
        return None
    
    for i in nums:                  #For loop to search each number in the list nums
        if i < 60:                  #Begining of case block to asign each number found in nums to its proper catagory
            F = F + 1               #Updates how many F's have been achieved so far and replaces previous total. 
        elif i <= 69 and i >= 60:
            D = D + 1               #Updates how many D's have been achieved so far and replaces previous total.
        elif i <= 79 and i >= 70:
            C = C + 1               #Updates how many C's have been achieved so far and replaces previous total.
        elif i <= 89 and i >= 80:
            B = B + 1               #Updates how many B's have been achieved so far and replaces previous total.
        else:
            A = A + 1               #Updates how many A's have been achieved so far and replaces previous total.
    return ("A: " ,A," B: ",B," C: ",C," D: ",D, "F: ",F) #end of case block and returns values for all counts. 
   
def main():
    nums = get_scores()
    print(min_value(nums))
    print(max_value(nums))
    print(average(nums))
    print(std_deviation(nums))
    print(distribution(nums))
    
if __name__ == '__main__':
    main()

    
