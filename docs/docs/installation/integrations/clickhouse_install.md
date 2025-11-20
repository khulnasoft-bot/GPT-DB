# ClickHouse

In this example, we will show how to use the ClickHouse as in GPT-DB Datasource. Using a column-oriented database to implement Datasource can, to some extent, alleviate the uncertainty and interpretability issues brought about by vector database retrieval.

### Install Dependencies

First, you need to install the `gptdb clickhouse datasource` library.

```bash
uv sync --all-packages \
--extra "base" \
--extra "datasource_clickhouse" \
--extra "rag" \
--extra "storage_chromadb" \
--extra "gptdbs"
```

### Prepare ClickHouse

Prepare ClickHouse database service, reference-[ClickHouse Installation](https://clickhouse.tech/docs/en/getting-started/install/).

Then run the following command to start the webserver:
```bash
uv run gptdb start webserver --config configs/gptdb-proxy-openai.toml
```

Optionally, you can also use the following command to start the webserver:
```bash
uv run python packages/gptdb-app/src/gptdb_app/gptdb_server.py --config configs/gptdb-proxy-openai.toml
```

### ClickHouse Configuration

<p align="left">
  <img src={'https://github.com/user-attachments/assets/b506dc5e-2930-49da-b0c0-5ca051cb6c3f'} width="1000px"/>
</p>

