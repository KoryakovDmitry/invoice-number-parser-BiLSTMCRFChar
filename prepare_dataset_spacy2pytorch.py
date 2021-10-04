import os
import json
import os.path as osp
from glob import glob

dataset_paths = glob(osp.join(os.getcwd(), "dataset/dataset_ner_invnum_*.json"))
# dataset_paths = glob(osp.join(os.getcwd(), "dataset/bad_test.json"))

dataset = list()

for p in dataset_paths:

    with open(p, "r") as f:
        dataset.extend(json.load(f))


new_dataset = list()

for text, span in dataset:
    span = span["entities"][0]
    start = span[0]
    end = span[1]

    text_true = text[start:end]

    chars = list(text)
    chars_l = len(chars)
    tags = list()
    for char_i in range(0, chars_l):
        if char_i == start:
            tags.append("B")
        elif char_i >= end:
            tags.append("O")
        elif char_i > start:
            tags.append("I")
        else:
            tags.append("O")
    assert chars_l == len(tags), "yasno hueta"

    new_dataset.append((chars, tags))

with open(
    osp.join(os.getcwd(), "new_dataset/dataset_ner_invnum_all.json"),
    "w",
    encoding="utf8",
) as f:
    json.dump(new_dataset, f, ensure_ascii=False)
