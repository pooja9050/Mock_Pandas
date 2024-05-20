#619. Biggest Single Number
import pandas as pd
def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    x = list(my_numbers['num'])
    # Create an empty dictionary to store counts of each number.
    dict1 = defaultdict(int)
    # Loop through each number in the list and count its occurrences.
    for i in x:
        dict1[i] += 1
    # Initialize maxnum to None initially.
    maxnum = None
    # Initialize max_count to -1 initially to ensure it is lower than any count found.
    max_count = -1
    # Loop through each key-value pair in the dictionary.
    for key, value in dict1.items():
        # If the count of the number is 1, update maxnum if it's the first single number found or larger than the current maxnum.
        if value == 1:
            if maxnum is None or key > maxnum:
                maxnum = key
                # Update max_count to the count of the current single number.
                max_count = value
    # Check if any single number was found and return it, otherwise return None.
    if maxnum is not None:
        return pd.DataFrame({'num': [maxnum]})
    else:
        return pd.DataFrame({'num': [None]})
#620. Not Boring Movies
import pandas as pd
def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    #Filtering inside of cinema by not include the boring in the description column and id should not be even.
    y = cinema[(cinema['description']!='boring') & (cinema['id'] % 2 != 0)]
    #Result should be in descending order of rating with all the columns with the filtered data of odd id and not including boring description
    return y.sort_values(by = 'rating', ascending=False)
