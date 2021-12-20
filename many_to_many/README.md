# Many-To-Many Demo

First create the database with the credentials given in `piccolo_conf.py`.

Then run the following:

```bash
pip install -r requirements.txt
piccolo migrations forwards all
piccolo music load_data
piccolo user create
python main.py
```
