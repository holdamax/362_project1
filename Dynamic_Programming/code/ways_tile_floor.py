"""Python implementation to
count number of ways to tile a floor
of size n x m using 1 x m tiles"""
def descr():
    """Function for to input and verification data"""
    try:
        n_size = int(input('Please, input the n size floor: '))
        m_size = int(input('Please, input the m size floor: '))
        return ways_tile_floor(n_size, m_size)
    except:
        print('Error! Please, enter correct size (etc. 2 and 3)')

def ways_tile_floor(n_size, m_size):
    """ Function to count the number of ways to tile the given floor using 1 x m tiles.
        Keyword arguments:
                n_size -- n size floor (default 0)
                m_size -- m size floor (default 0)"""
    count = []
    for i in range(n_size + 2):
        count.append(0)
    count[0] = 0

    for i in range(1, n_size + 1):
        if i > m_size:
            count[i] = count[i - 1] + count[i - m_size]
        elif i < m_size:
            count[i] = 1
        else:
            count[i] = 2
    print("All combinations:", end=" ")
    return count[n_size]
print(descr())