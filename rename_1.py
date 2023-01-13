import os
from datetime import datetime

from PIL import Image

now = datetime.now()
current_time = now.strftime("%d-%m-%Y-%H-%M-%S")
os.mkdir('webp_'+current_time)

for filename in os.listdir("."):
    if filename.endswith("jpg") or filename.endswith("png") or filename.endswith("jpeg"):
        image = Image.open(filename)
        image = image.convert('RGB')
        image.save('webp_'+current_time+'/'+filename.split(".")[0]+'.webp', 'webp', optimize = True, quality = 100)