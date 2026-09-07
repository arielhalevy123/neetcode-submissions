from typing import List

def read_integers() -> List[int]:
    lst=input()
    parts=lst.split(',')
    nums_map =map(int,parts)
    nums_lst=list(nums_map)
    return nums_lst
    
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
