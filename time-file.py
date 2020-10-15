import time

import datetime as dt

a = dt.datetime(2013,12,30,23,59,59)
b = dt.datetime(2013,12,31,23,59,59)

print("Remaining seocnds----",(b-a).total_seconds())

epoch = time.time()
print("initial is Epoch time ",epoch)

current_time=time.ctime(epoch)
print("Current Time-",current_time)

result = time.localtime(epoch)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)


localtime = time.asctime(time.localtime(time.time()))
print("Current time is",localtime)
print("---------------------------------------")



initial = time.time()
print("Initial is ",initial)
k =0
while(k<2):
    print("This is while loop")
    k+=1
    print(initial)
print("While loop ran in -",time.time()-initial)

print("-----------------",time.gmtime(0)) # To check Epoch

initial2 = time.time()
for i in range(5):
    print("This is for loop")
print("For loop ran in -",time.time()-initial2)

localtime = time.asctime(time.localtime(time.time()))
print("Localtime is --- ",localtime)
result = time.gmtime(1545925769)
print("Result-",result)

# Print after wait 1 sec
# initial = time.time()
# k =0
# while(k<4):
#     print("This is while loop")
#     k+=1
#     time.sleep(1)
# print("While loop ran in -",time.time()-initial)