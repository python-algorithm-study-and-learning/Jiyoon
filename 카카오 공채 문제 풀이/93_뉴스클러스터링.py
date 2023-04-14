from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_set = [a+b for a, b in zip(str1, str1[1:]) if a.isalpha() and b.isalpha()]
    str2_set = [a+b for a, b in zip(str2, str2[1:]) if a.isalpha() and b.isalpha()]
    
    counter1 = Counter(str1_set)
    counter2 = Counter(str2_set)

    intersection = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    if not intersection and not union:
        return 65536
    else:
        return int(len(intersection) / len(union) * 65536)
