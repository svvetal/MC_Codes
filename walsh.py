import numpy as np

# Function to generate Walsh matrix 
def generate_walsh_matrix(n):
    if n == 1:
        return np.array([[1, 1], [1, -1]]) 
    else:
        prev_matrix = generate_walsh_matrix(n-1)
        upper = np.concatenate((prev_matrix, prev_matrix), axis=1) 
        lower = np.concatenate((prev_matrix, -prev_matrix), axis=1) 
        return np.concatenate((upper, lower), axis=0)
# Function to encode data using CDMA technique 
def cdma_encode(data_bits, walsh_matrix):
    encoded = np.zeros_like(walsh_matrix[0]) 
    for i, bit in enumerate(data_bits):
        encoded += bit * walsh_matrix[i] 
    return encoded 

# Function to decode a specific channel in CDMA

def cdma_decode(encoded_data, walsh_matrix, channel):
    decoded = np.dot(encoded_data, walsh_matrix[channel]) / len(walsh_matrix[channel]) 
    return decoded

# Get number of data bits from user
num_bits = int(input("Enter the number of data bits: "))

# Get data bits from user 
data_bits = []
print("Enter the data bits:") 
for i in range(num_bits):
    bit = int(input(f"Enter bit {i + 1}: ")) 
    data_bits.append(bit)
#Defining 
x=1
while (2**x<num_bits):
    x=x+1

# Generate Walsh matrix
walsh = generate_walsh_matrix(x) 
np.set_printoptions(threshold=np.inf) # Set printing options 
print("\nGenerated Walsh Matrix:")
print(walsh)

# Encode data using CDMA technique 
encoded_data = cdma_encode(data_bits, walsh)

# Get channel to decode from user
decode_channel = int(input(f"\nEnter the channel to decode (0 - {num_bits - 1}): "))

# Decode the selected channel
decoded_channel = cdma_decode(encoded_data, walsh, decode_channel) 
print(f"\nEncoded data: {encoded_data}")
print(f"Decoded data from channel {decode_channel}: {decoded_channel}") 
print(f"Input data for comparison: {data_bits}") 