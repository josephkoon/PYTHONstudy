//
//  main.cpp
//  HelloWorld
//
//  Created by Joseph Koon on 2/13/16.
//  Copyright © 2016 Joseph Koon. All rights reserved.
//

#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>

using namespace std;

//comment yes
/* comment here */



//display initial menu
//select different functions from menu

int randRange (int low, int high)
{
    return rand() % (high - low + 1) + low;
}



int main()
{
    long timevalue = time(NULL);
    
    srand(timevalue);
    
    
    int generatednum = randRange(1,100);
    int guessednum = 0;
    
    while (true)
    {
        cout << "Guess between 1-100: \n";
        cin >> guessednum;
        
        if (guessednum == generatednum)
        {
            cout << "You got it!\n";
            break;
        }
        else if (guessednum < generatednum)
        {
            cout << "Too low!\n";
        }
        else if (guessednum > generatednum)
        {
            cout << "Too high!\n";
        }
        
        
    }
    
    
}