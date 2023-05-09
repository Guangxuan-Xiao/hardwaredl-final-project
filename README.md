# Benchmarking ImageNet Classification Models 

MIT 6.5930 Hardware Arch for Deep Learning Final Project
### Guangxuan Xiao, Tianwei Yin

# Workloads 

## Accuracy Evalaution

We evalaute the accuracy of the pretrained models on ImageNet validation set using [accuracy_evalution/test.py](accuracy_evalution/test.py).

## Timeloop Profiling

```bash
docker-compose pull
docker-compose up

cd final-project
bash scripts/profile_all.sh
```

