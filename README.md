# roverapp

instalar python 3.11:


    sudo apt install software-properties-common

    sudo add-apt-repository ppa:deadsnakes/ppa

    sudo apt update

    sudo apt install python3.11

    sudo apt install python3.11-dev python3.11-venv python3.11-distutils python3.11-gdbm python3.11-tk python3.11-lib2to3

Ambiente virtual

    python3.11 -m venv venv

    source venv/bin/activate

Instalar dependencias:

    pip install -r requerements.dev

Executar:

    python3 ./src/main.py testefile.txt

Testes:

    pytest --cov -v --cov-report html:cov_html