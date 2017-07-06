from gensim.models import Word2Vec

model = Word2Vec.load("../bin/word2vec_embeddings-SNAPSHOT.model")

print model.wv.most_similar(positive=['LiFePO4'])
print model.wv.doesnt_match("calcine anneal sinter wash".split())
print model.wv.similarity('titania', 'zirconia')
