# 11. Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

idx = 0

while idx < len(my_list):
    
    idx2 = 0
    
    while idx2 < len(my_list[idx]):
        
        if my_list[idx][idx2] % 2 == 0:
            print(my_list[idx][idx2])
        idx2 += 1
    
    idx += 1