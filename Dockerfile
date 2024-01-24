FROM python:3.8
RUN pip install streamlit
COPY src/* /app/
COPY img/* /app/img/neurona.jpg


WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py"]