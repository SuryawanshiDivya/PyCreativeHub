s=input("Enter a String")
#use slicing
#print(s[::-1])

#with logic
i = len(s) - 1  # Find the index of the last character in the string
print(i)        # Print the initial value of `i` (last index)

result = ''     # Initialize an empty string to store the reversed result
while i >= 0:   # Loop while `i` is greater than or equal to 0 (valid indices)
    result = result + s[i]  # Append the character at index `i` to `result`
    i = i - 1   # Move to the previous character
print(result)   # Print the reversed string

#to check palindrome you can use this

if s == result:  # Compare original and reversed strings
    print(f"The string '{s}' is a palindrome.")
else:
    print(f"The string '{s}' is not a palindrome.")