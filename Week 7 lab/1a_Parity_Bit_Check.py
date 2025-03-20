def compute_even_parity(data):
    return sum(data) % 2

data = [1, 0, 1, 0, 1, 1, 0, 0]
parity_bit = compute_even_parity(data)

print("Original Data:", data)
print("Computed Parity Bit (Even):", parity_bit)

transmitted_data = data + [parity_bit]
print("Transmitted Data (Data + Parity):", transmitted_data)

# Simulate an error
error_index = 3
data_with_error = transmitted_data.copy()
data_with_error[error_index] = 1 - data_with_error[error_index]

print("Data with an Error Introduced at index", error_index, ":", data_with_error)

# Check for error detection
if sum(data_with_error) % 2 == 0:
    print("No error detected (Parity Check Passed)")
else:
    print("Error detected (Parity Check Failed)")
