# Task 3: Calculate Uncompressed Grayscale Image Size in Kilobytes

# Take image dimensions from the user
width = int(input("Enter image width in pixels: "))
height = int(input("Enter image height in pixels: "))

# Calculate total pixels and size in bytes (1 byte per pixel for grayscale)
total_pixels = width * height
size_bytes = total_pixels

# Convert size from bytes to kilobytes (1 KB = 1024 bytes)
size_kb = size_bytes / 1024

# Display results
print("\n--- Image Size Calculation ---")
print("Total Pixels:", total_pixels)
print("Approximate Image Size:", size_bytes, "bytes")
print("Approximate Image Size in Kilobytes:", size_kb, "KB")
