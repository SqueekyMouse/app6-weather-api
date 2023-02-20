from flask import Flask,render_template
#commit: flask name pages params json return Sec29

app=Flask(__name__)# to enable????

# @means this is decorator and it decorates the fn below!!!
@app.route('/')
def home():
    return(render_template('home.html')) 

@app.route('/api/v1/<station>/<date>')#get args from url!!
def about(station,date):
    # df=pandas.read_csv('')
    # temparature=df.station(date)
    temparature=23
    # return(str(temparature))
    return({'station':station,
            'date':date,
            'temparature':temparature})
    # return(render_template('about.html'))

if __name__=='__main__':
    app.run(debug=True)