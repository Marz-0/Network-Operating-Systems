import numpy as np

def compute_parity(mat):
    return np.sum(mat, axis=1) % 2, np.sum(mat, axis=0) % 2

data = np.array([
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1]
])

print("Original Data:", data)
row_par, col_par = compute_parity(data)

print("Row Parity:", row_par)
print("Column Parity:", col_par)

# Introduce an error
data_err = data.copy()
data_err[2, 1] = 1 - data_err[2, 1]

print("Data with error at (2, 1):", data_err)

new_row_par, new_col_par = compute_parity(data_err)
err_row = np.where(new_row_par != row_par)[0]
err_col = np.where(new_col_par != col_par)[0]

if err_row.size == 1 and err_col.size == 1:
    error_location = (err_row[0], err_col[0])
    print("Error detected at:", error_location)
    data_err[error_location] = 1 - data_err[error_location]
    print("Corrected Data:", data_err)
else:
    print("No single-bit error detected or multiple errors occurred.")