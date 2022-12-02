import re

import pandas as pd

import config

if __name__ == '__main__':
    with open(config.DATAPATH / "revenues.txt", mode='r', encoding='UTF-8') as file:
        content = file.readlines()
        header = content[0].split()
        data = [s.rstrip('\n') for s in content[1:]]

    pattern = fr"(?P<index>\d+)\s+(?P<rank>\d+)\s+(?P<company>\w+[\s\&\.\w\-\'\(\)]*)\s+(?P<revenue>-*\d+)\s+(?P<employees>\d+[\,\d]*)\s+(?P<industry>\w+\s*\w*)\s+(?P<age>\d+)"
    regex = re.compile(pattern)

    data = [regex.match(d) for d in data]
    data_ = [[r.group('index'),
              r.group('rank'),
              r.group('company'),
              r.group('employees'),
              r.group('industry'),
              r.group('age')]for r in data if r is not None]


    data_df = pd.DataFrame(data=data_, columns=file.readlines()[0])

