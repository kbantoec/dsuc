import re

import pandas as pd


def extractor(txt: str, pattern: bin, columns: list):
    regex = re.compile(pattern)

    # Pass the header
    data = [regex.match(row) for i, row in enumerate(txt.split('\n')) if i > 0]
    data = [[r.group(col) for col in columns] for r in data if r is not None]
    df = pd.DataFrame(data=data, columns=columns)
    return df


def social_fin_extractor(txt: str):
    pattern: bin = r"\s*\d+\s+(?P<financial>\w+)\s+(?P<company>\w+)\s+(?P<year>\d{4})\s+(?P<value>-*\d+)"
    regex = re.compile(pattern)
    data = [regex.match(row) for i, row in enumerate(txt.split('\n')) if i > 0]
    data = [(r.group('financial'), r.group('company'), r.group('value')) for r in data if r is not None]
    df = pd.DataFrame(data=data, columns=['financial', 'company', 'value'])
    df.value = df.value.astype(int)
    return df


def inflation_extractor(txt: str):
    pattern = r"\s*\d+\s+(?P<country>\w+)\s+(?P<indicator>\w+\s%)\s+(?P<y2017>-*\d+\.\d+)\s+(?P<y2018>-*\d+\.\d+)\s+(?P<y2019>-*\d+\.\d+)"
    df = extractor(txt, pattern, columns=['country', 'indicator', 'y2017', 'y2018', 'y2019'])
    df.loc[:, ['y2017', 'y2018', 'y2019']] = df.loc[:, ['y2017', 'y2018', 'y2019']].astype(float)
    df.rename(columns=dict(zip(['y2017', 'y2018', 'y2019'], ['2017', '2018', '2019'])), inplace=True)
    return df


def gov_data_extractor(txt: str):
    months = [dt.month_name().lower()[:3] for dt in pd.date_range('2020-01', '2021-01', freq='m')]
    subpattern = '\s+'.join([f"(?P<{m}>\d+\.\d+|NaN)" for m in months])
    pattern = fr"\s*\d+\s+(?P<year>\d+)\s+{subpattern}"
    df = extractor(txt, pattern, columns=['year'] + months)
    df.year = df.year.astype(int)
    df_temp = df.drop('year', axis=1).copy()
    df.loc[:, df_temp.columns] = df_temp.astype(float)
    return df


if __name__ == '__main__':
    gov_data_str = """    year  jan  feb  mar  apr  may  jun  jul  aug  sep  oct  nov  dec
    0   2010  9.8  9.8  9.9  9.9  9.6  9.4  9.4  9.5  9.5  9.4  9.8  9.3
    1   2011  9.1  9.0  9.0  9.1  9.0  9.1  9.0  9.0  9.0  8.8  8.6  8.5
    2   2012  8.3  8.3  8.2  8.2  8.2  8.2  8.2  8.1  7.8  7.8  7.7  7.9
    3   2013  8.0  7.7  7.5  7.6  7.5  7.5  7.3  7.2  7.2  7.2  6.9  6.7
    4   2014  6.6  6.7  6.7  6.2  6.3  6.1  6.2  6.1  5.9  5.7  5.8  5.6
    5   2015  5.7  5.5  5.4  5.4  5.6  5.3  5.2  5.1  5.0  5.0  5.1  5.0
    6   2016  4.9  4.9  5.0  5.0  4.8  4.9  4.8  4.9  5.0  4.9  4.7  4.7
    7   2017  4.7  4.6  4.4  4.4  4.4  4.3  4.3  4.4  4.2  4.1  4.2  4.1
    8   2018  4.1  4.1  4.0  4.0  3.8  4.0  3.8  3.8  3.7  3.8  3.7  3.9
    9   2019  4.0  3.8  3.8  3.6  3.6  3.7  3.7  3.7  3.5  3.6  3.5  3.5
    10  2020  3.6  3.5  4.4  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN"""
    months = [dt.month_name().lower()[:3] for dt in pd.date_range('2020-01', '2021-01', freq='m')]
    subpattern = '\s+'.join([f"(?P<{m}>\d+\.\d+|NaN)" for m in months])
    pattern = fr"\s*\d+\s+(?P<year>\d+)\s+{subpattern}"
    df = extractor(gov_data_str, pattern, columns=['year'] + months)
    df.year = df.year.astype(int)
    df_temp = df.drop('year', axis=1).copy()
    df.loc[:, df_temp.columns] = df_temp.astype(float)