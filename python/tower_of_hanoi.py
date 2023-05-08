def tower_of_hanoi(n, source, destination, intermediate):
    # Where the top most disk is 1 and the bottom most disk is n
    if n >= 1:
        tower_of_hanoi(n-1, source, intermediate, destination)
        print(f'{n} {source} {destination}') 
        tower_of_hanoi(n-1, intermediate, destination, source)
    

if __name__ == '__main__':
    n = 2
    source = 'A'
    intermediate = 'B'
    destination = 'C'

    tower_of_hanoi(3, source, destination, intermediate)
