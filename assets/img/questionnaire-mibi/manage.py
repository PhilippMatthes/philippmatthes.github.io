import os
import json

# Just some quick and dirty helper functions
def rename():
    path = os.path.dirname(os.path.realpath(__file__))
    qid = 0
    for i, f in enumerate(sorted(os.listdir(path))):
        if not f.startswith("Bildschirmfoto"):
            continue
        if i % 2 == 0:
            os.rename(f, "question_{}.png".format(qid))
        else:
            os.rename(f, "answer_{}.png".format(qid))
            qid += 1


def list_as_json():
    path = os.path.dirname(os.path.realpath(__file__))
    answers = [f for f in sorted(os.listdir(path)) if f.startswith("answer")]
    questions = [f for f in sorted(os.listdir(path)) if f.startswith("question")]
    print(json.dumps(answers))
    print(json.dumps(questions))


if __name__ == "__main__":
    list_as_json()
