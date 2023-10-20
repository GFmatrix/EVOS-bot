import json
import os
from types import SimpleNamespace

with open(os.path.join('bot', 'translate', 'text.json'), encoding='utf-8') as f:
    text = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
    f.close()
    
jtext = json.load(open(os.path.join('bot', 'translate', 'text.json'), encoding='utf-8'))