import sys, os, Image

imgpath = '.'
for file in os.listdir(imgpath):
    if os.path.splitext(file)[1] == '.png':
        
        # Load into memory (we'll need pixel access)
        currimg = Image.open(file)
        currpix = currimg.load()
        
        # Look for non-black pixels from top, but not too far
        for i in range(0, 50):
            if not sum(currpix[0, i][:-1]):
                break
        upperbox = i
        
        # Look for non-black pixels from bottom, but not too far
        for i in range(currimg.size[1]-1, currimg.size[1]-30, -1):
            if not sum(currpix[0, i][:-1]):
                break
        lowerbox = i
        
        box = (0, upperbox, currimg.size[0]-1, lowerbox)
        print box
        
        currimg.crop(box).save('cropped_'+file)
    