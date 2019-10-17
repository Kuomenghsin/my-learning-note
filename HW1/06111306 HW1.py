
arr = [9,11,8,6,5,12,3,1]


def quick_sort(list):
    less = []
    more = []
    middle = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為選取的任意值
        for i in list:
            if i < key: #比任意值小的數
                less.append(i)
            elif i > key: #比任意值大的數
                more.append(i)    
            else:
                middle.append(i)
                
                
    less = quick_sort(less)   
    more  = quick_sort(more)
    return less + middle  + more

    
quick_sort(arr)

