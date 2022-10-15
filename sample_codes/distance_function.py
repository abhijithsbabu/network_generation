# The methods for all the distance functions will be defined here

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


print(averagel1_linf(t1,t2))
print(dice_distance(t1,t2))
print(gower_distance(t1, t2))
