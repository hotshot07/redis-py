import redis
from flask import Flask, app
import os 

app = Flask(__name__)


# Redis configurations
r = redis.Redis(
    host = "redis-service",
    port=80,
    password="foobared")


if not r.exists("value1"):
    r.set("value1", "0")
    
if not r.exists("value2"):
    r.set("value2", "0")


@app.route('/', methods=['GET'])
def main():
    
    value1 = int(r.get("value1").decode('utf-8'))
    value2 = int(r.get("value2").decode('utf-8'))
    
    return f"value1: {str(value1)}, value2: {str(value2)} \n"


@app.route('/inc1', methods=['GET'])
def inc1():
    r.incr("value1")
    
    value1 = int(r.get("value1").decode('utf-8'))
    
    return f"Value1: {str(value1)}\n"

@app.route('/inc2', methods=['GET'])
def inc2():
    r.incr("value2")
    
    value2 = int(r.get("value2").decode('utf-8'))
    
    return f"Value2: {str(value2)}\n"


@app.route('/dec1', methods=['GET'])
def dec1():
    r.decr("value1")
    
    value1 = int(r.get("value1").decode('utf-8'))
    
    return f"Value1: {str(value1)}\n"

@app.route('/dec2', methods=['GET'])
def dec2():
    r.decr("value2")
    
    value2 = int(r.get("value2").decode('utf-8'))
    
    return f"Value2: {str(value2)}\n"


@app.route('/reset', methods=['GET'])
def reset():
    
    r.set("value1","0")
    r.set("value2","0")
    
    value1 = int(r.get("value1").decode('utf-8'))
    value2 = int(r.get("value2").decode('utf-8'))
    
    return f"Values resetted. Value1: {str(value1)}, Value2: {str(value2)}\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





