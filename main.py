from flask import Flask,render_template
import pandas as pd
#commit: show stations table on homepage Sec31

app=Flask(__name__)# to enable????

stations=pd.read_csv('data_small/stations.txt',skiprows=17)
stations=stations[['STAID','STANAME                                 ']]

# @means this is decorator and it decorates the fn below!!!
@app.route('/')
def home():
    return(render_template('home.html',data=stations.to_html())) ## kwargs!!!

@app.route('/api/v1/<station>/<date>')#get args from url!!
def about(station,date):
    st_fill=str(station).zfill(6) #fillnum with leading zeros!!!
    df=pd.read_csv(f'data_small/TG_STAID{st_fill}.txt',skiprows=20,parse_dates=['    DATE'])
    temparature=df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    return({'station':station,
            'date':date,
            'temparature':temparature})

if __name__=='__main__':
    # app.run(port=5001,debug=True) # specify alt port if running multiple flask apps!!!
    app.run(debug=True,port=5000)