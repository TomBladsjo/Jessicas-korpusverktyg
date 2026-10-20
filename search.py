import argparse
import os



def parsefile(path):
    with open(path, 'r') as f:
        lines = [line.split() for line in f]
    forms, tags, lemmas, sents = [], [], [], []
    f, t, l, s = [], [], [], []
    for line in lines:
        if len(line):
            form, tag, lemma = line
            f.append(form), t.append(tag), l.append(lemma), s.append(line)
        else: 
            forms.append(f), tags.append(t), lemmas.append(l), sents.append(s)
            f, t, l, s = [], [], [], []
    return {'form': forms, 'tag': tags, 'lemma': lemma, 'sents': sents}


def loadfiles(dir):
    corpus = {}
    for file in os.listdir(dir):
        corpus[file] = parsefile(os.path.join(dir, file))
    return corpus


def compare_match(col, start, search):
    for i in range(len(search)):
        if col[start+i].lower() != search[i]:
            return False
    return (start+i, start+len(search))

def compare_match_sent(sent, search):
    if len(search) > len(sent):
        return False
    for i in range(len(sent)-(len(search)-1)):
        if compare_match(sent, i, search):
            return True
    return False


def search_col(col, search):
    search = search.lower().split(', ')
    matches = []
    for i in range(len(col)):
        m = compare_match_sent(col[i], search)
        if m:
            matches.append(i)
    return matches

# def collect_matches(matches, lines):
#     return [lines[start-1:end] for start, end in matches]

def collect_matchsents(matches, sents):
    return [sents[m] for m in matches]


parser = argparse.ArgumentParser()
parser.add_argument('mapp', help='mappen där korpusfilerna ligger')
# parser.add_argument('taggar', help='skriv den sekvens av taggar du vill söka efter, separerade med kommatecken och mellanslag. exempel: PRO-N, VBDI, ADV')
args = parser.parse_args()

searchstr = input('Skriv den sekvens av taggar du vill söka efter, separerade med kommatecken och mellanslag. Avsluta med enter. \nExempel: PRO-N, VBDI, ADV\nExempel: CONJ\n\nsökning: ')
name = '_'.join(searchstr.split(', '))
resultdir = f'./resultat/'

corpus = loadfiles(args.mapp)

os.makedirs(resultdir, exist_ok=True)

allmatches = {}

totmatches = 0

for c in corpus.keys():
    tags = corpus[c]['tag']
    sents = corpus[c]['sents']
    matches = collect_matchsents(search_col(tags, searchstr), sents)
    print(f'hittade {len(matches)} träffar i fil {c}')
    totmatches += len(matches)
    allmatches[c] = matches

print(f'\nHittade totalt {totmatches} träffar\n')

print(f'skriver resultat i fil {os.path.join(resultdir, name)}')

with open(os.path.join(resultdir, name), 'w') as f:
    for c in allmatches.keys():
        f.write(f'\nFil: {c}\n\n')
        for sent in allmatches[c]:
            for line in sent:
                f.write('\t'.join(line))
                f.write('\n')
            f.write('\n\n')

print('färdig!')








