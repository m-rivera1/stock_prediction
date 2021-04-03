from flask import Flask, render_template
from datetime import datetime


#-----------------------------------------------#
#              Initialize the app               #
#-----------------------------------------------#
app = Flask(__name__, static_folder="static")

#-----------------------------------------------#
#              Global Variables                 #
#-----------------------------------------------#


#-----------------------------------------------#
#                   Routes                      # 
#-----------------------------------------------#

@app.route("/")
def routes():

    return render_template("index.html")





if __name__ == '__main__':
    app.run(debug=True)