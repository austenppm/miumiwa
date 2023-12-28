# chokin = ganpon = 100000
# kinri = 0.05
# for i in range(20):
#     chokin = chokin + chokin * kinri
#     if chokin > ganpon * 2.0:
#         print("Excellent")
#     elif chokin > ganpon * 1.5:
#         print("Nice")
#     else:
#         print("Not yet")
        
# print(int(chokin))

# chokin = ganpon = 100000
# kinri = 0.05
# for year in range(50):
#     if year % 2 == 0:
#         continue
#     chokin = chokin + chokin * kinri
#     if chokin > ganpon * 1.5:
#         break
    
# print(int(chokin), year)


# chokin = ganpon = 100000
# kinri = 0.02
# year = 0

# while chokin < ganpon * 2:
#     chokin = chokin + chokin * kinri
#     year += 1
    
# print(int(chokin), year)

chokin = ganpon = 100000
kinri = 0.02
year = 0

while True:
    chokin = chokin + chokin * kinri
    year += 1
    print(int(chokin), year)
    if chokin > ganpon * 2 :
        break
    # print(int(chokin), year)
    
# print("This is the current " , int(chokin), year)
        
# while chokin < ganpon * 2 :
#     print(int(chokin), year)
#     chokin = chokin + chokin * kinri
#     year += 1    
    
# print(int(chokin), year)