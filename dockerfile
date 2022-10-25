FROM python:slim
ENV TOKEN ='Укажите здесь свой TOKEN'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py