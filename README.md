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
```
NOTE: The following examples assume that the root of this repo:
* is the current working directory, i.e. `cd hydra-cached-example` was executed, and
* it is in the python path, i.e. `export PYTHONPATH=.` or similar was executed (otherwise just prepend `PYTHONPATH=. ` 
  to the example commands).

Simple hello world example ([config](configs/hello_world.py)):
```bash
instantiate configs.hello_world
```

Same as above, but load name from file and show the config in yaml format via `-d`/`--display_config` ([config](configs/hello_file.py)):
```bash
instantiate configs.hello_file -d
```

Persisting the cache with `-p`/`--persist_cache` ([config](configs/takes_time.py)):
```bash
instantiate configs.takes_time -p -d
```
NOTES: 
 * Using `-p`/`--persist_cache` will also check, if there is content in the cache directory and load that, before instantiation starts.
 * `cache` is the default cache directory (change via `-c`/`--cache_dir` parameter).
 * Per default, only the result of functions is cached whose calculation needed more than one second to not clutter the cache directory so much. 
 * Each persisted cache entry consists of two files:
   * `SUBCONFIG_HASH.yaml`: the subconfig that was used to calculate the content
   * `SUBCONFIG_HASH.pkl`: the actual content (wrapped into a simple metadata class)
 
IMPORTANT: Methods that are **not deterministic** should be **marked with the decorator** 
`@hydra_cached.execution.hydra_utils.not_deterministic`! This will result in replacing the entry of that method call 
in entries above (regarding the execution DAG) with `{"hash": HASH`} where `HASH` is the result of the not 
deterministic function. This allows to use caching persistence also for methods that involve e.g. loading data from files etc.
