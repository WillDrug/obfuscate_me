FROM python:3.6
ADD . /
RUN pip install -r requirements.txt
ENV SECRET=${SECRET}
CMD python inline_telegram.py