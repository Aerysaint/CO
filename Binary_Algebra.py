def seven_bit_convertor(num):
    num = str(num)
    if len(num) <7:
        num = num[::-1]
        while(len(num) < 7):
            num += "0"
    num = num[::-1]
    return num

def binary_to_decimal(num):
    num = str(num)
    digits = list(num)
    digits.reverse()
    sum = 0
    for i in range(len(digits)):
        sum += (2**i)*int(digits[i])
    return int(sum) # An integer

def decimal_to_binary(num):
    if (int(num) == 0):
        return 0
    bin = ""
    while (int(num) > 0):
        bin += str(int(num)%2)
        num = str(int(num)//2)
    a = list(bin)
    a.reverse()
    b = ''.join(a)
    return (b) # A string

def one_comp(decimal_num):
    binary_num = decimal_to_binary(decimal_num)
    #binary_num = str(binary_num)
    lst = list(binary_num)
    for i in range(len(lst)):
        if (lst[i] == "1"):
            lst[i] = "0"
        elif (lst[i] == "0"):
            lst[i] = "1"
    num = ''.join(lst)
    return (num) #A string

def binary_addition(num1, num2):
    # I'm asuming dono numbers binary me hain
    num1 = list(str((num1)))
    num2 = list(str((num2)))
    # print(num1)
    # print(num2)
    num1.reverse()
    num2.reverse()
    index = max(len(num1), len(num2))
    sum = ""
    carry = 0
    for i in range(index):
        dig_sum = (carry + int(num1[i]) + int(num2[i]))
        if (dig_sum == 0):
            sum += "0"
            carry = 0
        elif (dig_sum == 1):
            sum += "1"
            carry = 0
        elif (dig_sum == 2):
            sum += "0"
            carry = 1
        elif (dig_sum == 3):
            sum += "1"
            carry = 1
    sum += str(carry)
    sum = sum[::-1]
    return int(sum)
        
#print(binary_addition(1011,1011))




def two_comp(decimal_num):
    binary_num = decimal_to_binary(decimal_num)
    ones_comp = one_comp(binary_num)
    print(ones_comp)
    twos_comp = binary_addition(ones_comp, 1)
    return (twos_comp)

#print(two_comp(1))



    
