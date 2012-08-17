#!/usr/bin/env python

#------------------------------------------------------------
#
# Ciro D. Santilli 
#
#------------------------------------------------------------

if __name__ == '__main__':
    
    import argparse
    
    parser = argparse.ArgumentParser(description="""Wrapper for markdown""",
        epilog="Report any bugs to ciro.santilli@gmail.com", 
        prog="Program")

    parser.add_argument('a',
        help="positional (obligatory) argument because no hyphen before a.",
        default="")

    parser.add_argument('-a',
        help="optional argument because there is hyphen before a. Takes a single value.",
        default="")

    parser.add_argument('-a', '--along'
        dest='a'
        help="provides long name. Must destination is 'along', not 'a'.",
        default="")

    parser.add_argument('-a', 
        action="store_true", 
        default=False, 
        help='a is False if not present')

    parser.add_argument('-a', 
        action="store_false", 
        default=True, 
        help="a is True if not present")




    parser.add_argument('-a',
        type=int,
        default=1
        help="stores an integer value")



    parser.add_argument('-a'
        nargs='*',
        help="optional. takes 0 or more args. stores a list.",
        default=[])

    parser.add_argument('-a'
        nargs=3,
        help="optional. takes 3 args exatcly. stores a list, even if nargs=1!",
        default=[])

    args = parser.parse_args(sys.argv[1:])
    a = args.a








    parser.add_argument('-b', '--blong', 
        action="store", 
        dest="b", 
        help='put string value given into b')
    

    
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
