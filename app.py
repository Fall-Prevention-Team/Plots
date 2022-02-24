from flask import Flask, request, render_template
from matplotlib.pyplot import title
import loss_and_acc as graph
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("base.html")

@app.route("/plots")
def plots():
    title = 'Here are examples of different plots where each plot in a graph represent an X,Y & Z coordinates'
    png_path = graph.makeGr()
    
    return render_template("plots.html", title=title, png=png_path)
    
@app.route("/datafromsisfall")
def morePlots():
    import plot as sisfalldata
    title = "Here you go"
    png_path = sisfalldata.getURL()
    print(png_path)
    return render_template("morePlot.html", title=title, png=png_path)




if __name__ == '__main__':
    app.run(port=5500)