"""Class encapsulating the corpus which keeps tracks of frequencies"""
import json
import traceback
import datetime
from functools import cmp_to_key


class Corpus:
    def __init__(self):
        # a very fancy wrapper for a dict ;)
        self.freqs = {}

    def load_json(self, json_file_handle):
        print("Attempting to load freqs from JSON if exists")
        # seek to the beginning of the file handle
        json_file_handle.seek(0)
        _json = json_file_handle.read()
        try:
            data = json.loads(_json)
            for word in data['words']:
                self.freqs[word['w']] = word['f']
        except:
            traceback.print_exc()

    def _debug_dump(self):
        print(self.freqs)

    def dump_json(self, json_file_handle):
        # erase all and then dump again for now
        _total_unq_words = len(self.freqs)
        _total_words = sum(self.freqs.values())
        res = {'date': datetime.datetime.now().isoformat(),
               'total_unique_words': _total_unq_words, 'total_words': _total_words}
        res['words'] = []
        for word in self.freqs:
            res['words'].append(
                {'w': word, 'f': self.freqs[word], 'p': self.freqs[word] / _total_words})

        def cmp_freq_desc(word1, word2):
            return word2['f'] - word1['f']
        res['words'].sort(key=cmp_to_key(cmp_freq_desc))
        json_file_handle.seek(0)
        json_file_handle.truncate()
        json_file_handle.write(json.dumps(res, indent=2, ensure_ascii=False))

    def add_word(self, word):
        if word not in self.freqs:
            self.freqs[word] = 1
        else:
            self.freqs[word] += 1
