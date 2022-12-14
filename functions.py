def get_valid_input(input_string_message, valid_options):
    input_string_message += ' ({}): '.format(', '.join(valid_options))
    while True:
        response = input(input_string_message)
        if response.lower() in valid_options:
            break
    return response

def print_menu():
    print(f'\n1. Add new property\n2. Show specific property\n3. Show all property')
    print(f'4. Modify property\n5. Quit from system')
