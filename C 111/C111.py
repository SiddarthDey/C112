import os
import shutil


path="C:/Users/deyde/OneDrive/Desktop/python/C111/Dog-walk.gif"
root,extn=os.path.splitext(path)
print(root)
print(extn)

path1="C:/Users/deyde/OneDrive/Desktop/python"
result=os.path.exists(path1)
print(result)
print(os.listdir(path1))
print(os.getcwd())


source="C:/Users/deyde/OneDrive/Desktop/python/C 111/Dog-walk.gif"
destination="C:/Users/deyde/OneDrive/Desktop/python/C110/Dog-walk.gif"

shutil.copy(source,destination)