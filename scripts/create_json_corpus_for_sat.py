import json
import math
import os
import random
import re
import torch

random.seed(1234)
import glob

def build_dictionnary(name:str,
					  train_examples:list[tuple],
					  dev_examples:list[tuple],
					  test_examples:list[tuple]):
	"""
	This function builds the final corpus.
	:param name: The name of the corpus (test, train, dev).
	:param examples: the examples as a list of tuples (example, lang).
	:param langs: the list of languages codes.
	:param delimiter: the delimiter.
	:param examples_number: the number of examples.
	:param chars: the total number of characters.
	:param words: the total number of words.
	:return: the dictionnary
	"""
	dictionnary = \
	{
		"language_code": {
			"sentence":
				{"dataset":
				{
					"meta":
						{
							"train_data" : train_examples
						},
							"data" : dev_examples
				}
		}
		}
	}

	return dictionnary


def split_texts(corpus:list[tuple[str]], proportion:dict) -> (list, list, list):
	"""
	This function splits the corpus into training, dev and test sets.
	:param corpus: the corpus as a list of tuples (text, lang).
	:param proportion:
	:return:
	"""
	corpus_length = len(corpus)
	examples_in_train = math.floor(corpus_length * proportion["train"])
	examples_in_dev = math.floor(corpus_length * proportion["dev"])
	examples_in_test = math.floor(corpus_length * proportion["test"])

	train = corpus[:examples_in_train]
	dev = corpus[examples_in_train:examples_in_train+examples_in_dev]
	test = corpus[-examples_in_test:]


	return train, dev, test

def produce_stats(corpus:list[tuple[str]], delimiter:str) -> dict:
	"""
	This function produces the statistics to be added to the corpus metadata
	:param corpus:
	:return:
	"""
	delimiters_regex = re.compile(r"\s+|([\.“\?\!—\"/:;,\-¿«\[\]»])")
	num_tokens = 0
	num_chars = 0
	num_segments = 0
	num_examples = len(corpus)
	delimiters_number = 0
	for text in corpus:
		num_chars += len(text)
		num_segments += text.count(delimiter)
		num_tokens += len([item for item in re.split(delimiters_regex, text) if item is not None])
		delimiters_number += text.count(delimiter)
	return {"num_examples": num_examples,
			"num_segments": num_segments,
			"num_chars": num_chars,
			"num_tokens": num_tokens,
			"delimiters_number": delimiters_number}


def read_texts(paths, delimiter) -> list[tuple[str]]:
	all_texts = []
	langs = []
	for path in paths:
		print(path)
		lang = path.split('/')[-2]
		langs.append(lang)
		with open(path, 'r') as f:
			interm_list = []
			current_text = [item.replace("\n", "") for item in f.readlines()]
			current_text = [item for item in current_text if item not in [None, ""]]
			[interm_list.extend(clean_text(text, delimiter=delimiter).split(delimiter)) for text in current_text]
			all_texts.extend(interm_list)
	all_texts = [item for item in all_texts if item != ""]
	return all_texts

def clean_text(example, delimiter):
	example = example.replace("“", "«")
	example = example.replace("”", "»")
	example = example.replace("—", "-")
	punctuation_regex = re.compile(rf"{delimiter}([\.,;\[\]:\?!¿’'”«\"»“/\-])")
	example = re.sub(punctuation_regex, rf"\1{delimiter}", example)
	spaces_regex = re.compile(fr"{delimiter}\s+")
	example = re.sub(spaces_regex, delimiter, example)
	if example[-1] == delimiter:
		example = example[:-1]
	if re.search(punctuation_regex, example):
		clean_text(example, delimiter)
	return example



def create_corpus(delimiter:str, path:str, out_dir:str):
	all_texts = glob.glob(path)
	corpus = read_texts(all_texts, delimiter)
	random.shuffle(corpus)
	proportion = {"train": .8, "test": .1, "dev": .1}
	train, dev, test = split_texts(corpus, proportion)

	train_dict = build_dictionnary(name="train",
									train_examples=train,
									dev_examples=dev,
									test_examples=test,
									)

	os.makedirs(out_dir, exist_ok=True)
	print(f"Creating dir: {out_dir}")

	serialize_json(train_dict, out_dir + "/train.json")
	torch.save(train_dict,
		f"{out_dir}/dataset.pth")

def serialize_json(dictionnary, path):
	with open(path, 'w') as f:
		json.dump(dictionnary, f)

def main():
	delimiter = "£"
	create_corpus(delimiter=delimiter,
						  path='data/segmented/pre_split/*/segmented*.txt',
						  out_dir="data/SaT/")


if __name__ == '__main__':
	main()