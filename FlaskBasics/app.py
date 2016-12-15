#initializes the Flask as app
from flask import Flask
app = Flask(__name__)

#never leave this on production or someone will break the site
#puts us in the flask debug mode
app.debug = True

#when we are at slash. use hello world
@app.route("/")
def hello():
	return "Hello World!"

#if this is the thing we are running the application from, run it
if __name__ == "__main__":
	app.run()
	#app.run(0.0.0.0) #will run your site on all public IPs. No need to do this

