'''
冒牌排序(Bubble sort)
算法步骤：
1、比较相邻的元素，如果前者大于后者，则交换；
2、对每一对相邻元素作同样的操作，从开始第一对到结尾最后一堆。这样最后的元素是最大的数；
3、针对所有的元素重复上述的步骤，除了最后一个；
4、持续上面的操作，直到没有一对元素需要比较
平均时间复杂度:O(n^2)
最好情况:O(1)
最坏情况O(n)
空间复杂度:O(1)
稳定性:稳定
'''
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    data = [1,3,5,11,55,2,4,5]
    print(bubbleSort(data))