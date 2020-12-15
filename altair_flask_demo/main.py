from flask import Flask
from flask import render_template
from flask import request

import altair as alt
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(f"index.html")


@app.route("/build_plot", methods=["POST"])
def build_plot():
    n = request.form.get("n_points", 200, type=int)
    max_bins = request.form.get("max_bins", 30, type=int)

    data = pd.DataFrame({'x': np.random.normal(size=n)})
    fig = alt.Chart(data).mark_bar().encode(
        alt.X("x:Q", bin=alt.Bin(maxbins=max_bins)),
        y='count()',
    )

    return fig.to_json()
