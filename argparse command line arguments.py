from argparse import OptionParser

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Post Yahoo weather to Twitter.', epilog="Report any bugs to example@email.com", prog='Program')

    parser.add_argument('-a', '--add', nargs=1, help='Add a new account. Use the desired account name as an argument.')
    parser.add_argument('-e', '--edit', nargs=1, choices=accountListSTR[:-1], help='Edit an account. Use the desired account name as an argument.')
    parser.add_argument('-g', '--getweather', nargs='*', choices=accountListSTR, help='Get weather and post here. Specify account(s) as argument. Use "all" for all accounts. If you specify multiple accounts, separate by a space NOT a comma.')
    parser.add_argument('-p', '--post', nargs='*', choices=accountListSTR, help='Post weather to Twitter. Specify account(s) as argument. Use "all" for all accounts. If you specify multiple accounts, separate by a space NOT a comma.')
    parser.add_argument('-c', '--custompost', nargs=2, help='Post a custom message. Specify an account then type the message. Make sure you use "" around the message. Use "all" for all accounts.')
    parser.add_argument('-l', '--list', action='store_const', const='all', help='List all accounts.')
    parser.add_argument('--version', action='version', version='%(prog)s 0.3.3')

    args = parser.parse_args()