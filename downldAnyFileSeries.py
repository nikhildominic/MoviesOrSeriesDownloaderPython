import urllib2
skipped = []
for i in range(0,16):
    skipper=[1]
    if(i+1 in skipper):
        continue
    url = "http://79.127.126.110/Serial/Breaking%20Bad/S05/720p/"
    ll= 2-len(str(i+1))
    pre='0'*ll+str(i+1)
    #Breaking.Bad.S05E01.BluRay.720p.x264.mkv
    fname="Breaking.Bad.S05E"+pre+".BluRay.720p.x264.mkv"    
    url=url+fname
    print url
    try:
        file_name = url.split('/')[-1]
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Size %sMB" % (file_name, file_size/1000000)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            print fname, " ",file_size_dl ,"/", file_size , " ", round((float(file_size_dl)/float(file_size))*100.0,2),"% ","\r",
            f.write(buffer)
        f.close()
        print ''
    except:
        skipped.append(pre)
        print 'could not find the file'
        pass
print "Skipped:"+skipped