FROM python:3.6
ADD . /
RUN pip install -r telegram_requirements.txt
CMD python inline_telegram.py