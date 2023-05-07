# hardwaredl-final-project

## Setup

```bash
conda create -n dreamer python
conda activate dreamer
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
pip install transformers accelerate datasets evaluate wandb diffusers xformers triton scipy clip 

# spacy
pip install -U spacy
python -m spacy download en_core_web_sm

python setup.py develop
```