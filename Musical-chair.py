import random  
num = int(input("Please enter the number of participants: "))
circ = []
for i in range(1, num+1):
    print("Please enter the name of the participant ", i, ": ", sep = "", end = "")
    name = input() 
    circ.append(name)
print()
total = len(circ)

def musicalGame(a, size): 
    i = 1 
    count = 1
    print("Elimination round winners: ")
    while(i > 0):                      #infinite loop
        num = random.randint(0,4)       #random number        
            
        if(num == 1):                  #removing n/2 
            x = int(size/2) 
            circ[x] = 0                 #making n/2 -> 0
            while(x < len(circ) - 1):            
                temp = circ[x]    
                circ[x] = circ[x+1] 
                circ[x+1] = temp
                x += 1                   
            size -= 1
            
            y = 0                       #round winners
            print("Round", count, ": ", end = " ") 
            while(y < size):
                print(circ[y], end = " ") 
                y += 1
            count += 1 
            print()
             
        else:                          #rotating right
            j = size - 1
            temp = circ[j] 
            while(j > 0): 
                circ[j] = circ[j-1]
                j -= 1
            circ[0] = temp
                
        if(size == 1):
            return circ[0]
        i += 1      
   
result = musicalGame(circ, total)
print("Final winner:", result) 

input("Press 'Enter' to close the program :")

