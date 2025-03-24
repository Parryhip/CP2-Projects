#Samuel Andelin, Tracing notes

#python -m trace --trace Notes\tracing.py

#_________________________________________1.What is tracing?

#Allows you to know when your functions are being called, where they are being called from, and what is happening inside


#_________________________________________2.What are some ways we can debug by tracing?

#make a function that lets us see how our function are interacting and running

"""
--trace (displays function lines as they are executed)
--count (displays the number of times each function is executed)
--listfuncs (displays the functions in the file)
--trackcalls (displays relationships between functions)
"""

#_________________________________________3.How do you access the debugger in VS Code?

#F5

#_________________________________________4.What is testing?
#_________________________________________5.What are boundary conditions?
#_________________________________________6.How do you handle when users give strange inputs?


def add(num1,num2):
    subtract(1,56)
    return num1+num2

def subtract(num1,num2):
    return num1-num2

print(add(1,56))
#print(subtract(1,56))

import trace
import sys

tracer = trace.Trace(count=False, trace=True)
def trace_calls(frame, event, arg):
    if event == "call":
        print(f'Calling function: {frame.f_code.co_name}')
    elif event == 'line':
        print(f'Executing line: {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return':
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception':
        print(f'Exception in {frame.f_code.co_name}: {arg}')
    return trace_calls

sys.settrace(trace_calls)
"""
call - When the function is called
line - when a new line is executed
return - when the function returns a value
exception - when there is an exception raised
"""