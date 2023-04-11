
import json


def is_answer(node):
    return len(node) == 1


f = open("/Users/wukaiti/Spiced/bergamot-encoder-encounter-notes/week_02/Debugging/questions.json")
content = f.read()
print(content)
try:
    node = json.reads()
except AttributeError as e:
    print("what do do now?")

finished = False

while not finished:
    try:
        print(node['text'])
    except NameError as e:
        print(f"find where {e} is defined")
        if "is_answer_node"(node):
            try:
                finished = True
            except NameError as e:
                print(f"find where {e} is defined")
else:
    "answer" == input()
    if "answer".upper() in ['yes', 'y']:
        node = node['no']
    else:
        node = node['yes']
