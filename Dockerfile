FROM python:3.10.5
WORKDIR /filmIndustry
COPY ./requirements.txt /filmIndustry/requirements.txt

RUN pip install --no-cache-dir -r /filmIndustry/requirements.txt

COPY ./app /filmIndustry/app
# Add a new user "movies" with user id 8877
RUN useradd -u 8877 movies
# Change to non-root privilege
RUN chown -R movies:movies /filmIndustry/
USER movies
#CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8401"]
CMD ["sh", "-c", "sleep 3 ; uvicorn app.main:app --reload --host 0.0.0.0 --port 8401"]
