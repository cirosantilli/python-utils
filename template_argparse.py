#!/usr/bin/env python

#------------------------------------------------------------
#
# Ciro D. Santilli 
#
#------------------------------------------------------------

if __name__ == '__main__':
    
    import argparse
    
    parser = argparse.ArgumentParser(description='Wrapper for markdown',
        epilog="Report any bugs to ciro.santilli@gmail.com", 
        prog='Program')

    parser.add_argument('a',
        help='positional (obligatory) argument')
    args = parser.parse_args('va')
    a = args.a

    parser.add_argument('a',
            nargs='*',
            help='n or zero positional args')

    parser.add_argument('-a', '--along', 
        dest='da', 
        action="store_true", 
        default=False, 
        help='a is False if not present')
    
    parser.add_argument('-b', '--blong', 
        action="store", 
        dest="b", 
        help='put string value given into b')
    
    parser.add_argument('-c', '--clong',
        dest="c_new",
        type=int,
        help='put value into c_new instead of c')

    parser.add_argument('--three', 
        nargs=3,
        help='3 args exatcly')
    
    parser.add_argument('--optional', 
        nargs='?', 
        help='0 or 1 args exatcly (must be last arguments)')
    
    parser.add_argument('--all', 
        nargs='*', 
        dest='all', 
        help='0 or more args (must be last arguments)')
    
    parser.add_argument('--one-or-more',
        nargs='+',
        help='1 or more args (must be last arguments)' )
    
    parser.add_argument('-c',
        action='store_const',
        dest='constant_value',
        const='value-to-store',
        help='Store a constant value')

    parser.add_argument('-t',
        action='store_true',
        default=False,
        dest='boolean_switch',
        help='Set a switch to true')
    
    parser.add_argument('-f',
        action='store_false',
        default=False,
        dest='boolean_switch',
        help='Set a switch to false')

    parser.add_argument('-a',
        action='append',
        dest='collection',
        default=[],
        help='Add repeated values to a list')

    parser.add_argument('-A', 
        action='append_const',
        dest='const_collection',
        const='value-1-to-append',
        default=[],
        help='Add different values to list')
    
    parser.add_argument('-B', 
        action='append_const',
        dest='const_collection',
        const='value-2-to-append',
        help='Add different values to list')

    args = parser.parse_args()
    a = args.a
