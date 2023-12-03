def process_line(line):    
    integers = []

    integers.append(get_first_integer(line))    
    integers.append(get_first_integer(reversed(line)))    
    return integers[0]*10 + integers[-1]

def get_first_integer(elements):
    for element in elements:
        if element.isdigit():
            return (int(element))        

def solution_1():
    with open('1/input', 'r') as file:    
        integers = []    
        for line in file:        
            integers.append(process_line(line))
        print(sum(integers))
# def solution_2():

solution_1()
        
