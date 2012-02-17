import sys, os, Image

imgpath = 'img\\2'
tilesize = 16

for file in os.listdir(imgpath):
    if os.path.splitext(file)[1] == '.png':
        im = Image.open(os.path.join(imgpath, file))
        width = im.size[0]
        height = im.size[1]
        
        w, h = im.size
        
        if not ((w+1)%tilesize + (h+1)%tilesize) == 0:
            print "Image "+file+" size not multiple of " + str(tilesize)
            print "X: "+str(((w+1.)/tilesize))+" Y: "+str((h+1.)/tilesize)
            
        else:
            n_vert_tiles = (w+1)/tilesize
            n_hori_tiles = (h+1)/tilesize

            for tx in range(0, n_hori_tiles):
                for ty in range(0, n_vert_tiles):
                    newtile = im.crop((tx * tilesize, ty * tilesize, tx * tilesize + tilesize, ty * tilesize + tilesize))
                    tile.save(os.path.join(imgpath, str(tx) + "-" + str(ty) + "_" + file))
                