# Define pyramid height
rows = 5

# Outer loop for rows
for i in range(1, rows + 1):
  # Inner loop for spaces (decreasing)
  for j in range(rows - i):
    print(" ", end="")  # Print spaces without a newline

  # Inner loop for numbers (increasing)
  for j in range(1, i + 1):
    print(j, end=" ")  # Print number with a space

  # Move to the next line
  print()
