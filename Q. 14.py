dict1 = {
    'jay': 11,
    'nikhil' : 12,
    'yash' : 456,
    'nirav' : 786,
    'chirag' : 564,
    'ayaan' : 5456
}

dict2 = dict(sorted(dict1.items(), key=lambda x:x[1], reverse=True)[:3])
print(dict2)