import os

votes = []
for file_name in os.listdir():
    if 'cola' in file_name and file_name.endswith('.tsv'):
        with open(file_name, 'r') as f:
            indices, preds = [], []
            lines = f.read().splitlines()[1:]
            for line in lines:
                line = line.split('\t')
                indices.append(line[0])
                preds.append(line[1])
            votes.append([indices, preds])
votes = votes[:4]
with open('CoLA.tsv', 'w') as f:
    f.write('index\tprediction\n')
    for i, index in enumerate(votes[0][0]): # votes[0][0][i] = indices[i] = index
        pred = 0
        for j in range(len(votes)):
            assert votes[j][0][i] == index
            pred += int(votes[j][1][i])
        f.write('%s\t%i\n' % (index, pred > len(votes) / 2))

votes = []
for file_name in os.listdir():
    if 'stsb' in file_name and file_name.endswith('.tsv'):
        with open(file_name, 'r') as f:
            indices, preds = [], []
            lines = f.read().splitlines()[1:]
            for line in lines:
                line = line.split('\t')
                indices.append(line[0])
                preds.append(line[1])
            votes.append([indices, preds])
votes = votes[:4]
with open('STS-B.tsv', 'w') as f:
    f.write('index\tprediction\n')
    for i, index in enumerate(votes[0][0]): # votes[0][0][i] = indices[i] = index
        pred = 0.0
        for j in range(len(votes)):
            assert votes[j][0][i] == index
            pred += float(votes[j][1][i])
        f.write('%s\t%f\n' % (index, pred / len(votes)))