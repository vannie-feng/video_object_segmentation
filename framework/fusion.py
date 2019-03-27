#!usr/bin/python2.7

import PIL
import cv2 
import PIL.Image as Image
import os

#blackimg=Image.open('black.png')
#blackimg=blackimg.convert('RGBA')
def transparent (img):
    img=img.convert('RGBA')
    L,H = img.size
    color_0=(0,0,0,255)
    for h in range(H):
        for l in range(L):
            a=img.getpixel((l,h))
            if(a==color_0):
                color_1=a[:-1]+(0,)
                img.putpixel((l,h),color)
    return img

def fusion(forimg,backimg,alpha):
    imgf=forimg.convert('RGBA')
    mask=alpha.convert('RGBA')
    imgb=backimg.convert('RGBA')
    L,H = imgf.size
    lb,hb=backimg.size
    color_0=(0,0,0,255)
    #color_0=blackimg.getpixel((0,0))
    for h in range(H):
        for l in range(L):
            if(mask.getpixel((l,h))==color_0):
              #  color_1=a[:-1]+(0,)
                if (l<lb) and (h<hb):
                    color=imgb.getpixel((l,h))
                else:
                    color=color_0
                imgf.putpixel((l,h),color)
    return imgf

if __name__=='__main__':
    forpath='./DAVIS/JPEGImages/Full-Resolution/'
    maskpath='./OSVOS-PyTorch/models/Results/'
    i=0
    backimg=Image.open('./back.jpg')
    savepath='./Fusion/'
    videoname='car-shadow/'
    savepath=savepath+videoname
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    print ("savepath: "+savepath)
    for mask in os.listdir(maskpath+videoname):
        filename=mask.split(".")
        print filename
        if (filename[-1]!='png'):
            continue
        filename=filename[0]
        mask=Image.open(maskpath+videoname+"./"+mask)
      #  fe=Image.open(forpath+ '{:05d}.jpg'.format(i))
        fe = Image.open(forpath+ videoname+filename+'.jpg')
        new_image=fusion(fe,backimg,mask)
        print "here"
        new_image.save(savepath+filename+'.png')
        print(savepath+filename+": done")

