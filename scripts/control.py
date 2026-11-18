import numpy as np

# Define the matrix A
A = np.array([[0, 1],
              [-6, -5]])

# Calculate eigenvalues
eigenvalues = np.linalg.eig(A)

print("Matrix A:")
print(A)
print("\nEigenvalues:")
print(eigenvalues[0])
print("\nEigenvectors:")
print(eigenvalues[1])

# Alternative: Get just eigenvalues
eigenvalues_only = np.linalg.eigvals(A)
print("\nEigenvalues (only):")
print(eigenvalues_only)

# Verify by checking the characteristic equation
print("\nVerification:")
for i, eigval in enumerate(eigenvalues[0]):
    print(f"Eigenvalue {i+1}: {eigval:.6f}")
    
    # Check if det(A - λI) = 0
    I = np.eye(2)  # Identity matrix
    det_value = np.linalg.det(A - eigval * I)
    print(f"det(A - λI) = {det_value:.10e}")