import os
import yaml
import argparse

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import torch

if __name__ == '__main__':
    with open('config.yml') as f:
        conf = yaml.load(f)
    data_dir = conf['data']['dir']
    data = pd.read_csv(os.path.join(data_dir, 'train.csv'))

    print(data.columns)
    data_sample = data[data['Asset_ID'] == 2]
    close = data_sample['Close']
    close = close.to_numpy(dtype=float)

    plt.plot(close)
    plt.show()
    plt.savefig('data.pnd')
