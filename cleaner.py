import csv
import os
import pandas as pd

import re
import converter as conv
import cleaner as clr
import usersentencedivert as usd
import twitterhandler as twk

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)