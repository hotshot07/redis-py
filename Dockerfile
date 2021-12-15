FROM python
COPY app.py /app.py
RUN pip install flask 
RUN pip install redis