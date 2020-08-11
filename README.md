# Corpus Generator

A simple tool to generate word/词语 frequencies from an input file.

### Usage
```
$ mandarin_corpus_gen --help
Usage: mandarin_corpus_gen [OPTIONS] COMMAND [ARGS]...

  Corpus generation tool for our Mandarin Learning App. Please run one of
  the subcommands below.

Options:
  --help  Show this message and exit.

Commands:
  extract   Extracts vocabulary frequencies from a plaintext file.
  json2csv  Converts the JSON progress file saved to a CSV (without...
```

```
$ mandarin_corpus_gen extract --help
Usage: mandarin_corpus_gen extract [OPTIONS]

  Extracts vocabulary frequencies from a plaintext file.

Options:
  -i, --in TEXT          Path to file in plaintext.  [required]
  -o, --out TEXT         Path to output JSON file containing the relative and
                         absolute frequencies and various other stats. Updates
                         if exists. Default: output.json

  -c, --chunker TEXT     Path to a module that contains a function which
                         chunks the input file up into syntactically correct
                         sentences. Example: ./cloze_rc_splitter.py
                         [required]

  --extractor-args TEXT  JSON string to pass to the extractor if supported.
  --help                 Show this message and exit.
```

### A sample command
Download and modify `mandarin_corpus_generator/cloze_rc_splitter.py` beforehand, and place it into your working directory.
```sh
$ mandarin_corpus_gen extract -i ~/path/to_plaintext_file.txt -o test.json -c ./cloze_rc_splitter.py
Attempting to load freqs from JSON if exists
Chunk: 19484
...
$ head test.json
{
  "date": "2020-08-11T16:05:48.270634",
  "total_unique_words": 9088,
  "total_words": 260885,
  "words": [
    {
      "w": "的",
      "f": 14466,
      "p": 0.055449719224945855
    },
```