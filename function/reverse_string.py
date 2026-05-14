# string[start : stop : step]
# start → where to begin
# stop → where to end
# step → how to move

# What does -1 mean?

# It means:
# 👉 move backward one step at a time.
def reverse_string(s):
    return s[::-1]


def reverse_array(arr):
    return arr[::-1]


print(reverse_string("Harsh"))
print(reverse_array([1, 2, 3, 4, 5]))