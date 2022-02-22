from flask import Flask, request, render_template
from matplotlib.pyplot import title
import loss_and_acc as graph
import plot as sisfalldata
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("base.html")

@app.route("/plots")
def plots():
    title = 'Plots!'
    #search_term = request.args.get('s', type=str)
    #popularity_relation = request.args.get('pr', type=str)
    #n = request.args.get('n', default=20, type=int)
    png_path = graph.makeGr()
    
    return render_template("plots.html", title=title, png=png_path)
    
@app.route("/datafromsisfall")
def morePlots():
    title = "Here you go"
    png_path = sisfalldata.getURL()
    print(png_path)
    return render_template("morePlot.html", title=title, png=png_path)




if __name__ == '__main__':
    app.run(port=5500)