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

print(averagel1_linf(t1,t2))