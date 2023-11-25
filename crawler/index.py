"""
get postings:
index.getInvertedIndex().getPostings(pointer:LexiconEntry)

To search:
br = pt.BatchRetrieve(index, wmodel="Tf") #Alternative Models: "TF_IDF", "BM25"
br.search("best")
queries = pd.DataFrame([["q1", "blue best"], ["q2", "bright blue sky"]], columns=["qid", "query"])
br.transform(queries) <----- preferred

Retrieve model?
bm25 = pt.BatchRetrieve(index, wmodel="BM25")
"""
import pandas as pd
import json
import pyterrier as pt


def run():
    if not pt.started():
        pt.init()

    with open('saatchiart.json') as f:
        data = json.load(f)
        df = pd.DataFrame(data)
        df['docno'] = [f'd{i + 1}' for i in range(len(df))]
        df.info()
        pd_indexer = pt.DFIndexer('./index_saatchiart', overwrite=True)
        # index columns of dataframe
        index_ref = pd_indexer.index(df['author'], df['title'], df['description'], df['docno']) # add tags
        index = pt.IndexFactory.of(index_ref)
        print('Index stats: ', index.getCollectionStatistics().toString())
        print('lexicon: ')
        for kv in index.getLexicon():
            print(f'{kv.getKey()} -> {kv.getValue().toString()}')

    return


    with open('artsyresult.json') as f:
        data = json.load(f)

        # Use pd.json_normalize to convert the JSON to a DataFrame
        df = pd.json_normalize(data,
                               meta=['image', 'author', 'title', 'price', 'url'])

        # Add a 'docno' column to the DataFrame
        df['docno'] = [str(i) for i in range(1, len(df) + 1)]

        # Display the DataFrame
        print(df)

        # Specify the 'docno' column during indexing using DFIndexer
        indexer = pt.DFIndexer("./index_3docs", indexerType="basic", meta=["docno", "author", "title", "price", "url"], overwrite=True)
        index_ref = indexer.index(df['docno'], df)

        # Display the index reference
        print(index_ref)

        index = pt.IndexFactory.of(index_ref)
        type(index)
        print(index.getCollectionStatistics().toString())

        for kv in index.getLexicon():
            print("%s -> %s " % (kv.getKey(), kv.getValue().toString() ))

    with open('artfinderresult.json') as f:
        data = json.load(f)

        # Use pd.json_normalize to convert the JSON to a DataFrame
        df = pd.json_normalize(data,
                               meta=['image', 'author', 'title', 'price', 'description', 'tag'])

        # Add a 'docno' column to the DataFrame
        df['docno'] = [str(i) for i in range(1, len(df) + 1)]

        # Display the DataFrame
        print(df)

        # Specify the 'docno' column during indexing using DFIndexer
        indexer = pt.DFIndexer("./index_3docs", indexerType="basic", meta=["docno", 'image', 'author', 'title', 'price', 'description', 'tag'], overwrite=True)
        index_ref = indexer.index(df['docno'], df)

        # Display the index reference
        print(index_ref)

        index = pt.IndexFactory.of(index_ref)
        type(index)
        print(index.getCollectionStatistics().toString())

        for kv in index.getLexicon():
            print("%s -> %s " % (kv.getKey(), kv.getValue().toString() ))

    
if __name__ == "__main__":
    run()
