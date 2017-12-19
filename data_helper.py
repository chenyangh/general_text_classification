import operator


class data_helper():

    def construct_vocab(self, lines, vocab_size):
        """Construct a vocabulary from tokenized lines."""
        vocab = {}
        for line in lines:
            for word in line:
                if word not in vocab:
                    vocab[word] = 1
                else:
                    vocab[word] += 1

        # Discard start, end, pad and unk tokens if already present
        if '<s>' in vocab:
            del vocab['<s>']
        if '<pad>' in vocab:
            del vocab['<pad>']
        if '</s>' in vocab:
            del vocab['</s>']
        if '<unk>' in vocab:
            del vocab['<unk>']

        word2id = {
            '<s>': 0,
            '<pad>': 1,
            '</s>': 2,
            '<unk>': 3,
        }

        id2word = {
            0: '<s>',
            1: '<pad>',
            2: '</s>',
            3: '<unk>',
        }

        sorted_word2id = sorted(
            vocab.items(),
            key=operator.itemgetter(1),
            reverse=True
        )

        sorted_words = [x[0] for x in sorted_word2id[:vocab_size]]

        for ind, word in enumerate(sorted_words):
            word2id[word] = ind + 4

        for ind, word in enumerate(sorted_words):
            id2word[ind + 4] = word

        return word2id, id2word
