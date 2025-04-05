# 3. Consider the following code:

def sum_of_squares(num1, num2):
        
    def square(number):
        squared = number**2
        return squared

    total = square(num1) + square(num2)
    return total

print(sum_of_squares(3, 4))     # 25
print(sum_of_squares(5, 12))    # 169
