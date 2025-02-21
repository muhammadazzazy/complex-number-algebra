def main() -> None:
    exit_message: str = 'Exiting program...'
    print('Welcome to The Complex Number Algebra 🖩!')
    while True:
        try:
            user_input: str = input(
                'Enter a complex number algebraic expression: ')
            if user_input == 'exit':
                print(exit_message)
                exit()

            user_input = user_input.replace('^', '**')
            user_input = user_input.replace('i', 'j')

            imaginary: complex = eval(user_input)
            print(f'Result: {imaginary}')

        except NameError:
            print('Please enter some valid input...')

        except KeyboardInterrupt:
            print(exit_message)
            exit()


if __name__ == '__main__':
    main()
