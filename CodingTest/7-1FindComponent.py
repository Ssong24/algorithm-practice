"""
* Find Components
In electronic stores, there are 'N' components.
Each component has its own serial number.
If customer asks 'M' components with specific kinds,
you need to write whether your store has it or not.
(There's no redundant serial number in stores or customer's component array)

* Input *
5           # N (1 ~ 1,000,000)
8 3 7 9 2   # serial numbers of components in store (integer, 1~1,000,000)
3           # M (1 ~ 100,000)
5 7 9       # serial numbers of components customer asks(integer, 1~ 1,000,000)
-------
* Output *
no yes yes
"""

def findCompoenent():
    # Get N(number of components in store)
    n = int(input())
    # Get components' serial number with blank
    seller = list(map(int, input().split()))
    seller.sort()  # sorting

    # Get m (number of components buyer wants)
    m = int(input())
    # Get components' serial number with blank
    buyer = list(map(int, input().split()))
    buyer.sort()  # sorting

    # Check requested component's serial number one by one
    for i in range(m):
        result = binary_search(seller, buyer[i], 0, n - 1)
        if result is None:
            print("no", end=" ")
        else:
            print("yes", end=" ")


def counting_sort(n,store_array, custom_array):
    count_array = [0] * (n+1)

    for num in store_array:
        count_array[num] = 1  # No redundant component's serial number

    for num in custom_array:
        if count_array[num] == 1:
            print('yes', end=' ')
        else:
            print('no', end=' ')


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# findCompoenent()

# Algorithm Time Test
import random
import time


def set_func(stores,customers):
    stores = set(stores)

    for i in customers:
        if i in stores:
            print('yes', end=' ')
        else:
            print('no ', end=' ')


def timeTest_bs(n,m,stores, customers):
    # Binary Search
    for i in range(m):
      result = binary_search(stores, customers[i], 0, n-1)
      if result is None:
        print("no", end=" ")
      else:
        print("yes", end=" ")

maxN = 1000000
maxM = 100000

# Random array for customers
stores= list(range(1, maxN+1))
customers = random.sample(range(1, maxN+1), maxM)

print(len(customers) == maxM)
# Sort
customers.sort()

start_time = time.time()
# timeTest_bs(maxN,maxM,stores,customers)  # 1.081 [sec]
# counting_sort(maxN, stores,customers) # 0.686 [sec]
set_func(stores, customers) # 0.592 [sec]
end_time = time.time()
print('\nTime: ', end_time - start_time)
