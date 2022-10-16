# The methods for all the distance functions will be defined here

import math

#creating a sample time series
t1 = [18,9,3,4,7,8,14,26,14,55,3]
t2 = [25,13,9,4,1,6,72,45,2,4,44]

# function for average L1 L-inf distance 
def averagel1_linf(a,b):
    if(len(a)!=len(b)):
        print("The length of time series are not the same")
        return 0
    dist = 0
    temp_arr = []
    for i in range(len(a)):
        temp_arr.append(abs(a[i]-b[i]))
    for i in temp_arr:
        dist += i
    dist += max(temp_arr)
    dist /= 2
    return dist
        
# function for bhattacharya distance
def bhatt_distance(a,b):
    pass

# function for correlation distance
def corr_function(a,b):
    pass

# function for dice distance
def dice_distance(a,b):
    a_sq = 0
    b_sq = 0
    ab_sq = 0
    for i in range(len(a)):
        a_sq += a[i]*a[i]
        b_sq += b[i]*b[i]
        ab_sq += (a[i]-b[i])**2
    dist = ab_sq/(ab_sq+b_sq)
    return dist

# function for gower distance
def gower_distance(a,b):
    dist = 0
    for i in range(len(a)):
        dist += abs(a[i]-b[i])
    dist /= len(b)
    return dist

# function for kulczynski distance
def kulc_distance(a,b):
    dif_sum = 0
    min_sum = 0
    for i in range(len(a)):
        dif_sum += abs(a[i]-b[i])
        min_sum += min(a[i],b[i])
    dist = dif_sum/min_sum
    return dist

# function for manhattan distance
def manhattan(a,b):
    dist = 0
    for i in range(len(a)):
        dist += abs(a[i]-b[i])
    return dist

# function for sorensen distance
def sorensen(a,b):
    dif_sum = 0
    add_sum = 0
    for i in range(len(a)):
        dif_sum+=abs(a[i]-b[i])
        add_sum += a[i] + b[i]
    dist = dif_sum/add_sum
    return dist

# function for squared euclidean
def sq_euclidean(a,b):
    dist = 0
    for i in range(len(a)):
        dist += (a[i] - b[i])**2
    return dist

# function for tanimoto distance
def tanimoto(a,b):
    numerator = 0
    denominator = 0
    for i in range(len(a)):
        numerator += abs(a[i]-b[i])
        denominator += max(a[i],b[i])
    dist = numerator/denominator
    return dist

# function for lorentzian equation:
def lorent_distance(a,b):
    dist = 0
    for i in range(len(a)):
        dist += math.log(1+abs(a[i]-b[i]),2)
    return dist

# function for jaccard distance
def jaccard(a,b):
    sq_diff = 0
    a_sq = 0
    b_sq = 0
    sq_prod = 0
    for i in range(len(a)):
        sq_diff += (a[i] - b[i])**2
        a_sq += a[i]*a[i]
        b_sq += b[i]*b[i]
        sq_prod += a[i]*b[i]
    dist = sq_diff/(a_sq+b_sq-sq_prod)
    return dist

print(averagel1_linf(t1,t2))
print(dice_distance(t1,t2))
print(gower_distance(t1, t2))
print(kulc_distance(t1,t2))
print(sorensen(t1,t2))
print(manhattan(t1,t2))
print(sq_euclidean(t1,t2))
print(tanimoto(t1,t2))
print(lorent_distance(t1,t2))
print(jaccard(t1,t2))


