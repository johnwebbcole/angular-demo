#AngularJS Demo
This is a simple demo showing a Python Tornado app with AngularJS

## Prerequisite
You will need [Python](http://www.python.org/download/) and [virtualenv](http://www.virtualenv.org/en/latest/) installed.  You'll need [MongoDB](http://www.mongodb.org/downloads) to run a local database.  *Note*: no database creation scripts are included.  You'll need to populate your database.

## Installation
Clone the demo repository. And configure `virtualenv`.

```
git clone https://github.com/johnwebbcole/angular-demo.git
cd angular-demo
virtualenv venv --python=python2.7
. venv/bin/activate
pip install tornado
pip install pymongo
```

All of the client libraries are installed with [Bower](http://bower.io).  Bower requires [Node](http://nodejs.org) and [git](http://git-scm.com).  Once these are installed, you can have bower install the client libraries.

```
bower install
```
## Running

Just run demo.py.

```
python demo.py
```

Then open [http://localhost:8888/static/index.html](http://localhost:8888/static/index.html) with your browser of choice.
