//
//  calculator.cpp
//  HelloWorld
//
//  Created by Joseph Koon on 2/13/16.
//  Copyright © 2016 Joseph Koon. All rights reserved.
//


#include <iostream>
#include <string>

using namespace std;

//comment yes
/* comment here */

int addition (int x, int y)
{
    return x + y;
}

int subtraction (int x, int y)
{
    return x - y;
}

int multiplication (int x, int y)
{
    return x * y;
    
}

int division (int x, int y)
{
    return x / y;
}





int main ()
{
    string input = "";
    
    int result = 0;
    int value1 = 0;
    int value2 = 0;
    bool stop = true;
    
    while (stop == true)
    {
        cout << "+ - x / \n";
        cin >> input;
        
        if (input == "EXIT")
        {
            cout << "BYE\n";
            break;
        }
        
        cout << "Value 1: ";
        cin >> value1;
        
        cout << "Value 2: ";
        cin >> value2;
        
        
        if (input== "+")
        {
            result = addition(value1, value2);
            cout << result << "\n";
        }
        else if (input== "-")
        {
            result = subtraction(value1, value2);
            cout << result << "\n";
        }
        else if (input== "x")
        {
            result = multiplication(value1, value2);
            cout << result << "\n";
        }
        else if (input== "/")
        {
            result = division(value1, value2);
            cout << result << "\n";
        }
        
        
        
        
    }
    
    
    
}