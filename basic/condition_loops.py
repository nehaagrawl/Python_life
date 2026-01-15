user_age= int(input("Enter your AGE correctly : "))



if user_age>=18:
    print("Congratulation!! You can Vote.")
elif user_age>14:
    print("You are teenager")
else:
    print("You are child")


for n in range(user_age):
    print("user age count",n)
    

print("\nWhile loop counting down:")
count = user_age
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Done!")