FROM python:3.13.2

# for test environment to run with the same ids than local user
# to be able to mount local file system and view logs as local user
ARG UID=1000
ARG GID=1000

USER root

WORKDIR /app

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# only for test enviroment
RUN useradd -m -r -u $UID appuser
RUN groupmod -g $GID appuser

# Now copy in our code, and run it
COPY src/ .

RUN mkdir /app/logs

# only for test enviroment
RUN chown -R $UID:$GID /app

# only for test enviroment
USER appuser

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
