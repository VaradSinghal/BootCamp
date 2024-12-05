import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

divisors = [2, 3, 4, 5, 6]
lcm_value = divisors[0]
for num in divisors[1:]:
    lcm_value = lcm(lcm_value, num)


multiples = []
i = 1 
count = 0  

while count < 4:
    multiple = 7 * i
    if (multiple - 1) % lcm_value == 0:
        multiples.append(multiple)
        count += 1
    i += 1


print("1st multiple:", multiples[0])
print("2nd multiple:", multiples[1])
print("4th multiple:", multiples[3])
