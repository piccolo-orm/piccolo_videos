# Many-To-Many Demo

Here is the [video](https://www.youtube.com/watch?v=J9YFt8Hxm4I).

## Setup

First create the database with the credentials given in `piccolo_conf.py`.

Then run the following:

```bash
pip install -r requirements.txt
piccolo migrations forwards all
piccolo music load_data
piccolo user create
python main.py
```
