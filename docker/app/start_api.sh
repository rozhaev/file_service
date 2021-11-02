/.venv/bin/gunicorn src.api.main:app -b 0.0.0.0:8081 -k uvicorn.workers.UvicornWorker -c /gunicorn_conf.py -w 8
