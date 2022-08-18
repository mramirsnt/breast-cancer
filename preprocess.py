# import pandas as pd
# import shutil
# import glob
# import shutil
# import os
#
# xlsx_file = "./dataset/Radiology manual annotations.xlsx"
#
# df = pd.read_csv("data.csv")
# # print(df)
# df = df.rename(columns={"Pathology Classification/ Follow up":"Label"},errors="raise")
# df = df.replace(["Benign","Malignant","Normal"],["2","1","0"])
# # print(df.groupby("Label").size())
# # print(df.groupby(["Label","Type"]).size())
# sd = df.groupby(["Label","Type"])["Image_name"]
# cs0 = []
# cs1 = []
# cs2 =[]
# dm0 = []
# dm1 = []
# dm2 =[]
# for key,value in sd:
#
#     if key[0] == '0' and key[1] == "CESM":
#         for i in value:
#             cs0.append(i)
#     if key[0] == '1' and key[1] == "CESM":
#         for i in value:
#             cs1.append(i)
#     if key[0] == '2' and key[1] == "CESM":
#         for i in value:
#             cs2.append(i)
#     if key[0] == '0' and key[1] == "DM":
#         for i in value:
#             dm0.append(i)
#     if key[0] == '1' and key[1] == "DM":
#         for i in value:
#             dm1.append(i)
#     if key[0] == '2' and key[1] == "DM":
#         for i in value:
#             dm2.append(i)
#     # print("key is ",key,"\n")
#     # print("vlaue",value)
#
#
#
# l =[]
# for i in dm2:
#     l.append('/home/amirsanati/PycharmProjects/pythonProject/dataset/low/'+i+'.jpg')
base_dir = '/home/amirsanati/PycharmProjects/pythonProject/dataset/'
# src_dir = "your/source/dir"
# dst_dir = "./dataset/dm/2/"
# # print(len(cs0))
# # for jpgfile in glob.iglob(os.path.join(base_dir, "*.jpg")):
# #     # print(jpgfile)
# #     if jpgfile in l:
# #         print(jpgfile)
# #         shutil.copy(jpgfile, dst_dir)
#
#
#
#
#
#
