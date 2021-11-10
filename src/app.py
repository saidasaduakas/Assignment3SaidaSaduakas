from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route('/coin', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        if(language == 'coin'):
        	return '''
        	           <form method="POST">
               			<div><label><input type="text" name="language"></label></div>
               			<input type="submit" value="Check">
          				 </form>
                  	<h4>Bitcoin (BTC-USD) turns positive and marks another record high following better-than-expected inflation prints for October.
The largest digital token by market cap reached as high as $68.7K following the inflation data, and has since pulled back somewhat to $68.2K per token, though still elevated by 2.3% intra-day, according to data from CoinMarketCap.
In response to the highest level of inflation in 31 years, Twitter and Square CEO Jack Dorsey, a regular crypto advocate, says "now try measuring using the pre-1980 methodology,'" via Twitter.
Of course, Ethereum (ETH-USD) is making a similar move as BTC, rising 1.2% to $4.9K, a new all-time high.
Gold (XAUUSD:CR) +1.5% and Silver (XAGUSD:CUR) +3.2% are also gapping up in response to higher inflation prints even with nominal yields rising a bit, though in the past year alone, cryptos are dominating most asset classes.
Commodities are known to respond well to major monetary regime shifts, whether inflationary or deflationary, and it appears cryptos may be following the "safe haven" trend as well.
In October, JPMorgan strategists said inflation fears fueled bitcoin's rally.  {}</h1>'''


    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label><input type="text" name="language"></label></div>
               <input type="submit" value="Check">
           </form>'''

