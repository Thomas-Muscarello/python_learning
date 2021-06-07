#Allow us to take a number and raise it to a power
print(2**3)
#prints 2 to the 3rd power

def raise_to_power(base_num, pow_num):
    #var to store info
    ans=1
    #multiply base num as many as there are pow num
                #loop from 0-#b4 pow_num; Example if pow num = 4
                #loop woul go from 0, 1, 2, 3
    for index in range(pow_num):
        ans= ans*base_num
    return ans

print(raise_to_power(3,2))
