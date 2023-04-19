T = int(input())
for i in range(T):
    test_number = int(input())
    scores = list(map(int, input().split()))
    reusult = 0

    score_dict = {}
    for i in scores:
        if i in score_dict:
            score_dict[i] += 1
        else:
            score_dict[i] = 1

    max_count = 0
    for key, value in score_dict.items():
        if max_count < value:
            max_count = value
            result = key
        elif max_count == value:
            if result < key:
                result = key
    
    print('#', test_number, result)