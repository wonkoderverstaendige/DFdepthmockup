import sys, os, Image, hashlib
import numpy as np


imgpath = 'img\\2'
tilesize = 16
tiles = []

class growingdict(dict):
    def __missing__(self, key):
        self[key] = len(self) + 1
        return self[key]

tiledict = growingdict()
imgdict = dict()

for file in os.listdir(imgpath):
    if os.path.splitext(file)[1] == '.png':
        im = Image.open(os.path.join(imgpath, file))

        w, h = im.size
        
        # +1 because I screwed up cropping, delete these later!!!
        #if not ((w % tilesize) + (h % tilesize)) == 0:
        if not ((w+1)%tilesize + (h+1)%tilesize) == 0:
            print "Image "+file+" size not multiple of " + str(tilesize)
            print "X: "+str(((w+1.)/tilesize))+" Y: "+str((h+1.)/tilesize)
            
        else:
            n_vert_tiles = (w+1)/tilesize
            n_hori_tiles = (h+1)/tilesize

            # ignore first/last column/line when looping, only get "content", not frame
            for tx in range(1, n_hori_tiles-1):
                for ty in range(1, n_vert_tiles-1):
                    newtile = im.crop((tx * tilesize, ty * tilesize, tx * tilesize + tilesize, ty * tilesize + tilesize))
                    
                    imgdict[tiledict[hashlib.md5(newtile.tostring()).hexdigest()]] = newtile
                    
print len(tiledict)
t = 0
for tileimgkey in imgdict:
    print os.path.join(imgpath, 'tiles', str(t))
    imgdict[tileimgkey].save(os.path.join(imgpath, 'tiles', str(t)+'.png'),'PNG')
    t += 1