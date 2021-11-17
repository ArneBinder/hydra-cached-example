# hydra-cached-example
example repo to show usage of [hydra-cached](https://github.com/ArneBinder/hydra-cached)

## Setup

```bash
# install hydra-cached
python -m pip install git+https://github.com/ArneBinder/hydra-cached
# get the example from this repo
git clone git@github.com:ArneBinder/hydra-cached-example.git
```

## Usage
```bash
# show help for hydra-cached
instantiate -h

# execute example (don't forget to add the location of code and configs to the python path)
PYTHONPATH=hydra-cached-example instantiate configs.hello_mike
```
