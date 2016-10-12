# -*- coding: utf-8 -*-

#original from https://gist.github.com/nag4/ccea3b87bce3d2495bd2
from PIL import Image
from datetime import date
import os
import shutil
import filecmp

# exists src_dir/hoge.jpg, fuga.png, etc...
src_dir = u'F:\ARXEIA_ROULAS\ΦΩΤΟΓΡΑΦΙΕΣ ΑΠΟ ΡΟΥΛΑ'
# create dst_dir/yyyymmdd/
dst_dir = "e:\photos"

if os.path.exists(dst_dir) == False:
    os.mkdir(dst_dir)
print src_dir
for root, dirs, files in os.walk(src_dir):
    print root
    for filename in files:
        fullFilename = os.path.join(root,filename)
        if (filename == "desktop.ini"):
            break
        basename, extension = os.path.splitext(filename)


        try:
            image = Image.open(fullFilename)
            # 36867 : EXIF DateTimeOriginal
            xinfo = image._getexif()[36867]
            yyyy, mm = xinfo[:4], xinfo[5:7]
        except Exception as e:
            timec = os.path.getmtime(fullFilename)
            yyyy = date.fromtimestamp(timec).year
            mm   = date.fromtimestamp(timec).month

        yyyymmdd_dir = os.path.join(dst_dir, str(yyyy) + "-" + str(mm))
        if os.path.exists(yyyymmdd_dir) == False:
            os.mkdir(yyyymmdd_dir)
        dst = os.path.join(yyyymmdd_dir, filename)
        if os.path.exists(dst) == False:
            shutil.copy2(fullFilename, dst)
        elif not filecmp.cmp(dst,fullFilename):
            shutil.copy2(fullFilename,
                os.path.join(dst_dir,yyyymmdd_dir,basename+"1"+extension))
        else:
            print(dst + " exists!")
