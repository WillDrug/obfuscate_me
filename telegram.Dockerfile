FROM python:3.6
ADD . /
RUN pip install -r telegram_requirements.txt
ENV SECRET=${SECRET}
CMD python inline_telegram.py