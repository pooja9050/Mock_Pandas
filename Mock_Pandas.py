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


#1084. Sales Analysis III
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    q1_2019 = sales[(sales['sale_date'] >= '2019-01-01') & (sales['sale_date'] <= '2019-03-31')]
    other_q = sales[(sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31')]
    exclusive_ids = q1_2019[~q1_2019['product_id'].isin(other_q['product_id'].unique())]['product_id'].unique()
    return product[product['product_id'].isin(exclusive_ids)][['product_id', 'product_name']]

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df1 = sales[(sales['sale_date']>= '2019-01-01') & (sales['sale_date'] <= '2019-03-31')]
    df2 = sales[~((sales['sale_date']>= '2019-01-01') & (sales['sale_date'] <= '2019-03-31'))]
    df3 = df1.merge(df2, left_on = 'product_id', right_on = 'product_id', how = 'left')
    df4 = df3[df3['price_y'].isna()]
    df = df4.merge(product, left_on = 'product_id', right_on = 'product_id', how = 'inner')
    return df[['product_id', 'product_name']].drop_duplicates()


#1158. Market Analysis I
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders['orders_in_2019'] = orders['order_date'].apply(lambda x: 1 if x.year==2019 else 0)
    df = orders.groupby('buyer_id')['orders_in_2019'].agg('sum').reset_index()
    df = users.merge(df, left_on='user_id', right_on='buyer_id', how='left')
    df['orders_in_2019'] = df['orders_in_2019'].fillna(0).astype(int)
    return df[['user_id', 'join_date', 'orders_in_2019']].rename(columns={'user_id': 'buyer_id'})

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = pd.to_datetime(orders['order_date']) # Convert order_date to datetime
    orders['order_date'] = orders['order_date'].dt.year
    orders = orders[orders['order_date'] == 2019]
    df = orders.groupby('buyer_id').size().reset_index(name='orders_in_2019')
    df = users.merge(df, left_on='user_id', right_on='buyer_id', how='left')
    df['orders_in_2019'] = df['orders_in_2019'].fillna(0).astype(int)
    df = df[['user_id', 'join_date', 'orders_in_2019']]
    return df.rename(columns={'user_id': 'buyer_id'})

