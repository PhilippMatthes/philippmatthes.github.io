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
            os.rename(f, "q_gentech_{}.png".format(qid))
        else:
            os.rename(f, "a_gentech_{}.png".format(qid))
            qid += 1


def shorten():
    path = os.path.dirname(os.path.realpath(__file__))
    for f in sorted(os.listdir(path)):
        name = str(f)
        print(name)
        if name.startswith("answer"):
            name = name.replace("answer", "a")
            os.rename(f, name)
        if name.startswith("question"):
            name = name.replace("question", "q")
            os.rename(f, name)



def list_as_json():
    path = os.path.dirname(os.path.realpath(__file__))
    answers = [f for f in sorted(os.listdir(path)) if f.startswith("a_gentech")]
    questions = [f for f in sorted(os.listdir(path)) if f.startswith("q_gentech")]
    print(json.dumps(answers))
    print(json.dumps(questions))


if __name__ == "__main__":
    list_as_json()
