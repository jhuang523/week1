#practice 1.3

'''Generate a list of prime numbers (numbers that are only divisible by 1 and themselves) from 1 to 10000'''

def getprimes(rnge):
    primes = []
    for n in range (2, rnge+1):
        isPrime = True
        for i in range(2, n):
            if n % i == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(n)
    return primes

print(len(getprimes(10000)))
            

"""Create a function called text_analyzer that takes a string of text as input. 
The function should count the number of words in the text, identify the longest word, and count the occurrences of each unique word. 
BUT the function must skip words that are in a predefined global list of stopwords 
(common words like "the", "is", "at", "which" )"""

import string

stopwords =["the", "is", "was", "are", "that", "at", "which", "a", "an"]
def text_analyzer(txt):
    global stopwords
    words = {}
    longest = ""
    txt = (txt.translate(str.maketrans('','',string.punctuation))).lower() #remove punctuation and make lowercase
    txt_lst = txt.split()
    wordcount = len(txt_lst)
    
    for word in txt_lst:
        if word in stopwords:
            continue
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    for key in words:       #find longest word
        if len(key) > len(longest):
            longest = key
    print(f"Word count: {wordcount}")
    print(f"Longest word: {longest}")
    return words
    

print(text_analyzer("Hey!! hey hey what's up my name is peepee poopoo I love to code,,,, and I am really good at it !!!!"))


"""Vector Class
Create a class Vector that can be initialized with a list of numbers
Implement a method to print a user-friendly string representation of the vector
Overload the + operator to add two vectors of the same dimension (hint: Google 'dunder' methods!)
Implement a method to calculate the dot product of two vectors
Implement a method to calculate multiplication between a vector and a scalar (single number)"""

class Vector:
    def __init__(self, vector):
        self.vector = vector
    
    def __str__ (self):
        return(str(self.vector))
    
    def __add__(self, other):
        try:
            sum = []
            for i in range(len(self.vector)):
                sum.append(self.vector[i] + other.vector[i])         
            return Vector(sum)
        except IndexError:
            print("Vectors must be the same dimension")
    
    @staticmethod
    def dot (v1, v2):      #dot product
        try:
            dp = 0
            for i in range(len(v1.vector)):
                dp += (v1.vector[i] * v2.vector[i])
            return dp
        except IndexError:
            print("Vectors must be the same dimension")
    
    @staticmethod
    def scalar_mult (v, s):
        ls = []
        for i in range(len(v.vector)):
            ls.append(v.vector[i] * s)
        return Vector(ls)

#testing 
v1 = Vector([1,2,5])
print(v1)
v2 = Vector([5,8,2])
print(v1 + v2)
dp = Vector.dot(v1, v2)
print(dp)
scalar = Vector.scalar_mult(v1, 3)
print(scalar)

v3 = Vector([2,7])
print(v1 + v3)
