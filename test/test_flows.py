from common_utils.pyflow import seq


if __name__ == "__main__":
    print seq.open('./common_utils/pyflow/flows/a.txt', encoding='utf8').take(2, lazy=True).map(lambda line: line.strip()).filter(lambda x: len(x) > 3).get()
