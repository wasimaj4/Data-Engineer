# Challenge 1: In Range
def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    return False

print(in_range(10, 5, 15))
print(in_range(5, 10, 15))

# Challenge 2: Same Name
def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    return False

print(same_name("Alice", "Alice"))
print(same_name("Bob", "Alice"))

# Challenge 3: Always False
def always_false(num):
    if num > 0 and num < 0:
        return True
    return False

print(always_false(5))
print(always_false(-5))

# Challenge 4: Movie Review
def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    if rating < 9:
        return "This one was fun."
    return "Outstanding!"

print(movie_review(3))
print(movie_review(7))
print(movie_review(10))

# Challenge 5: Max Number
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie!"

print(max_num(5, 3, 9))
print(max_num(9, 9, 2))
print(max_num(8, 11, 8))
