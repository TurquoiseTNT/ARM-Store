from flask import Flask
import os

app = Flask(__name__)

@app.route("/installapp/<appname>")
def installapp(appname):
    os.system("curl https://raw.githubusercontent.com/TurquoiseTNT/ARM-Store-Installers/main/" + appname + "/install || bash")
    return "APP INSTALLED <a href='tnt.is-a.dev/ARM-Store'><button>Back to App List</button></a>"
    
@app.route("/removeapp/<appname>")
def installapp(appname):
    os.system("curl https://raw.githubusercontent.com/TurquoiseTNT/ARM-Store-Installers/main/" + appname + "/uninstall || bash")
    return "APP REMOVED <a href='tnt.is-a.dev/ARM-Store'><button>Back to App List</button></a>"
