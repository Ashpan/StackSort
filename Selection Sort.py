from classes import Stack
def stacksort(cs):
    ss = Stack() #Small Stack
    bs = Stack() #Big Stack
    while not cs.is_empty(): #if the current stack is not empty
        new = cs.pop()
        placed = False
        while(not placed): #placed represents whether or not the new variable has been placed into a stack
            if ss.is_empty(): #if small stack is empty
                if bs.is_empty(): #and big stack is empty
                    ss.push(new) #push new into small stack
                    placed = True #end the while loop and start with the next value in the cs
                else: #ss is empty but bs is not
                    big = bs.pop()
                    if(new>big): #if the value from cs is bigger than bs
                        ss.push(big) #put the bs value at the top of ss
                    else:
                        bs.push(big) #otherwise push it back into bs
                        bs.push(new) #and then push new on top of it
                        placed = True #end while loops
            else: #if ss is not empty
                small = ss.pop()
                if(new<small): #if cs value is less than ss value
                    bs.push(small) #put ss value into bs and then restart the loop
                else:
                    ss.push(small) #otherwise put small back into ss
                    if bs.is_empty():
                        bs.push(new) #and if bs is empty put new into bs
                        placed=True  #end loop
                    else:
                        big = bs.pop() #if bs isn't empty
                        if(new>big): #and if cs value is bigger than bs value
                            ss.push(big) #put bs value into ss
                        else:
                            bs.push(big) #if cs value is smaller than bs value push big then new in that order
                            bs.push(new)
                            placed =True #end loop

    while not bs.is_empty():
        a = bs.pop()
        ss.push(a)
    while not ss.is_empty():
        a = ss.pop()
        cs.push(a)
    return cs
