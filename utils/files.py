from pathlib import Path
from typing import Union
from utils.display import repr1

def get_files(path: Union[str, Path], extension='.wav'):
    if isinstance(path, str): path = Path(path).expanduser().resolve()
    return list(path.rglob('*%s' % (repr1(extension))))
