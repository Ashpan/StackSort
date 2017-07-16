from classes import Stack
#This version of task 2 uses a selection sort kind of approach
def stacksort(cs):
    final = Stack()
    temp = Stack()
    temp.push(1) #I have to do this so it will go into the while loop underneath
    while not cs.is_empty() and not temp.is_empty(): #This while loop stops when I have nothing left in either loop, this happens when all the elements are in the 'final' stack
        a = cs.pop() #Pop the first value of cs into a
        temp = Stack() #Clear this stack
        while not cs.is_empty(): #this will take 2 values and compare them to each other and look for the smallest number
            b = cs.pop() #Pop another value from cs into b
            if a<b or a==b: #look for the smaller value
                temp.push(b) #if a is smaller, continue on to compare a to all the other remaining values
            else:
                temp.push(a) #otherwise push a into the temp stack and set the value of a to b
                a = b
        final.push(a) #after it finds the smallest value, push that into the final stack
        while not temp.is_empty(): #push all the values from temp into cs
            cs.push(temp.pop())
        temp.push(1) #I have to do this so it will go into the while loop once again
    the_final = Stack()
    while not final.is_empty():
        the_final.push(final.pop())
    return the_final
