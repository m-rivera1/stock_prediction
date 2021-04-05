from flask import Flask, request, render_template, redirect, url_for
import stockModel


#-----------------------------------------------#
#              Initialize the app               #
#-----------------------------------------------#
app = Flask(__name__, static_folder="static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

#-----------------------------------------------#
#                   Routes                      # 
#-----------------------------------------------#

@app.route("/")
def default():

    return render_template("index.html")

@app.route("/get-stock",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        ticker = request.form['search']
        dates = stockModel.getStockDates(ticker)
        closeData = stockModel.getStockClose(ticker)
        companyName = stockModel.getCompanyName(ticker)


    return render_template("index.html", labels=dates, data=closeData, cName=companyName)



if __name__ == '__main__':
    app.run(debug=True)