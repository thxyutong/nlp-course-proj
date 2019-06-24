import json

for run in range(7):
    file_name = 'stsb_%i' % run

    with open(file_name + '.json', 'r') as f:
        results = json.load(f)
        uids = results['uids']
        scores = results['scores']

    with open(file_name + '.tsv', 'w') as f:
        f.write('index\tprediction\n')
        assert len(uids) == len(scores)
        paired = [(int(uid), scores[idx]) for idx, uid in enumerate(uids)]
        paired = sorted(paired, key=lambda item: item[0])
        for uid, score in paired:
            f.write('%i\t%f\n' % (uid, score))