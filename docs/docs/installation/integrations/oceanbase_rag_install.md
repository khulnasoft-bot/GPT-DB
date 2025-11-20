# OceanBase Vector RAG


In this example, we will show how to use the OceanBase Vector as in GPT-DB RAG Storage. Using a graph database to implement RAG can, to some extent, alleviate the uncertainty and interpretability issues brought about by vector database retrieval.


### Install Dependencies

First, you need to install the `gptdb OceanBase Vector storage` library.

```bash
uv sync --all-packages \
--extra "base" \
--extra "proxy_openai" \
--extra "rag" \
--extra "storage_obvector" \
--extra "gptdbs"
````

### Prepare OceanBase Vector

Prepare OceanBase Vector database service, reference[OceanBase Vector](https://open.oceanbase.com/) .


### OceanBase Configuration

Set rag storage variables below in `configs/gptdb-proxy-openai.toml` file, let GPT-DB know how to connect to OceanBase Vector.

```
[rag.storage]
[rag.storage.vector]
type = "oceanbase"
uri = "127.0.0.1"
port = "19530"
#username="gptdb"
#password=19530
```

Then run the following command to start the webserver:
```bash
uv run python packages/gptdb-app/src/gptdb_app/gptdb_server.py --config configs/gptdb-proxy-openai.toml
```

Optionally, you can also use the following command to start the webserver:
```bash
uv run python packages/gptdb-app/src/gptdb_app/gptdb_server.py --config configs/gptdb-proxy-openai.toml
```