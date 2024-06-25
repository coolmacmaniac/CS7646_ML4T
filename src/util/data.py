"""MLT: Utility code."""

import os
import yaml
import pandas as pd
#
from pydantic import BaseModel

# ---------------------------------------------------------------------------
def symbol_to_path(symbol, base_dir=None):
    """Return CSV file path given ticker symbol."""
    if base_dir is None:
        src_root_dir = os.environ.get('SRC_ROOT_DIR')
        market_data_dir = os.path.join(src_root_dir, 'data')
    return os.path.join(market_data_dir, '{}.csv'.format(str(symbol)))

# ---------------------------------------------------------------------------
def get_data(symbols, dates, addSPY=True, colname = 'Adj Close'):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if addSPY and 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols = ['SPY'] + symbols
    
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', colname], na_values=['nan'])
        df_temp = df_temp.rename(columns={colname: symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=['SPY'])
    
    return df

# ---------------------------------------------------------------------------
def plot_data(df, title='Stock prices', xlabel='Date', ylabel='Price'):
    import matplotlib.pyplot as plt
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.legend()
    plt.show()

# ---------------------------------------------------------------------------
def read_yaml(conf_file_path: str, model_class: BaseModel) -> BaseModel:
    """
    Performs the following tasks:
        1. Reads a config yaml file from the given path location
        2. Parse it using the given model_class
        3. Return the validated contents as BaseModel object
    """
    with open(conf_file_path, 'r') as fstream:
        config = yaml.load(fstream, Loader=yaml.SafeLoader)
    # the following call converts the model object to dict, if needed
    # return model_class(**config).model_dump()
    return model_class(**config)
