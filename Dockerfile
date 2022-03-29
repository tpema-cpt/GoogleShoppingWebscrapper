FROM python:3.7

WORKDIR /main
COPY . .

RUN pip install -r requiremenst.txt

ENTRYPOINT ["python"]
CMD ["main.py"]