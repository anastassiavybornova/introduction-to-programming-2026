def mystery_function(N):

    first_multiplier = int(N)
    final_number = int(N)
        
    if first_multiplier == 1 or first_multiplier == 0:
        return 1

    while first_multiplier > 1:
        final_number = final_number * (first_multiplier-1)
        first_multiplier -= 1

    return final_number

user_number = input("Provide me with an integer number! ")
mystery_number = mystery_function(user_number)
print(f"The mystery number for {user_number} is {mystery_number}!")