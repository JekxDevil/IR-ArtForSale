import json
from ..models import Document
import pandas as pd


def populate_database():
    print("POPULATING DB")
    with open('../../../crawler/saatchiart.json') as f:
        data = json.load(f)
        df = pd.DataFrame(data)
        df['docno'] = [f'd{i + 1}' for i in range(len(df))]  # add docno column to doc entries
        df.info()

    # Loop through DataFrame rows and create Document objects
    for index, row in df.iterrows():
        new_doc = Document(
            title=row['title'],
            author=row['author'],
            description=row['description'],
            url=row['url'],
            image=row['img'],
            tags=row['tags'],
            price=row['price'],
            docno=row['docno'],
        )
        new_doc.save()


if __name__ == "__main__":
    populate_database()
