# import os
# def soldier(path, file, format):
#     os.chdir(path)
#     i = 1
#     files = os.listdir(path)
#     print("Files present in directory are -",files)
#     with open(file) as f:
#         filelist = f.read().split("\n")
#         print("File after splitting new line",filelist)
#
#     for file in files:
#         if file not in filelist:
#             os.rename(file, file.capitalize())
#
#         if os.path.splitext(file)[1] == format:
#             os.rename(file, f"{i}{format}")
#             i +=1
#
# soldier(r"D:\VE",
#         r"C:\Users\ucc14\PycharmProjects\firstprog\check2.txt", ".png" )

import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    print("Files -",files)
    with open(file) as f:
        filelist = f.read().split("\n")
        print("Filelist are -",filelist)

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1

soldier(r"D:\VE",
         r"C:\Users\ucc14\PycharmProjects\firstprog\check2.txt", ".png" )
