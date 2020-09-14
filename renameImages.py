#Rename images, change path in it 

import os
path='testing/'
imagesToRename = os.listdir(path)
for i,file in enumerate(imagesToRename):
  os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(i), '.jpg'])))
