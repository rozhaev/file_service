FROM python:3.9-alpine as builder

RUN apk add --no-cache gcc g++ musl-dev libffi-dev openssl-dev make xvfb python3-dev postgresql-dev

ADD . .

ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

RUN pip install --no-cache-dir poetry
RUN poetry install

FROM  builder as api
COPY ./docker/app/start_api.sh /project/start.sh
RUN chmod +x /project/start.sh
CMD /project/start.sh


FROM  builder as worker
COPY ./docker/app/start_worker.sh /project/start.sh
RUN chmod +x /project/start.sh
CMD /project/start.sh