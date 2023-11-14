import pandas as pd
import json
import pyterrier as pt


def run():
    if not pt.started():
        pt.init()

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


if __name__ == "__main__":
    run()
