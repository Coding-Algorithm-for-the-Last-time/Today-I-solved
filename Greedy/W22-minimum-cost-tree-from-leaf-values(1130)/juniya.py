
arr = [11, 12, 12]

sort_arr = sorted(arr, reverse=True)

mct = 0

for i in range(len(sort_arr)):
    if i < (len(sort_arr)-1):
        mct += sort_arr[i]*sort_arr[i+1]

print(mct)
