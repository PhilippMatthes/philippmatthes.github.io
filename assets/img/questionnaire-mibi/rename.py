import os

if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    qid = 0
    for i, f in enumerate(os.listdir(path)):
        if not f.startswith("Bildschirmfoto"):
            continue
        if i % 2 == 0:
            os.rename(f, "question_{}.png".format(qid))
        else:
            os.rename(f, "answer_{}.png".format(qid))
        qid += 1
