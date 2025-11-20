# BM25 RAG

In this example, we will show how to use the Elasticsearch as in GPT-DB RAG Storage. Using a Elasticsearch database to implement RAG can, to some extent, alleviate the uncertainty and interpretability issues brought about by Elasticsearch database retrieval.

### Install Dependencies

First, you need to install the `gptdb elasticsearch storage` library.

```bash
uv sync --all-packages --frozen \
--extra "base" \
--extra "proxy_openai" \
--extra "rag" \
--extra "storage_elasticsearch" \
--extra "gptdbs"
````

### Prepare Elasticsearch

Prepare Elasticsearch database service, reference-[Elasticsearch Installation](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) .

### Elasticsearch Configuration


Set rag storage variables below in `configs/gptdb-bm25-rag.toml` file, let GPT-DB know how to connect to Elasticsearch.

```

[rag.storage]
[rag.storage.full_text]
type = "ElasticSearch"
uri = "127.0.0.1"
port = "9200"
```

Then run the following command to start the webserver:
```bash
uv run python packages/gptdb-app/src/gptdb_app/gptdb_server.py --config configs/gptdb-bm25-rag.toml
```

Optionally
```bash
uv run python packages/gptdb-app/src/gptdb_app/gptdb_server.py --config configs/gptdb-bm25-rag.toml
```

