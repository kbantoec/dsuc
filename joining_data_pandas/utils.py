import re

import pandas as pd


def social_fin_extractor(txt: str):
    pattern: bin = r"\s*\d+\s+(?P<financial>\w+)\s+(?P<company>\w+)\s+(?P<year>\d{4})\s+(?P<value>-*\d+)"
    regex = re.compile(pattern)
    data = [regex.match(row) for i, row in enumerate(txt.split('\n')) if i > 0]
    data = [(r.group('financial'), r.group('company'), r.group('value')) for r in data if r is not None]
    df = pd.DataFrame(data=data, columns=['financial', 'company', 'value'])
    df.value = df.value.astype(int)
    return df
