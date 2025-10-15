import json
import sys

def main():
	filepath = sys.argv[1]
	with open(filepath) as f:
		as_json = json.load(f)
	metadata = as_json["metadata"]
	delimiter = as_json["metadata"]["delimiter"]
	examples = as_json["examples"]
	langs = set([example["lang"] for example in examples])
	out_dict = {lang:[] for lang in langs}
	for example in examples:
		lang = example["lang"]
		out_dict[lang].append(example)


	for lang, examples in out_dict.items():
		final_dict = {"metadata": {"delimiter": delimiter},
					  "examples": examples }
		with open(f"data/segmented/split/monolingual/{lang}/{lang}_test_v2.json", "w") as f:
			json.dump(final_dict, f)

if __name__ == '__main__':
    main()