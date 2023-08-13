# Author: Sakthi Santhosh
# Created on: 13/08/2023
from flask import redirect, render_template, url_for

from app import app_handle, redis_handle

@app_handle.route('/')
def index_handle():
    return render_template("index.html", counter=redis_handle.get("counter"))

@app_handle.route("/incr")
def incr_handle():
    redis_handle.incr("counter")
    return redirect(url_for("index_handle"))
