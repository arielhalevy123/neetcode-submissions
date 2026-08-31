from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    ch_count={}
    for ch in word:
        if ch in ch_count:
            ch_count[ch]+=1
        else:
            ch_count[ch]=1
    return ch_count
    




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
