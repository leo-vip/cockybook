# coding: UTF-8
import os, json

def getTree(path):
    rs={}
    for filename in os.listdir(path):
        print "filename :",filename
        
        tmpname=os.path.join(path,filename)
        if os.path.isdir(tmpname):
            rs[filename] = getTree(tmpname)
        else:
            justname=filename[:filename.find('.'):]
            
            if rs.has_key(justname):
                rs[justname].append(filename)
            else:
                rs[justname] = [filename]
    return rs
            
def writeMetadata(rsjson):
    ff=open("metedata.xml", mode='w')
    
    ff.write(json.dumps(rsjson,indent=4,encoding='gbk'))    
    ff.close()


def generateMetadataXml():
    rsjson=getTree('.')
    if rsjson.has_key('generate'):
        
        rsjson.pop('generate')
    
    if rsjson.has_key('metedata'):    
        rsjson.pop('metedata')
    
    writeMetadata(rsjson)

def getFile(jjson,paths):
    if len(paths)==1:
        if paths[0]=='':
            return jjson
        elif jjson.has_key(paths[0]):
            
            return jjson[paths[0]]
        else:
            print 'Jjson',json.dumps(jjson)
            print 'No this Key:', paths[0]
            return None
    elif len(paths)>1:
        return getFile(jjson[paths[0]], paths[1:])
    
if __name__ == '__main__':
    
    #generateMetadataXml()

    rsjson=json.load(open("F:/opds/metedata.xml"))
    print json.dumps(rsjson,encoding='gbk')
    print getFile(rsjson, u'/佛学'.split('/')[1:])

    pass
