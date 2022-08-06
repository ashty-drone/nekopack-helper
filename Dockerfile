FROM ashdroid4/nekopack-helper:fitpack

COPY . .

RUN pip3 install -r requirements.txt && pip3 install python-dotenv

CMD ["python3", "helper_script"]
