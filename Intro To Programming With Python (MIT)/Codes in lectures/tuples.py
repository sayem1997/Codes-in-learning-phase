def get_data(aTupple):
    '''
    return the number of song have been sung in a certain time. 
    '''
    num_of_years = ()
    name_of_song = ()
    for t in aTupple:
        num_of_years = num_of_years + (t[0],)
        if t[1] not in name_of_song:
            name_of_song = name_of_song + (t[1],) 

    min_year = min(num_of_years)
    max_year = max(num_of_years)

    number_of_song = len(name_of_song)

    return (min_year,max_year,number_of_song)

tswift = ((2005,'Joe'),
            (2008,'Harry'),
              (2012,'Jake'))

(starting_year, closing_year, number_of_song) = get_data(tswift)

print('From {} to {} Taylor Swift have sung {} songs'.format(starting_year,closing_year,number_of_song))