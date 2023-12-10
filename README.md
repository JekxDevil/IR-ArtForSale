# Art For Sale
Project for Information Retrieval course.

Search engine to display for sale artworks. 
Around 8,500k~ documents indexed from art selling related [websites](#webpages), 
served in a [user-friendly](#user-evaluation) interface.

## Features
- Simple:
  - Result presentation
  - Filtering
- Complex:
  - Automatic recommendation

## Webpages
- https://www.artsy.net/
- https://www.artfinder.com/
- https://www.saatchiart.com/

## Setup
Download 
[Poetry](https://python-poetry.org/)
to handle the project dependencies.

Poetry creates a virtual environment for the project, to activate it select it as local interpreter in IDE or
run `poetry shell` in the terminal to join the poetry environment.

Run `poetry install --no-root` to install the dependencies from within the virtual env.

All commands assume dependencies are installed in your python virtual environment e.g. poetry env, venv, etc

## Crawler
Web crawling feature uses the 
[Scrapy](https://scrapy.org/)
open source Python framework for extracting data in a fast, simple and extensible way. 

The [webpages](#webpages) are crawled by the spiders, which scrapy the web pages and get
documents out of every post regarding selling art with its major info:
- author
- title
- price
- description
- categories
- image url reference
- post url reference

the crawler project is in `crawler/`.

To run a website crawler, got into `crawler/` directory and run:
```shell
scrapy crawl crawler-name -O file-data.json
```

## Indexer
The indexer is a microservice using a FastAPI application exposing a REST API running in uvicorn
[ASGI](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
server at port `8001`.

Technologies:
- [PyTerrier](https://pyterrier.readthedocs.io/en/latest/index.html)
- [Pandas](https://pandas.pydata.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)

The inverted index creation process:
- load the list of document results in json format given from crawlers
- convert the json entries into a pandas dataframe
- index it with Pyterrier DFIndexer class to generate the inverted index
- retrieve docs with Batch using _BM25_ model

Functionalities offered are:
- query the indexer, GET req.
- regenerate the inverted index, POST req

Backend and indexer are separated to allow for a more flexible deployment
and separation of concerns in microservices architecture infrastructure.

To run indexer with hot reload, get into `crawler/` directory and run:
```shell
uvicorn index:app --reload --port 8001
```

## Backend
Django.

To run the backend with hot reload, run the python script inside the `backend/` folder: 
```shell
./manage.py runserver
```

## Frontend 
Vuejs, vite, typescript

To run the frontend with hot reload:
```shell
yarn run dev
```

## User Evaluation
SUS

## Troubleshooting
**Remember:** do not name files as popular python modules e.g. pyterrier

**Problem:** `ModuleNotFoundError: No module named '_bz2'`.
[solution](https://stackoverflow.com/questions/12806122/missing-python-bz2-module)

```shell
# beware of path assumptions made here for python version and distro
sudo apt-get install libbz2-dev
sudo cp /usr/lib/python3.10/lib-dynload/_bz2.cpython-310-x86_64-linux-gnu.so  /usr/local/lib/python3.10/
```

**Problem**: common MS Windows issues
- set `JAVA_HOME` in system environment variables for Pyterrier lookup
- `jvm.dll` not found, download jdk from oracle containing both JDK and JRE

### DevOps
pip3 installs from PyPI an incompatible version of pyterrier `0.9.x` with latest pandas `2.0.0 >`:
spotted issue in `pyterrier/index.py` file from pyterrier module because
using a deprecated API call on pandas dataframe

https://stackoverflow.com/questions/76200452/error-while-iterating-over-dataframe-columns-entries-attributeerror-series

Solution: enforce newer pyterrier version `0.10.x` from repository

## References

- [HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [Pyterrier repository](https://github.com/terrier-org/pyterrier.git)
