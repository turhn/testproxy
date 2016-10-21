FROM python:3.5
RUN pip install flask
COPY ./run.py /run.py
EXPOSE 5000
CMD python /run.py
