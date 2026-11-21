from pathlib import Path
import json
root=Path(__file__).parent
questions=json.loads((root/'questions.json').read_text(encoding='utf-8'))
assert sum(q['type']=='ai' for q in questions)>=5
assert sum(q['type']=='real' for q in questions)>=5
assert len({q['id'] for q in questions})==len(questions)
import hashlib
from urllib.parse import quote
for q in questions:
 f=q['file'].replace(' ','_')
 h=hashlib.md5(f.encode('utf-8')).hexdigest()
 q['directUrl']=f'https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{quote(f)}'
tpl=(root/'index.template.html').read_text(encoding='utf-8')
if tpl.count('__QUESTIONS_PAYLOAD__') != 1:raise ValueError('placeholder missing')
text=tpl.replace('__QUESTIONS_PAYLOAD__',json.dumps(questions,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
(root/'index.html').write_text(text,encoding='utf-8')
print('Built index.html',len(text),'characters,',len(questions),'images')
