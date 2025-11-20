# Introduction

This is the introduction to the GPT-DB API documentation. You can interact with the API through HTTP requests from any language, via our official Python Client bindings.

## Authentication
The GPT-DB API uses API keys for authentication. Visit your API Keys page to retrieve the API key you'll use in your requests.

Production requests must be routed through your own backend server where your API key can be securely loaded from an environment variable or key management service.

All API requests should include your API key in an Authorization HTTP header as follows:
    
    ```http
    Authorization: Bearer GPTDB_API_KEY
    ```
Example with the GPT-DB API curl command:

    ```bash
    curl "http://localhost:5670/api/v2/chat/completions" \
    -H "Authorization: Bearer $GPTDB_API_KEY" \
    ```
Example with the GPT-DB Client Python package:
    
    ```python
    from gptdb_client import Client

    GPTDB_API_KEY = "gptdb"
    client = Client(api_key=GPTDB_API_KEY)
    ```
Set the API Key in .env file as follows:
:::info note
API_KEYS - The list of API keys that are allowed to access the API. Each of the below are an option, separated by commas.
:::
```python
API_KEYS=gptdb
```

## Using the GPT-DB official Python Client

If you use Python, you should install the official GPT-DB Client package from PyPI:

```bash
pip install "gptdb-client>=0.7.1rc0"
```

## Using the OpenAI Python SDK

In some chat cases, you can use the OpenAI Python SDK to interact with the GPT-DB API. The GPT-DB API is compatible with the OpenAI API.

```bash
pip install openai
```