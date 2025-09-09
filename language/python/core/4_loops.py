## Sum from 1 to 100 (inclusive) ##
sum = 0
for counter in range(101):
    sum += counter
print(sum)
  
## Factorial Calculator #
n = 6
nFactorial = 1
while n > 1:
    nFactorial *= n
    n -= 1
print(nFactorial)

## Skip Multiples of 3 ##
for number in range(1,21):
    if number % 3 == 0:
        continue
    print(number)