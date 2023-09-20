from fractions import Fraction

def approximate_fraction(numerator, denominator, decimal_places):
    fraction = Fraction(numerator, denominator)
    result = round(fraction, decimal_places)
    
    return result

numerator, denominator = map(int, input().split())
decimal_places = int(input())

result = approximate_fraction(numerator, denominator, decimal_places)
print(float(result)) 