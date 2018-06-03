"""Functions to implement quick sort"""
def qsort(nums,p,r):
    while p < r:
        q=partition(nums,p,r)
        qsort(nums,p,q-1)
        p=q+1
    return nums

def partition(nums,p,r):
	pivot=nums[r]
	i=p-1
	j=p
	while j<r:
		if nums[j] < pivot:
			temp=nums[i+1]
			nums[i+1]=nums[j]
			nums[j]=temp
			i=i+1
		j=j+1
	temp=nums[i+1]
	nums[i+1]=nums[r]
	nums[r]=temp
	return i+1

def main():
    A=[23, 34, 12, 45, 67, 99, 7, 56, 1, 22, 36, 49, 4, 101, 103, 54, 77, 11, 8, -4]
    qsort(A,0,19)
    print('quick sort module main function')

if __name__ == "__main__":
	main()