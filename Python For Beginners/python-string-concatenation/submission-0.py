def concatenate(s1: str, s2: str) -> str:
    strlong=s1+s2
    if len(strlong)>10:
        return("Too long!")
    return strlong




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
