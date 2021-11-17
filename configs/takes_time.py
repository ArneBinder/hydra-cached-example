from src.code import load_file, delay

config = dict(
    _target_=delay,
    data=dict(
        _target_=load_file,
        file_name="data/lorem_ipsum.txt"
    ),
    seconds=2,
)
