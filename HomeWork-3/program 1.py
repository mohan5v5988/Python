def bunny_ears(par) :
    if (par < 1) :
        return 0
    elif ( par%2 == 0 ) :
        return bunny_ears(par-1) + 3
    else :
        return bunny_ears(par-1) + 2

print("bunny_ears(0) -> "+str(bunny_ears(0)))
print("bunny_ears(1) -> "+str(bunny_ears(1)))
print("bunny_ears(2) -> "+str(bunny_ears(2)))
print("bunny_ears(3) -> "+str(bunny_ears(3)))