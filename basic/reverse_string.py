def reverse_string(s):
    if len(s)==6:
        #first method to reverse
        reversed_string=""
        for char in s:
            reversed_string=char+reversed_string
        return reversed_string
    else :
        #second method to reverse
        return s[::-1]


def reverse_integer(n):
    return int(str(n)[::-1])


print(reverse_string("lawarga ahen"))
print(reverse_integer(12345))

    



