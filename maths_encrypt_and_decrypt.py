import numpy as np
a = np.array([[1,-1,1],[2,-1,0],[1,0,0]])
alp_code = {' ':0,'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
     'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,
     'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def encryption():
    message =  input("Enter your message:").upper()
    mess_len = len(message)
    new_str = message

    if (mess_len % 3) == 0:
        pass
    elif (mess_len % 3) == 1:
        new_str += '  '
    elif (mess_len % 3) == 2:
        new_str += ' '
 
    new_str_code = []

    for i in new_str:
        new_str_code.append(alp_code.get(i))
    temp = new_str_code
    nested_code = []
    len_temp = len(temp)

    for i in range(1,len_temp+1,3):
        b = []

        for j in range(3):
           b.append(temp[j])
           if len(b) == 3:
             nested_code.append(b)        

        for k in b:
           temp.remove(k)

    nested_array = np.array(nested_code)

    for i in nested_array:
        print(i.dot(a))
        
def decryption():

    n = int(input("Enter the number of rows:"))
    m = 3
    matrx = []

    for i in range(1,n+1):
       matrx2 = []
       
       for j in range(1,m+1):
           num = int(input("Enter the number:"))
           matrx2.append(num)
           if len(matrx2) == 3:
              matrx.append(matrx2)

    result = [[0 for i in range(m)] for j in range(n)]
    
    a_inverse = [[0,0,1],[0,-1,2],[1,-1,1]]

    for i in range(len(matrx)):
 
        for j in range(len(a_inverse[0])):
        
            for k in range(len(a_inverse)):
               result[i][j] += matrx[i][k] * a_inverse[k][j]

    print(result)
    def get_key(val):
        for key, value in alp_code.items():
            if val == value:
               return key
    string = ''
    for i in result:
        for j in i:
            string += get_key(j)
    print("your decrypted message is",string)        
        
  

def code_choice():
    print("press for 1 Encryption.\npress 2 for Decryption.")
    choice  = int(input("Enter your choice:"))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Invalid choice")
code_choice()        
