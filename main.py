def main() -> None:
    while True:
        try:
            user_input: str = input(
                'Enter an expression of complex number algebra: ')

            if user_input == 'exit':
                print('Thanks for trying my program!')
                exit()

            user_input = user_input.replace('^', '**')
            user_input = user_input.replace('i', 'j')

            imaginary: complex = eval(user_input)
            print(f'Result: {imaginary}')
        except NameError:
            print('Invalid input')
        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
