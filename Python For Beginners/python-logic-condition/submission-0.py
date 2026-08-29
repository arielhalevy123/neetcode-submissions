def discount_applies(age: int) -> bool:
    if age >= 65 or age<18:
        return True
    return False




# don't modify this code below this line
print(discount_applies(17))
print(discount_applies(18))
print(discount_applies(40))
print(discount_applies(65))
print(discount_applies(70))
