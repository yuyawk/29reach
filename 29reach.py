#!/usr/bin/env/ python
# *-# -*- coding: utf-8 -*-

import sys



flag = 0

while flag == 0 :

    flag = 1
    
    print('Input an integer larger than 8 : ')
    print('Your input: ', end = '')
    N = int(sys.stdin.readline().strip())
    print(N)
    
    if N <= 8 :

        flag = 0
        print('The integer has to be larger than 8.')
        print('Try again.')

    #end if
    
#end while

if N % 2 == 0 :

    k = 0
        
    while N - 18 * k  >= 2 :

        print('{}=2x{}+9x{}'.format( N, int(N/2) - 9 * k , 2 * k ) )
        k += 1

    #end while

else :
    
    k = 0
        
    while N - 18 * k  >= 9 :

        print('{}=2x{}+9x{}'.format( N, int((N-1)/2) - 4 - 9 * k , 2 * k + 1 ) )
        k += 1

    #end while

#end if
        
        
    
