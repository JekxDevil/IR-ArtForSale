# IR-ArtForSale
Project for Information Retrieval course

## Webpages:
- https://www.artsy.net/
- https://www.catawiki.com/en/c/85-art
- https://www.deviantart.com
- https://www.ugallery.com/
- https://www.patreon.com/
- https://society6.com/
- https://ko-fi.com/explore

## Setup

Download Poetry to handle the project, then run `poetry install` to install the dependencies.

Poetry creates a virtual environment for the project, to activate it select it as local interpreter in IDE or
run `poetry shell`

Follow [documentation](https://python-poetry.org/) for further info.

## Crawler

To run crawler:

```shell
scrapy crawl crawler-name -O file-data.json
```

## Django

To run: 
./manage.py runserver

## Indexer

Port address: 8001

Technologies:

- [PyTerrier](https://pyterrier.readthedocs.io/en/latest/index.html)
- [Pandas](https://pandas.pydata.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)

The indexer is a FastAPI application that exposes a REST API to query the index running in uvicorn ASGI server.

Backend and indexer are separated to allow for a more flexible deployment.

To run indexer with hot reload

```shell
uvicorn index:app --reload --port 8001
```

Run for production:

```shell
uvicorn index:app --port 8001
```

Run with
```shell
 poetry run python3 -m uvicorn index:app --reload --port 8001

```

## Troubleshooting

**Remember:** do not name files as popular python modules.

**Problem:** `ModuleNotFoundError: No module named '_bz2'`.
[solution](https://stackoverflow.com/questions/12806122/missing-python-bz2-module)

```shell
sudo apt-get install libbz2-dev
sudo cp /usr/lib/python3.10/lib-dynload/_bz2.cpython-310-x86_64-linux-gnu.so  /usr/local/lib/python3.10/
```

to activate env: source venv/bin/activate

**Problem**: 
Windows
- set `JAVA_HOME` in system environment variables
- `jvm.dll` not found, download jdk from oracle containing both JDK and JRE within

### DevOps

pip3 installs from PyPI an incompatible version of pyterrier `0.9.x` with latest pandas `2.0.0 >`

Spotted issue in `pyterrier/index.py` file from pyterrier module

https://stackoverflow.com/questions/76200452/error-while-iterating-over-dataframe-columns-entries-attributeerror-series

Solution: enforce newer pyterrier version `0.10.x` from repository

## References

- [HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
