class NaturalNum:
    def sum_of_n_natural_num(self,n):
        return n*(n+1)/2
    
    def num(self,n):
        value=0
        for i in range(0,n+1):
            value+=i
        return value

    

n_ob=NaturalNum()
n=5
print(n_ob.num(n))
print(n_ob.sum_of_n_natural_num(n))
        