fileTransfer
=======
Python-based version of fileTransfer 
This project includes unittest and coverage report

Getting Started
===============
This project is running on Windows 10 using Ubuntu 18.04 app and Python 3.6

Prerequisites
=============
Make git repository directory from your home directory, setup fileTransfer remote, 
pull fileTransfer from master and Export your python src code path so that game 
will pick up the fileTransfer package.

cd
mkdir -p git/fileTransfer
cd git/fileTransfer
git init
git remote add fileTransfer https://github.com/morrisfd/fileTransfer.git
git pull fileTransfer master
export PYTHONPATH=$PYTHONPATH:~/git/fileTransfer/src

To run test.sh you will need to install pip3 and coverage.
    1. pip3 
         sudo apt install python3-pip
    2. coverage
         pip3 install coverage

To run pylint install from pip3
    1. pylint
        pip3 install pylint

Running the tests and coverage report
=====================================
From the root directory ("~/git/fileTransfer") run the test.sh script. This will run all unit test and give a coverage report.

cd ~/git/fileTransfer
./test.sh

Running individual tests
========================
From the tests directory ("~/git/fileTransfer/tests") run each test with pylint

cd ~/git/fileTransfer/tests
./test_mft.py

Running pylint (source-code, bug and quality checker for Python)
========================
cd ~/git/fileTransfer/src/fileTransfer
pylint file_manager.py 
pylint logger.py
pylint utility.py
pylint xml_parser.py
