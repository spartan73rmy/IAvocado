#Rename images on path
import os
path='Images'
imagesToRename = os.listdir(path)
for i,file in enumerate(imagesToRename):
  os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(i), '.jpg'])))
