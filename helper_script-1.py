from sys import exit
from os import environ
from pathlib import Path
from subprocess import run
from os.path imporet dirname
from dotenv import load_dotenv

username = environ.get("GITHUB_ACTOR")
password = environ.get("github_password")
repo = environ.get("GITHUB_REPOSITORY")
repo_name = str(environ.get("GITHUB_REPOSITORY"))[len(username)+1:]

script = """\
git clone https://{}:{}@github.com/{}
mv {} nekopack
"""

script = script.format(username, password, repo, repo_name)

run(script, shell=True, check=True)
environ["PROGRESS_FORWARD"] = "true"

script = """\
cd nekopack
python3 start
"""

if environ.get("run_docker"):
  run(script, shell=True, check=True)
  
load_dotenv("nekopack/config.env")

script = """\
docker image build -t catuserbot .
docker image run catuserbot
"""

path = Path(dirname(__file__))
for file in path.iterdir():
  if file.name == "Dockerfile":
    environ["run_docker"] = True
    run(script, shell=True, check=True)
    exit()

script = """\
wget https://raw.githubusercontent.com/ashty-drone/nekopack-helper/main/Dockerfile
"""
      
if not environ.get("DATABASE_URL"):
  run(script, shell=True, check=true)
  environ["PROGRESS_FORWARD"] = "false"
