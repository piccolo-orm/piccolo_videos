# Making a powerful REST API, like GraphQL

Here is the [video](https://www.youtube.com/watch?v=OUvWn0GUDSI).

## Setup

### Install requirements

```bash
pip install -r requirements.txt
```

### Create Postgres database

See `piccolo_conf.py` for details. Then use `piccolo movies generate_data` to add some test data.

### Run server

```bash
python main.py
```

### Try out API

Go to `localhost:8000/docs`.
