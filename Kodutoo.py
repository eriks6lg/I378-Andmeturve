from Crypto.Cipher import AES

def to_binary(byte_type):
    
    binary_type = ((byte_type[0] ) << 8) + byte_type[1] 
    binary_type = (binary_type << 8) + byte_type[2] 
    binary_type = (binary_type << 8) + byte_type[3] 
    binary_type = (binary_type << 8) + byte_type[4] 
    binary_type = (binary_type << 8) + byte_type[5] 
    binary_type = (binary_type << 8) + byte_type[6] 
    binary_type = (binary_type << 8) + byte_type[7] 
    binary_type = (binary_type << 8) + byte_type[8] 
    binary_type = (binary_type << 8) + byte_type[9] 
    binary_type = (binary_type << 8) + byte_type[10] 
    binary_type = (binary_type << 8) + byte_type[11] 
    binary_type = (binary_type << 8) + byte_type[12] 
    binary_type = (binary_type << 8) + byte_type[13] 
    binary_type = (binary_type << 8) + byte_type[14] 
    binary_type = (binary_type << 8) + byte_type[15] 
    binary_type = (binary_type << 8) + byte_type[16] 
    binary_type = (binary_type << 8) + byte_type[17] 
    binary_type = (binary_type << 8) + byte_type[18] 
    binary_type = (binary_type << 8) + byte_type[19] 
    binary_type = (binary_type << 8) + byte_type[20] 
    binary_type = (binary_type << 8) + byte_type[21] 
    binary_type = (binary_type << 8) + byte_type[22] 
    binary_type = (binary_type << 8) + byte_type[23]
    
    
    return binary_type

def to_list(binary_type):

    list_type = list()
    
    list_type.append(binary_type >> 184)
    list_type.append((binary_type >> 176) - ((binary_type >> 184) << 8))
    list_type.append((binary_type >> 168) - ((binary_type >> 176) << 8))
    list_type.append((binary_type >> 160) - ((binary_type >> 168) << 8))
    list_type.append((binary_type >> 152) - ((binary_type >> 160) << 8))
    list_type.append((binary_type >> 144) - ((binary_type >> 152) << 8))
    list_type.append((binary_type >> 136) - ((binary_type >> 144) << 8))
    list_type.append((binary_type >> 128) - ((binary_type >> 136) << 8))
    list_type.append((binary_type >> 120) - ((binary_type >> 128) << 8))
    list_type.append((binary_type >> 112) - ((binary_type >> 120) << 8))
    list_type.append((binary_type >> 104) - ((binary_type >> 112) << 8))
    list_type.append((binary_type >> 96) - ((binary_type >> 104) << 8))
    list_type.append((binary_type >> 88) - ((binary_type >> 96) << 8))
    list_type.append((binary_type >> 80) - ((binary_type >> 88) << 8))
    list_type.append((binary_type >> 72) - ((binary_type >> 80) << 8))
    list_type.append((binary_type >> 64) - ((binary_type >> 72) << 8))
    list_type.append((binary_type >> 56) - ((binary_type >> 64) << 8))
    list_type.append((binary_type >> 48) - ((binary_type >> 56) << 8))
    list_type.append((binary_type >> 40) - ((binary_type >> 48) << 8))
    list_type.append((binary_type >> 32) - ((binary_type >> 40) << 8))
    list_type.append((binary_type >> 24) - ((binary_type >> 32) << 8))
    list_type.append((binary_type >> 16) - ((binary_type >> 24) << 8))
    list_type.append((binary_type >> 8) - ((binary_type >> 16) << 8))
    list_type.append((binary_type) - ((binary_type >> 8) << 8))
    
    return list_type


obj = AES.new('aaaaaaaaaaaaaaaaaaaa0825', 3, '0000000000000000')

plaintext = to_list(0b0)
is_found = False
tries = 0


while (not is_found):
    cyphertext = obj.encrypt(bytes(plaintext))
    cypherbinary = to_binary(cyphertext)
    tries += 1
    
    multiplication = cypherbinary & 0b111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111100000000000000000000

    if multiplication == cypherbinary:
        is_found = True
        
        print("Number of encryptions: ")
        print(tries)
        print("\n")
        print("Plaintext in binary:")
        print(bin(binary_type))
        print("\n")
        print("Cyphertext in binary")
        print(bin(cypherbinary))
        
        continue
    
    plaintextbinary = to_binary(bytes(plaintext))
    plaintextbinary += 0b100000000000000000000
    
    print(bin(plaintextbinary))
    
    plaintext = to_list(plaintextbinary)
    
    
    
    
