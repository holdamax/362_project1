"""Python implementation to
count number of ways to tile a floor
of size n x m using 1 x m tiles"""


def descr():
    """Function for to input and verification data"""
    n_size = input('Please, input the n size floor >= 0 (etc. 2): ')
    m_size = input('Please, input the m size floor >= 0 (etc. 3): ')
    if n_size == 'q' or m_size == 'q':
        return 'q'
    try:
        print("All combinations: {}".format(ways_tile_floor(n_size, m_size)))
        return None
    except (TypeError, ValueError, IndexError):
        print('Error! Please, enter correct size >= 0 and < 1000 (etc. 2 and 3)')




def ways_tile_floor(n_size, m_size):
    """ Function to count the total
        number of ways to sum up to 'number'
        Keyword arguments:
                n_size -- n size floor
                m_size m_size floor"""
    n_size = int(n_size)
    if len(str(n_size)) > 3 or len(str(m_size)) > 3:
        raise ValueError
    m_size = int(m_size)
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
    return count[n_size]
descr()