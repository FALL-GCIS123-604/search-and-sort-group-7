import time 
import random
import arrays

def insertion_sort(array):
    
    def swap(f, s):
        
        temp = array[f]
        array[f] = array[s]
        array[s] = temp
    
    for i in range(len(array) - 1):
        
        j = i + 1
        
        if array[i] > array[j]:
            
            swap(i, j)
            i += 1
            j -= 1
            
            while array[j] < array[j-1] and j > 0:
                
                swap(j, j - 1)
                j -= 1
                
    return array



def generate_sorted_data(size):
    array=arrays.Array(size) 
    array = [random.randint(1, 100) for _ in range(size)]
    print(array)
    return insertion_sort(array)

size = int(input("Size of array - "))

sorted_array = generate_sorted_data(size)
print(sorted_array)

target = eval(input("Please enter the target = "))

def binary_search(sorted_array, target):

    lw = 0 
    """lowest index value"""
    l = len(sorted_array) - 1 #highest index value(can change in loop)
    h = l #highest index value(won't change in loop)
    flag = "green"

    while lw <= h:  

        """program runs as long as lw not greater than h"""
        m = (lw+l)//2 
        """midpoint is taken"""
    
        if sorted_array[m] > target: 
            l = m-1 
            """highest index value changes"""

        elif sorted_array[m] < target:

            lw = m+1  
            """lowest index value changes"""
            l = h 
            """highest index value of the array is put in l""" 

        else:
            print("Index : ",m) 
            """if sorted_array[m] = target then program breaks"""
            break  

    else: 
        """if lw > h then target is not in array"""
        print("Index : None, as it is not in the array")
        flag = "red"

    if flag == "green": 
        """if value in binary search then index is returned else None is returned"""
        return m
    
    else:
        return None
    
binary_search(sorted_array, target)

def generate_sorted_data(size):
    """extended function"""
    data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(size)]
    return merge_sort(data)

def merge_sort(data):
    
    if len(data)>1:
        
        mid=len(data)//2
        
        """splitting in halves"""
        left=data[:mid]
        right=data[mid:]
        merge_sort(left)
        merge_sort(right)
        
        """initialising"""
        i = j = k = 0
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                data[k]=left[i]
                i+=1
                k+=1
            else:
                data[k]=right[j]
                j+=1
                k+=1
        
        while i<len(left) and j>=len(right):
            data[k]=left[i]
            i+=1
            k+=1
        
        while i>=len(left) and j<len(right):
            data[k]=right[j]
            j+=1
            k+=1
        
        return data
    
large_sorted_data = (generate_sorted_data(990))
print(large_sorted_data)


def linear_search(array,target):
    la = len(array)
    flag = "red"
    for i in range(la):
        if target == array[i]:
            flag = "green"
            break
    if flag == "green" :
        print("Index :",i)
        return i 
    else:
        print("Index : None, as it is not in the array")
        return None
    

"""time for linear search"""        
start_bin=time.perf_counter()
linear_search(large_sorted_data,72)
end_bin=time.perf_counter()
lin_time=start_bin-end_bin
"""time for binary search"""     
start_bin=time.perf_counter()
binary_search(large_sorted_data,72)
end_bin=time.perf_counter()
bin_time=start_bin-end_bin 
print("time for linear:",lin_time,"\ntime for binary:",bin_time)