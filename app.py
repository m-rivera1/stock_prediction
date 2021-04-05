from flask import Flask, render_template
import stockModel


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
def home():
    dates = stockModel.getStockDates('FB')
    closeData = stockModel.getStockClose('FB')
    companyName = stockModel.getCompanyName('FB')
    # print(dates)
    return render_template("index.html", labels=dates, data=closeData, cName=companyName)

@app.route("/Project Scope")
def info():
    return render_template("")





if __name__ == '__main__':
    app.run(debug=True)