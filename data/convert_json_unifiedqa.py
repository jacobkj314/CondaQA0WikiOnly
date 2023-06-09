import json
import jsonlines
# import tensorflow as tf
import re

def normalize_text(text):
    """Lowercase and remove quotes from a TensorFlow string."""
    text = text.lower()
    #text = re.sub(text, "'(.*)'", r"\1")
    return text


def write_data(data, filename):
    with jsonlines.open(filename, mode='w') as writer:
        writer.write_all(data)
        writer.close()


filenames = ["./condaqa_train.json", "./condaqa_dev.json", "./condaqa_test.json"]

for filename in filenames:
    data = []
    gold = [] # # # I also need to filter out the gold answer keys
    with open(filename) as f:
        for line in f:
            '''data.append(json.loads(line))''' # # # This was here before - changing it to keep only original text from wikipedia
            # # # This is my replacement, which checks that PassageEditID is 0
            sample = json.loads(line)
            if sample["PassageEditID"] == 0:
                data.append(sample)
                gold.append(sample)
            # # # End of my replacement

    t5_samples = [{"input": normalize_text(sample["sentence2"].replace("\n", " ")) + " \\n " + normalize_text(
        sample["sentence1"].replace("\n", " ")),
                   "answer": sample["label"]} for sample in data]

    OUTPUT_DIR = "./unifiedqa_formatted_data/"
    t5_filename = OUTPUT_DIR + filename.split("/")[-1].split(".")[-2] + "_unifiedqa.json"
    print(t5_filename)

    write_data(t5_samples, t5_filename)
    write_data(gold, filename) # # #
