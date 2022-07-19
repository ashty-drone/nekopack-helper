FROM ashdroid4/nekopack-helper:fitpack

RUN wget https://raw.githubusercontent.com/ashty-drone/nekopack-helper/main/helper-script

CMD ["python3", "helper-script"]
