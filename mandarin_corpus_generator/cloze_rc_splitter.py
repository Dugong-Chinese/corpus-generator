"""
A sample module that turns a stream of a file in the format of
cft.test.auto or cft.test.human ( https://github.com/ymcui/Chinese-Cloze-RC )
into a generator.

This file format is trivial.
"""


def to_generator(stream):
    delin = '||| '
    stream.seek(0)
    while True:
        l = stream.readline()
        if not l:
            break
        # strip the leading [number ||| ]
        l = l[l.find(delin) + len(delin):]
        # 5 ||| 伞包 的 颜色 哪些 ？ 红 的 、 XXXXX 、 蓝 的 、 绿 的 。 ||| 黄的
        # replace the XXXXX (since the original purpose was essentially to train an ML model to 填空)
        # with the answer at the end (that is again delin. with |||)
        xxxxx_idx = l.find('XXXXX')
        ans_idx = l.find(delin)

        if xxxxx_idx > -1 and ans_idx > -1:
            ans = l[ans_idx + len(delin):]
            l = l[:ans_idx]
            l = l.replace('XXXXX', ans)
        else:
            l = l.replace('|||', '')
        l = ''.join(l.split())
        yield l
