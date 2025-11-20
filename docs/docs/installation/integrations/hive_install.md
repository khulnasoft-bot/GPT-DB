# Hive

In this example, we will show how to use the Hive as in GPT-DB Datasource. Using Hive to implement Datasource can, to some extent, alleviate the uncertainty and interpretability issues brought about by vector database retrieval.

### Install Dependencies

First, you need to install the `gptdb hive datasource` library.

```bash
uv sync --all-packages \
--extra "base" \
--extra "datasource_hive" \
--extra "rag" \
--extra "storage_chromadb" \
--extra "gptdbs"
```

### Prepare Hive

Prepare Hive database service, reference-[Hive Installation](https://cwiki.apache.org/confluence/display/Hive/GettingStarted).

Then run the following command to start the webserver:
```bash

uv run python packages/gptdb-app/src/gptdb_app/gptdb_server.py --config configs/gptdb-proxy-openai.toml
```

Optionally, you can also use the following command to start the webserver:
```bash
uv run python packages/gptdb-app/src/gptdb_app/gptdb_server.py --config configs/gptdb-proxy-openai.toml
```

### Hive Configuration

<p align="left">
  <img src={'https://github.com/user-attachments/assets/40fb83c5-9b12-496f-8249-c331adceb76f'} width="1000px"/>
</p>

