FROM python:3.10.12

WORKDIR /app

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#RUN useradd -m -r appuser && \
#   chown -R appuser /app

# Now copy in our code, and run it
COPY src/ .

RUN mkdir /app/logs

#RUN chown -R appuser:appuser /app

#USER appuser
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
