def n_fun(i, count=1):
    if i == 1:
        return count
    
    if i % 2 == 0:
        return n_fun(i//2, count+1)
    
    return n_fun(i*3+1, count+1)

# Iterate across the problem range calling `cycle` for each number and storing
# the largest current result which is returned once the whole range is traversed.
def max_count(high, low):
    max = 0
    
    for num in range(low, high):
        result = n_fun(num, 1)
        if result > max:
            max = result
    
    return max

print max_count(22,1)