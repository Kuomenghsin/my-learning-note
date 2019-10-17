
arr = [9,11,8,6,5,12,3,1]


def quick_sort(list):
    small = []
    big = []
    point = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為選取的任意值
        for i in list:
            if i < key: #比任意值小的數
                small.append(i)
            elif i > key: #比任意值大的數
                big.append(i)    
            else:
                point.append(i)
                
                
    small = quick_sort(small)   
    big  = quick_sort(big)
    return small + point  + big

    
quick_sort(arr)

