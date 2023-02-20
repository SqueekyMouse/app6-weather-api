from flask import Flask,render_template
#commit: Initial commit Sec29

app=Flask('Website')

# @means this is decorator and it decorates the fn below!!!
@app.route('/home') #this is connected to the function below!!!
def home():
    return(render_template('tutorial.html')) #page need to be in templates folder!!!

@app.route('/about/') #this is connected to the function below!!!
def about():
    return(render_template('about.html')) #page need to be in templates folder!!!

app.run(debug=True) # debug to see html errors!!!