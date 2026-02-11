from flask import Flask, render_template

#app=Flask()
app=Flask(__name__)

@app.route('/')
def home():   
     username ="SOWMYA"
     hobbies = ["Reading","Sleeping","Eating"]
     return render_template('index.html', username=username, hobbies = hobbies)


if __name__=="__main__":
    app.run(debug=True)