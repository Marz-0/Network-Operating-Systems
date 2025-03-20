def ones_complement_sum(a, b, bit_size=16):
    result = a + b
    if result >= (1 << bit_size):
        result = (result + 1) & ((1 << bit_size) - 1)
    return result

def calculate_checksum(data, bit_size=16):
    checksum = 0
    for word in data:
        checksum = ones_complement_sum(checksum, word, bit_size)
    return ~checksum & ((1 << bit_size) - 1)

def verify_checksum(data, received_checksum, bit_size=16):
    total = 0
    for word in data:
        total = ones_complement_sum(total, word, bit_size)
    total = ones_complement_sum(total, received_checksum, bit_size)
    return total == (1 << bit_size) - 1

data = [0b1010101010101010, 0b1100110011001100, 0b1111000011110000]
checksum = calculate_checksum(data)
print(f"Calculated Checksum: {bin(checksum)}")

is_valid = verify_checksum(data, checksum)
print("Checksum is valid" if is_valid else "Checksum is invalid")
