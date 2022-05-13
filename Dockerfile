FROM appdynamics/machine-agent:alpine-latest

RUN apk add python3

WORKDIR /opt/appdynamics/monitors/PythonSelfMonitoring

RUN python3 -m venv .venv

ADD requirements.txt .
ADD monitor.xml .
ADD python_self_monitoring.sh .
ADD self_monitoring.py .
ADD config.ini .
ADD apis/account.py ./apis/
ADD apis/application.py ./apis/

RUN . /opt/appdynamics/monitors/PythonSelfMonitoring/.venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt