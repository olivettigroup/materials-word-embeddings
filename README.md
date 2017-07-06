# Materials Science Word Embeddings

This repository provides a **trained** Word2Vec model trained across 640k+ materials science journal articles. (See Mikolov et al. 2013 for a description of the underlying Word2Vec algorithm.)

This trained model corresponds to the publication, "Machine-learned and codified synthesis parameters of oxide materials" in the journal *Scientific Data*.

We use the **gensim** implementation for Word2Vec: https://radimrehurek.com/gensim/

There is an example Python script included with the binary files, and the outputs of the script are provided below:

    from gensim.models import Word2Vec

    model = Word2Vec.load("../bin/word2vec_embeddings-SNAPSHOT.model")

    print model.wv.most_similar(positive=['LiFePO4'])
    >> [(u'Li4Ti5O12', 0.7679851055145264), (u'LiMn2O4', 0.7558220028877258), (u'LTO', 0.7144792079925537),
        (u'LiCoO2', 0.7069114446640015), (u'LiMnPO4', 0.69638991355896), (u'FePO4', 0.6824520826339722),
        (u'LFP', 0.6670607328414917), (u'LiNi0.5Mn1.5O4', 0.6622583866119385), (u'FeF3', 0.6584429740905762),
        (u'LiV3O8', 0.6576569080352783)]

    print model.wv.doesnt_match("calcine anneal sinter wash".split())
    >> wash

    print model.wv.similarity('titania', 'zirconia')
    >> 0.599160183811


## Usages

Word embeddings have rapidly become a standard technique for representing words in Natural Language Processing (NLP) research. Many trained models exist, although these are often trained across general-topic text (e.g., news articles). Here, we provide a Word2Vec model which has been trained specifically for the domain of materials science.
