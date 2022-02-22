from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>SUP BITCHES IT WORKS BTW</h1>"""

@app.route("/plots")
def plots():
    title = 'Plots!'
    this_could_be_a_png = ['This should be a png','but, it isnt..', 'b/c its a list']
    search_term = request.args.get('s', type=str)
    popularity_relation = request.args.get('pr', type=str)
    n = request.args.get('n', default=20, type=int)

    if search_term:
        return render_template("plots.html", title=title, png=this_could_be_a_png)
    else:
        return """
        <h1>No input = No output</h1>
        How to use:
        <br><code>http://[HOST]>/plots?s=yalla&pr=play.google.com&n=25 </code>
        <p><br>Search = s
        <br>Popularity relation = pr
        <br>Number of x = n
        </p>
        <h3>This is an example of how to use flask to pass url parameters.</h3>
        """


if __name__ == '__main__':
    app.run()