import sys, os, Image

imgpath = '.'
for file in os.listdir(imgpath):
    if os.path.splitext(file)[1] == '.png':
        
        # Load into memory (we'll need pixel access)
        currimg = Image.open(file)
        currpix = currimg.load()
        width = currimg.size[0]
        height = currimg.size[1]
        
        box = [0, 0, width-1, height-1]
        print box
        
        # LEFT
        for i in range(0, 16):
            if sum(currpix[i, height/2][:-1]):
                break
        box[0] = i          

        # TOP
        for i in range(0, 16):
            if sum(currpix[width/2, i][:-1]):
                break
        box[1] = i
        
        # RIGHT
        for i in range(width-1, width-16, -1):
            if sum(currpix[i, height/2][:-1]):
                break
        box[2] = i         
        
        # BOTTOM
        for i in range(height-1, height-16, -1):
            if sum(currpix[width/2, i][:-1]):
                break
        box[3] = i        
        
        print box
        
        currimg.crop(box).save('1_'+file)
    