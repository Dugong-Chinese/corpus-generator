import json
import hanlp
import inspect

from .corpus import Corpus


def parse(in_file_handle, out_json_handle, to_generator, args='{"tokenizer":"PKU_NAME_MERGED_SIX_MONTHS_CONVSEG","tagger":"CTB5_POS_RNN_FASTTEXT_ZH","tags_to_ignore":["PU","SYM","CD","NR"]}'):
    c = Corpus()
    c.load_json(out_json_handle)

    args = json.loads(args)

    tags_to_ignore = set(args['tags_to_ignore'])
    tokenizer = hanlp.load(args['tokenizer'])
    tagger = hanlp.load(getattr(hanlp.pretrained.pos, args['tagger']))
    pipeline = hanlp.pipeline() \
        .append(tokenizer, output_key='tokens') \
        .append(tagger, output_key='pos_tags')

    in_file_handle.seek(0)
    with in_file_handle as f:
        j = 0
        for chunk in to_generator(f):
            print('Chunk: {0}\r'.format(j), end="")
            j += 1
            res = pipeline(chunk)
            for i in range(len(res['tokens'])):
                if res['pos_tags'][i] not in tags_to_ignore:
                    c.add_word(res['tokens'][i])

    # c._debug_dump()
    c.dump_json(out_json_handle)
