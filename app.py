from flask import Flask, request,render_template
from src.getData import getTweets,getNews, getHeadlines
from src.analysis import sentimentAnalysis, generateWordCloud, generateGraph, getImgPath, getGraphPath


app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        keyword = request.form.get('keyword')
        print(keyword)
        if not keyword:
            fulldata = getHeadlines()
        else:
            fulldata = getNews(keyword)
        data = [d[0] for d in fulldata]
        samples = fulldata[:5]
        results = sentimentAnalysis(data)
        generateWordCloud(data, keyword)
        generateGraph(results)
        
        img_path = getImgPath()
        graph_path = getGraphPath()
        return render_template('index.html', img_path=img_path, graph_path=graph_path, results=results, samples=samples, keyword=keyword, number=len(data))
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)