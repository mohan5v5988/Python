import  os

def findfile(p , fi ) :
    allFiles = os.listdir(p)
    di = []
    files = []
    r = []
    for a in allFiles :
        if os.path.isdir( os.path.join( p , a ) ) :
            di.append(a)
        else :
            files.append(a)
    for b in files :
        if b == fi :
            return str( os.path.join( p ) )
    for c in di :
        r.append(findfile( os.path.join( p , c ) , fi))
    return r

z = input("path : ")
y = input("file : ")
print( findfile(z,y) )