import os
import random

task = 'STS-B' #'CoLA'

samples = []

for run in range(10):
    for split in ['train', 'dev']:
        with open(os.path.join('data', task, '%s.tsv' % split), 'r') as f:
            lines = f.read().splitlines()
            if (task == 'STS-B'):
                lines = lines[1:]
            samples += lines
    indices = [idx for idx in range(len(samples))]
    random.shuffle(indices)
    indices_split = 1043 if task == 'CoLA' else 1498
    indices_train = indices[:indices_split]
    indices_dev = indices[indices_split:]
    for split in ['train', 'dev']:
        with open(os.path.join('data', task, '%s_%i.tsv' % (split, run)), 'w') as f:
            if (task == 'STS-B'):
                f.write('index\tgenre\tfilename\tyear\told_index\t'
                        'source1\tsource2\tsentence1\tsentence2\tscore\n')
            indices_split = eval('indices_%s' % split)
            for idx in indices_split:
                line = samples[idx]
                f.write(line + '\n')