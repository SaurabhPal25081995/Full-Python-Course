# By using normal method
l1=["Aloo","Bhindi","Laduki","Khoya"]
# i=0
# for item in l1:
#     if i%2==0:
#         print(f"Now left items are {item}")
#     i+=1

# By using enumerate
l1=["Aloo","Bhindi","Laduki","Khoya"]
for index,item in enumerate(l1):
        print(f"Now {item} is place on {index} position")
        