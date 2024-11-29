# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
while True:
    user_input = input("Enter a word (type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    print(f"The length of the word '{user_input}' is {len(user_input)} characters.")
