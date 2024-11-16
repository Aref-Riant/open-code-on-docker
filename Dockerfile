FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install torch~=2.5.0 --index-url https://download.pytorch.org/whl/cpu
RUN pip install transformers~=4.46.2
RUN pip install accelerate
RUN pip install sentencepiece

COPY firstrun.py .
RUN python3 firstrun.py

COPY entrypoint.py .
ENTRYPOINT ["python3","entrypoint.py"]
