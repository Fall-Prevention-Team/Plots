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
    
@app.route("/choosedata")
def loadpage():
    title = "DATA"
    
    return render_template("morePlot.html", title=title)


@app.route("/datafromsisfall", methods=['GET','POST'])
def loadgraph():
    import plot as sisfalldata
    fuck_this_shit = request.form.get('person-comp').split('.')
    list_of_png = sisfalldata.GetList(int(fuck_this_shit[0]), fuck_this_shit[1])

    return render_template("image_template.html", pngs=list_of_png)
    


if __name__ == '__main__':
    app.run(port=5500)