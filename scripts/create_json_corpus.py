import json
import math
import os
import random
import re

random.seed(1234)
import glob

def build_dictionnary(name:str,
					  examples:list[tuple],
					  langs:list[str],
					  delimiter:str,
					  examples_number:int,
					  segments_number:int,
					  chars:int,
					  words:int):
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
	dictionnary = {}
	dictionnary["metadata"] = {
		"name": name,
		"delimiter": delimiter,
		"examples_number": examples_number,
		"segments": segments_number,
		"chars": chars,
		"words": words,
		"langs": langs
	}
	dictionnary["examples"] = []
	for example in examples:
		text, lang = example
		dictionnary["examples"].append({
			"example": text,
			"lang": lang
		})

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
	for example in corpus:
		text, lang = example
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
			current_text = [item.replace("\n", "") for item in f.readlines()]
			current_text = [item for item in current_text if item not in [None, ""]]
			current_text = [(clean_text(text, delimiter=delimiter), lang) for text in current_text]
			all_texts.extend(current_text)
	langs = list(set(langs))
	return all_texts, langs

def clean_text(example, delimiter):
	example = example.replace("“", "«")
	example = example.replace("”", "»")
	example = example.replace("—", "-")
	punctuation_regex = re.compile(rf"{delimiter}([\.,;\[\]:\?!’'”«\"»“/\-])")
	example = re.sub(punctuation_regex, rf"\1{delimiter}", example)
	spaces_regex = re.compile(fr"{delimiter}\s+")
	example = re.sub(spaces_regex, delimiter, example)
	if example[-1] == delimiter:
		example = example[:-1]

	return example



def create_corpus(delimiter:str, path:str, out_dir:str):
	all_texts = glob.glob(path)
	corpus, langs = read_texts(all_texts, delimiter)
	random.shuffle(corpus)
	proportion = {"train": .8, "test": .1, "dev": .1}
	train, dev, test = split_texts(corpus, proportion)
	train_stats = produce_stats(train, delimiter)
	dev_stats = produce_stats(dev, delimiter)
	test_stats = produce_stats(test, delimiter)
	corpus_stats = produce_stats(corpus, delimiter)

	corpus_dict = build_dictionnary(name="full",
									examples=corpus,
									langs=langs,
									delimiter=delimiter,
									examples_number=corpus_stats["num_examples"],
									segments_number=corpus_stats["num_segments"],
									chars=corpus_stats["num_chars"],
									words=corpus_stats["num_tokens"]
									)

	train_dict = build_dictionnary(name="train",
									examples=train,
									langs=langs,
									delimiter=delimiter,
									examples_number=train_stats["num_examples"],
									segments_number=train_stats["num_segments"],
									chars=train_stats["num_chars"],
									words=train_stats["num_tokens"]
									)

	dev_dict = build_dictionnary(name="dev",
									examples=dev,
									langs=langs,
									delimiter=delimiter,
									examples_number=dev_stats["num_examples"],
									segments_number=dev_stats["num_segments"],
									chars=dev_stats["num_chars"],
									words=dev_stats["num_tokens"]
									)

	test_dict = build_dictionnary(name="test",
									examples=test,
									langs=langs,
									delimiter=delimiter,
									examples_number=test_stats["num_examples"],
									segments_number=test_stats["num_segments"],
									chars=test_stats["num_chars"],
									words=test_stats["num_tokens"]
									)
	try:
		os.mkdir(out_dir)
	except FileExistsError:
		pass

	serialize_json(train_dict, out_dir + "/train.json")
	serialize_json(dev_dict, out_dir + "/dev.json")
	serialize_json(test_dict, out_dir + "/test.json")
	serialize_json(corpus_dict, out_dir + "/full.json")
	return langs

def serialize_json(dictionnary, path):
	with open(path, 'w') as f:
		json.dump(dictionnary, f)

def main():
	delimiter = "£"
	langs = create_corpus(delimiter=delimiter,
						  path='data/segmented/pre_split/*/segmented*.txt',
						  out_dir="data/segmented/split/multilingual")

	for lang in langs:
		try:
			os.mkdir(f"data/segmented/split/monolingual/{lang}")
		except FileExistsError:
			pass
		create_corpus(delimiter = delimiter,
					  path=f'data/segmented/pre_split/{lang}/segmented*.txt',
					  out_dir=f"data/segmented/split/monolingual/{lang}")

if __name__ == '__main__':
	main()