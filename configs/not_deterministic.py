from src.code import hello, load_file

config = dict(
    _target_=hello,
    you=dict(
        _target_=load_file,
        file_name="data/me.txt"
    ),
)
