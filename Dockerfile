FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src .
EXPOSE 5000
ENTRYPOINT [ "python3", "app.py"]