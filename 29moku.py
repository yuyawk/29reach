#!/usr/bin/env/ python
# *-# -*- coding: utf-8 -*-

import sys
import numpy as np



#constants

Nrow = 29
Ncolumn = 29
turn_max = 92
Npoint_win = 3




kanji = { 2 : 'Ni' , 9 : 'Ku' }

mp = [ [ '#' for _ in range(Ncolumn)] for __ in range(Nrow) ]

turn = 1

mp_fl = np.array([[0] * Ncolumn for _ in range(Nrow)])




def count( Y , X , num , ind ) :

    
    dY = [ 0, 1, 1, -1 ]
    dX = [ 1, 0, 1, 1 ]


    global mp_fl
    

    mp_fl[Y][X] = 1  
    
        
    for j in range( -1 , 2 , 2 ) :
        
        nY = Y + j * dY[ind] 
        nX = X + j * dX[ind]
        
        if 0 <= nY < Nrow and 0 <= nX < Ncolumn :
            
            if  mp[nY][nX] == '{}'.format(num) and mp_fl[nY][nX] == 0  :

                count( nY , nX , num , ind )
                                        
            #end if
            
        #end if

    #end for

  
#end def




flag_win = 0


while turn <= turn_max and flag_win == 0 :


    for y in range(Nrow) :

        print(''.join(mp[y]))

    #end for

    
    if turn % 2 == 1 :
        
        print('Player Ni\'s turn (turn{})'.format(turn))
        n = 2
        
    else :

        print('Player Ku\'s turn (turn{})'.format(turn))
        n = 9
        
    #end if

    print('To indicate the point x-th from the left and y-th from the top, you have to enter "x y"')
    print('Don\'t forget the space between x and y.')
    print('1 <= x <= {}, 1 <= y <= {} : integers'.format(Ncolumn,Nrow))
    print('Indicate where to place your number {}. :'.format(n))

    try :

        x,y = map( int , sys.stdin.readline().split() )

        x -= 1
        y -= 1
        
        if x < 0 or x > Ncolumn - 1 or y < 0 or y > Nrow - 1 :
            
            raise ValueError

        #end if 


        if mp[y][x] == '#' :
        
            mp[y][x] = '{}'.format(n)

        else :

            print('ValueError:You cannot place the number there.')
            raise ValueError

        #end if 
        
            

        for j in range(4) :
            
            mp_fl = np.array([[0] * Ncolumn for _ in range(Nrow)])
            
            count(y,x,n,j)
            
            if np.sum(mp_fl) >= Npoint_win :
                
                print('{} wins!'.format(kanji[n]) )

                flag_win = 1
                
                break
            
            #end for


        
        turn += 1

            
    except KeyboardInterrupt:

        print('KeyboardInterrupt')
        sys.exit()

    except ValueError:

        print('ValueError:Try again.\n')
        pass
        

    #end try
        
    
#end while

if turn > turn_max and flag_win == 0:

    print('Draw')

#end if
