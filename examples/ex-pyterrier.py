import pyterrier as pt
import pandas as pd


def run():
    if not pt.started():
        pt.init()

    docs_df = pd.DataFrame(
        [
            ["d1", "this is the first document of many documents"],
            ["d2", "this is another document"],
            ["d3", "the topic of this document is unknown"],
        ],
        columns=["docno", "text"],
    )

    docs_df = pd.DataFrame(
        [
            ["d1", "the bright blue butterfly hangs on the breeze"],
            ["d2", "it is best to forget the great sky and to retire from every wind"],
            ["d3", "under blue sky in bright sunlight one need not search around"],
        ],
        columns=["docno", "text"],
    )

    print(docs_df)

    indexer = pt.DFIndexer("./index_3docs", overwrite=True)
    # deprecated index_ref = indexer.index(docs_df["text"], docs_df["docno"])
    # index_ref.toString()
    #index = pt.IndexFactory.of(index_ref)


if __name__ == "__main__":
    run()
