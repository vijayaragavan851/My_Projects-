from turtle import st
import numpy as np
alp_code = {' ':0,'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
enc_code = {'AQ': 0, 'AW':1, 'AE':2, 'AR':3, 'AT':4,'AY':5,'AU':6, 'AI':7, 'AO':8, 'AP':9,'AA':10,
            'AS':11, 'AD':12, 'AF':13, 'AG':14,'AH':15,'AJ':16, 'AK':17, 'AL':18, 'AZ':19,'AX':20,
            'AC':21, 'AV':22, 'AB':23, 'AN':24,'AM':25,'BA':26, 'BN':27, 'BH':28, 'BK':29,'BL':30,
            'BC':31, 'BT':32, 'BD':33, 'BX':34,'BZ':35,'BV':36, 'BS':37, 'BJ':38, 'BP':39,'RR':40,
            'BQ':41, 'BI':42, 'BR':43, 'CA':44,'CZ':45,'CT':46, 'CY':47, 'CU':48, 'CI':49,'CP':50,
            'CO':51, 'CH':52, 'CK':53, 'CV':54,'CB':55,'CM':56, 'CN':57, 'CQ':58, 'CG':59,'CE':60,
            'CF':61, 'CR':62, 'DQ':63, 'DG':64,'DT':65,'DZ':66, 'DJ':67, 'DU':68, 'DO':69,'DP':70,'DM':71, 'DN':72, 'DS':73, 'DL':74,'DV':75,'EA':76, 'ER':77, 'ET':78, 'EU':79,'EO':80,'EP':81, 'EG':82, 'EW':83, 'EL':84,'FO':85,'FG':86, 'FH':87, 'FN':88, 'FP':89,'FQ':90,'FT':91, 'FD':92, 'FZ':93, 'GT':94,'GY':95,'GU':96, 'GI':97, 'GZ':98, 'GX':99,'GC':100,'GH':101,'GI':102,'GU':103,'GK':104} #hash dictinonary

def encryption(): #this function will encrypt the data
    #private key matrix
    a = np.array([[1,1,1],[2,1,0],[1,0,0]])
    message =  input("Enter your message:").upper() #getting the input from user
    mess_len = len(message)
    new_str = message
    if (mess_len % 3) == 0:
        pass
    elif (mess_len % 3) == 1:
        new_str += '  '
    elif (mess_len % 3) == 2:
        new_str += ' ' #assigning the extra values to match the matrix
    new_str_code = []
    for i in new_str: new_str_code.append(alp_code.get(i)) #getting the coressponding numbers from alpha code and storing it in array
    nested_code = []
    nested_code = [new_str_code[i : i+3] for i in range(0,len(new_str_code) , 3)]
    #print(nested_code)
    nested_array = np.array(nested_code) #formating the array to nx3 matrix
    #print(nested_array)
    #converting the message into encrypt message
    sam = nested_array.dot(a).tolist()
    #print(sam)
    sin_digits = []
    #printing the single array elements
    for sub in sam:
        for val in sub:
            sin_digits.append(val)
    #printing the final output!
    print("Your Hash code is: ",end="")
    string = ''
    for i in sin_digits :
        string += get_key(i, 1)
        #output
    print(string)
    code_choice()

def get_key(val, val1): #this is for encryption
    if(val1 == 1):
        for key, value in enc_code.items():
            if val == value:
                return key
    else:
        for key, value in alp_code.items():
            if val == value:
                return key

def decryption(mats):

    n = mats.shape[0] #getting the row value
    m = 3
    matrx = mats
    array_matrx =  np.array(matrx)
    result = [[0 for i in range(m)] for j in range(n)]
    #private inverse Key
    a_inverse = [[0,0,1],[0,1,-2],[1,-1,1]]
    #For loop to multiply the inverse with encrypted matrix
    result = array_matrx.dot(a_inverse).tolist()
    result = np.array(result)
    #print("The final decrypted matrix is:",result)
    string = ''
    for i in result:
        for j in i:
            string += get_key(j, 2)
    string1 = string.lower()        
    print("Your Decrypted message:", string1)
    code_choice()

def my_dec():
    message =  input("Enter the hash code:")
    K = 2
    res = [message[idx : idx + K] for idx in range(0, len(message), K)]
    new_str_code = []
    for f in res: new_str_code.append(enc_code.get(f))
    nested_code = []
    nested_code = [new_str_code[i : i+3] for i in range(0,len(new_str_code) , 3)]
    nested_array = np.array(nested_code) #formatting the nx3 matrix
    #passing the value to decryption array
    decryption(nested_array)

def code_choice():
    print("\n-:Welcome Sir,select your choice:-\n")
    print("\n1)Encryption.\n2)Decryption.\n3)Exit\n")
    choice  = int(input("Enter your choice:"))
    if choice == 1:
        encryption()
    elif choice == 2:
        my_dec()
    elif choice == 3:
        exit()
    else:
        print("Invalid choice")
        code_choice()
code_choice()
