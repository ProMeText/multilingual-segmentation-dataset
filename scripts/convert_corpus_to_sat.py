import json
import shutil
from collections import OrderedDict

def create_corpus(file_to_convert, delimiter="£"):
	with open(file_to_convert, "r") as input_file:
		json_file = json.load(input_file, object_pairs_hook=OrderedDict)
	all_examples = []
	for example in json_file['examples']:
		text = example['example'].strip()
		as_split = [item.strip() for item in text.split(delimiter) if item != ""]
		all_examples.extend(as_split)

	return all_examples

if __name__ == '__main__':
	train = "data/training_data/segmented/split/multilingual/train.json"
	test = "data/training_data/segmented/split/multilingual/test.json"
	dev = "data/training_data/segmented/split/multilingual/dev.json"
	out_dir = "data/SaT/"
	train_corpus = create_corpus(file_to_convert=train)
	dev_corpus = create_corpus(file_to_convert=dev)
	dictionnary = \
		{
			"language_code": {
				"sentence":
					{"dataset":
						{
							"meta":
								{
									"train_data": train_corpus
								},
							"data": dev_corpus
						}
					}
			}
		}
	with open("data/SaT/corpus.json", "w") as output_file:
		json.dump(dictionnary, output_file)

	shutil.copy(test, f"data/SaT/test.json")
	print("Done")