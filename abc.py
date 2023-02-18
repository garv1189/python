# Accept the file name from the user
filename = input("Enter a file name:abc ")

# Find the position of the last dot in the file name
dot_position = filename.rfind('.')

# Extract the extension from the file name
extension = filename[dot_position + 1:]

# Print the extension
print("The extension of the file is:py", extension)