mysting = "the quick, brown fox jumped over the lazy dog!"
mynumbers = [1, 3, 5, 6, 9, 12, 14, 17, 20, 30]
print(len(mysting))
print(len(mynumbers))   
print(max(mysting))
print(min(mynumbers))
prefix = "result: "
result = 5
print(prefix + str(result))
for i in range(5, 15):
    print(i)
for i in range(5, len(mysting), 2):
    print(mysting[i])  
greetings = "hello! "
count = 10
print(f"{greetings} you are customer number: {count}")