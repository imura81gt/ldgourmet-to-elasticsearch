
DESCRIPTION
-------------

* DATA SOURCE: tar.gz on Github (https://github.com/livedoor/datasets)
* ETL: digdag + embulk
* DATA STORE: Elasticsearch


SETUP for MAC
-------------

```
pip install pipenv
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
pipenv install
pipenv shell
```

RUN
-------------

running all tasks

```
digdag run ldgourmet.dig
```

If you run tasks once, you can skip the download task after second time.

```
digdag run --start +transform ldgourmet.dig
```


