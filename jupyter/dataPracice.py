from __future__ import division #이것을 써주어야 평균값이 더 정확히 계산된다는????
import collections
import matplotlib.pyplot as pit
import math


num_friends = [100, 40, 30, 54, 25, 3, 100,100, 3,3,3,3,3,3,3,3,3,3,3]
# collcetion의 Counter 함수로 동일한 데이터 표현해줌
# 3이 몇개, 100이 몇개 이런식으로
friends_counts = collections.Counter(num_friends)
print('friends:', friends_counts)

# 가시화 추가
xs = range(101)
ys = [friends_counts[x] for x in xs]

'''

pit.bar(xs,ys)
# x축 y축의 범위를 정해줌.
pit.axis([0,101,0,30])
# 축의 이름을 정해줌
pit.xlabel(" # of friends")
pit.ylabel(" # of people")
pit.show()
'''
# 데이터의 개수 
num_points = len(num_friends)
print(num_points)
# 가장 큰 값
num_max = max(num_friends)
print(num_max)
# 가장 작은 값
num_min = min(num_friends)
print(num_min)

# 정렬해서, 원하는 값 뽑아낼 수 있음
sorted_value = sorted(num_friends)
print("두번째로 작은 값")
print(sorted_value[1])
# 두번째로 큰 값. -1은 제일 뒤의 값을 가리키니까.
print("두번째로 큰 값")
print(sorted_value[-2])

#평균구하기
def mean(x):
    return sum(x)/len(x)

avg_friends = mean(num_friends)
print("평균 값")
print(avg_friends)

# 중간값을 쓰는이유. 평균의 함정때문( 한명만 연봉 100억이면 평균존나올라감)
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    mid_ponit = n //2 # //로 나누면 int가 되고 /로 나누면 float이 됨

    if (n%2==1):
        return sorted_v[mid_ponit]
    else :
        lo = mid_ponit - 1
        hi = mid_ponit
        return (sorted_v[lo] + sorted_v[hi]) / 2

median_friends = median(num_friends) 
print("중간 값")
print(median_friends)

# 산포도 ( 최대 최소 사이의 범위))
def date_range(x):
    return max(x)-min(x)
print("산포도")
print(date_range(num_friends))

# 이상치를 제외하고 평범한 데이터 사이의 범위차이
def quantile(x,p):
    p_index = int (p * len(x))
    return sorted(x)[p_index]

def interquantile_range(x):
    return quantile(x ,0.75)-quantile(x ,0.25)

print("이상치제외")
print(interquantile_range(num_friends))

'''
# 분산

def dot(v,w) :
    return sum(v_i * w_i for v,i, w_i in zip (v,w))

def sum_of_squrare(v):
    return dot(v,v)

 # 요소들과 평균의 차이. 편차
def de_mean(x) :
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(n)
    deviations = de_mean(x)
    return sum_of_squrare(deviations) / (n-1)  # n보다 n-1로 나누어야 정확히 보정됨

print("분산")
print(variance(num_friends))
'''
def dot(v,w) :
     return sum(v_i * w_i for v_i, w_i in zip (v,w))
def sum_of_squares(v) :
     return dot(v,v)
def de_mean(x) : # 요소들과 평균의 차이
     x_bar = mean(x)
     return [x_i - x_bar for x_i in x]
def variance(x) :
     n = len(x)
     deviations = de_mean(x)
     return ((sum_of_squares(deviations)) / (n-1))
      # n으로 나누기보다 n-1로 나누어야 정확하게 보정됨 (위키참조)

print("분산")
print(variance(num_friends))

# 표준편차
def standard_deviantion(x):
    return math.sqrt(variance(x))
print("표준편차")
print(standard_deviantion(num_friends))

# 공분산. 두 요소가 상관괸계가 있는가?
def covariance(x,y):
    n = len(n)
    return ((dot(de_mean(x),de_mean(y)))/(n-1))
print("공분산")
print((dot(de_mean(x),de_mean(y))))
print(covariance(num_friends,num_friends))
