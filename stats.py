# # mean,median,mode
# N = int(input().strip())
# N1 = input().split()
# N2 = list(map(int,N1))
# print(round(sum(N2)/N,1))
# N2.sort()
# if len(N2)%2!=0:
#     print(N2[ceil(len(N2)/2)-1])
# else:
#     i = int((len(N2)/2)-1)
#     j = i+1
#     print(round((N2[i]+N2[j])/2,1))

# d = {}
# for i in N2:
#     d[i] = N2.count(i)

# res = all(ele == 1 for ele in d.values())
# if res:
#     print(str(list(d.keys())[0]))
# else:
#     print(max(d,key=d.get))

# #Weighted mean
# x = [10, 40, 30, 50, 20]
# y = [1, 2, 3, 4, 5]
# sum1 = 0
# for i,j in zip(x,y):
#     sum1 += i*j
# wm = round(sum1/sum(y),1)
# print(wm)

# Std 
# arr =[10, 40, 30, 50, 20]
# m = round(sum(arr)/len(arr),1)
# print(m)
# sum1 = 0
# for i in arr:
#     tmp = (i-m)**2
#     sum1 += (tmp)
# print(sum1)
# std1 = round((sum1/len(arr))**0.5,1)
# print(std1)

# Quartile
arr = [3,7,8,5,12,14,21,15,18,14]

# arr.sort()
# if len(arr)%2!=0:
#     tmp = (len(arr)//2)
#     median = arr[tmp]
#     l_l = arr[:tmp]
#     u_l = arr[tmp+1:]
#     t1 = len(l_l)//2
#     t3 = len(u_l)//2
#     q1 =  int((l_l[t1-1]+l_l[t1])/2)
#     q2 = median
#     q3 =  int((u_l[t3-1]+u_l[t3])/2)
#     print(q1)
#     print(q2)
#     print(q3)
# else:
#     tmp1 = len(arr)//2
#     median = int(round((arr[tmp1]+arr[tmp1-1])/2,1))
#     l_l = arr[:tmp1]
#     u_l = arr[tmp1:]
#     print(l_l,median,u_l)
#     if len(u_l)%2==0:
#         t1 = len(l_l)//2
#         t3 = len(u_l)//2
#         q1 =  int((l_l[t1-1]+l_l[t1])/2)
#         q2 = median
#         q3 =  int((u_l[t3-1]+u_l[t3])/2)
#         print(q1)
#         print(q2)
#         print(q3)
#     else:
#         t1 = len(l_l)//2
#         t3 = len(u_l)//2
#         q1 =  l_l[t1]
#         q2 = median
#         q3 =  u_l[t3]
#         print(q1)
#         print(q2)
#         print(q3)

# IQR
s = "10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10".split()
f = "1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20".split()
values = list(map(int,s))
freqs = list(map(int,f))
s = [] 
for i,j in zip(values,freqs):
    s.append([i]*j) 

S = [ele for li in s for ele in li]
S.sort()

if len(S)%2==0:
    t1 = len(S)//2
    l_l = S[:t1]
    u_l = S[t1:]
    if len(l_l)%2==0 and len(u_l)%2==0:
        t1_1 = len(l_l)//2
        t3_1 = len(u_l)//2
        q1 = round((l_l[t1_1-1]+l_l[t1_1])/2,1)
        q3 = round((u_l[t3_1-1]+u_l[t3_1])/2,1)
        iqr = round(q3-q1,1)
        print(iqr)
    else:
        t1_1 = len(l_l)//2
        t3_1 = len(u_l)//2
        q1 = float(l_l[t1_1])
        q3 = float(u_l[t3_1])
        iqr = float(q3-q1)
        print(iqr)
else:
    t1 = len(S)//2
    l_l = S[:t1]
    u_l = S[t1+1:]
    if len(l_l)%2==0 and len(u_l)%2==0:
        t1_1 = len(l_l)//2
        t3_1 = len(u_l)//2
        q1 = round((l_l[t1_1-1]+l_l[t1_1])/2,1)
        q3 = round((u_l[t3_1-1]+u_l[t3_1])/2,1)
        iqr = round(q3-q1,1)
        print(iqr)
    else:
        t1_1 = len(l_l)//2
        t3_1 = len(u_l)//2
        q1 = float(l_l[t1_1])
        q3 = float(u_l[t3_1])
        iqr = float(q3-q1)
        print(iqr)