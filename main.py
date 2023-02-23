from flask import Flask,render_template
import pandas as pd
#commit: add url, endpoint for yearly and all data Sec31

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

@app.route('/api/v1/<station>')
def all_data(station):
    st_file=str(station).zfill(6)
    df=pd.read_csv(f'data_small/TG_STAID{st_file}.txt',skiprows=20,parse_dates=['    DATE'])
    # result=df.to_dict() #returns dict of columns
    result=df.to_dict(orient='records')# return list of dict of rows
    return(result)

@app.route('/api/v1/yearly/<station>/<year>')
def yearly(station,year):
    st_file=str(station).zfill(6)
    # df=pd.read_csv(f'data_small/TG_STAID{st_file}.txt',skiprows=20,parse_dates=['    DATE'])
    # result=df[df['    DATE'].str.startswith(str(year))] #will err out as date has been parsed to date type!!!
    df=pd.read_csv(f'data_small/TG_STAID{st_file}.txt',skiprows=20)
    df['    DATE']=df['    DATE'].astype(str) # convert dates to srt!!!
    result=df[df['    DATE'].str.startswith(str(year))]
    result=result.to_dict(orient='records')
    return(result)

if __name__=='__main__':
    # app.run(port=5001,debug=True) # specify alt port if running multiple flask apps!!!
    app.run(debug=True,port=5000)