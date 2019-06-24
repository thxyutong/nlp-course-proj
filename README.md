# NLP Course Project

## Instructions

1. install requirements: ```> pip install -r requirements.txt```

2. download data: ```> sh download.sh```
   can also put the data of CoLA and STS-B into ```./data/CoLA``` and ```./data/STS-B```

3. preprocess data:
   ```> python prepro.py```

4. training models:
   1. CoLA dataset
      ```> sh scripts/nlp.sh 16 <gpu_id> cola```
   2. STS-B dataset
      ```> sh scripts/nlp.sh 8 <gpu_id> stsb```

5. get results: 
   after training, results are stored in ```./scripts/checkpoints/<model_dir>```
   where predictions of CoLA are in ```cola_test_scores_<epoch>.tsv``` and predictions of STS-B are in ```stsb_test_scores_<epoch>.json``` (can be transformed into ```.tsv``` with ```./json2tsv.py```)
   ```./ensemble.py``` is offerred to ensemble multi predictors (can obtain random splits with ```./random_split.py```)

## Model Check Points

Can down load via https://pan.baidu.com/s/1mR53v6-mgSY0Yw26t9tEOQ (hs97)

## Reference

- [Multi-Task Deep Neural Networks for Natural Language Understanding](https://github.com/namisan/mt-dnn)