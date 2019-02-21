'''
def f(x):
    for i in range(2,x+1):
        for y in range(2,i):
            if i%y==0:
                break
        else:
            yield i

q=int(input("Enter The number"))
gen=f(q)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

'''


'''
str1=input("Enter String")
a=str1.split(" ")
print(a)
for word in a:
    print(''.join(word[-1::-1]))



str1=input("Enter String")
str2=str1.lower()
vowel=0
for i in str1:
    if (i=='a'or i=='e' or i=='i' or i=='o' or i=='u'):
        vowel=vowel+1
print("number of vowel=",vowel)
'''


















'''
#n=int(input("Enter the number"))
class genPrimes(object):
  def __init__(self,x):
    self.primes = x
    self.currentPrime = 1

  def __iter__(self):
    return self

  def __next__(self):
    candidate = self.currentPrime + 1
    while True:
      candidateIsPrime = True
      # candidate is prime iff (candidate % p) != 0 for all earlier primes p
      for prime in self.primes:
        if candidate % prime == 0:
          candidateIsPrime = False
          break
      if candidateIsPrime:
        self.primes.append(candidate)
        self.currentPrime = candidate
        break
      else:
        candidate += 1
    return self.currentPrime

x=[int(input("Enter the number"))]
a=genPrimes(x)
i=a.__iter__()
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
'''
class prime(object):
    i=2
    def __init__(self,num):
        self.number=num
        self.prime1 = True
    def __iter__(self):
        #prime = True
        return self

    def __next__(self):

        for num in range(prime.i,self.number+1):
            self.prime1 = True
            for j in range(2,num):
                #print("num: ",num, "j: ", j)
                if (num%j==0):
                    self.prime1 = False
            prime.i=prime.i+1
            #print(self.prime1)
            if self.prime1:
                return num
                #print (num)

x=int(input("Enter the number"))

a=prime(x)
i=iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
