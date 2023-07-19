
import numpy as np
import pandas as pd

# --------------------------------------------------- TASK 1 -------------------------------------------------------

def create_df(missing=False, n=10):
    itemid   = np.random.randint(100000, size=n)+1000
    category = np.random.randint(3, size=n)
    price    = np.round(np.random.normal(loc=100, scale=10, size=n),2)
    margin   = np.round(np.random.normal(loc=10, scale=1, size=n),2)
    
    if missing:
        nmissing = np.random.randint(len(price)//2)+2                                     
        price[np.random.permutation(len(price))[:nmissing]] = np.nan
    
    d = pd.DataFrame(np.r_[[price, category, margin]].T, index=itemid, columns=["price", "category", "margin"])
    d.index.name="itemid"
    if np.random.random()>.5:
        d = d[d.columns[:2]]
        
    return d

d = create_df()

def select_items(df):
    # make sure to make a copy in case you modify the original df
    df = df.copy()
    
    ... # YOUR CODE HERE
    if df.shape[1] == 3:
        result = df[(df['price']>100)|(df['margin']>10)]
    else:
        result = df[(df['price']>100)]
    
    return list(result.index)

print(select_items(d))

# ---------------------------------------------------- TASK 2 ----------------------------------------

def get_stats(df):
    # make sure to make a copy in case you modify the original df
    df = df.copy()
        
    ... # YOUR CODE HERE    

    if df.shape[1] == 3:
        del(df['margin'])
    df2 = pd.DataFrame(df, columns=["media", "maximo", "minimo"], index=pd.to_numeric(df['category'], downcast='integer'))
    df2.sort_index(inplace=True)
    df.index.name = 'categoria'
    df2['media'] = df.groupby('category').mean()
    df2['maximo'] = df.groupby('category').max()
    df2['minimo'] = df.groupby('category').min()

    result = df2.groupby('category').max()
    return result

print(get_stats(d))

# --------------------------------------------------- TASK 3 -----------------------------------------

def fillna(df):
    # make sure to make a copy in case you modify the original df
    df = df.copy()
    
    ... # YOUR CODE HERE    
    
    k = df['price'].values
    j = df['price'].isna().values
    k[j] = np.random.normal(df.price.mean(), df.price.std(), df.isna().price.sum())

    result = df
    return result

d = create_df(missing=True)
print(d)
print(fillna(d))