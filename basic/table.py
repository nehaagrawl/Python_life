class table:
    def __init__(self,n):
        self.n=n

    def print_my_table(self):
        for i in range(1,11):
            print(f"{self.n} *{i}={self.n*i}")

n=int(input("enter the number to print its table:"))
table=table(n)
table.print_my_table()
