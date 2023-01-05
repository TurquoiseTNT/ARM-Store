from flask import Flask
import os

app = Flask(__name__)

@app.route("/installapp/<appname>")
def installapp(appname):
    os.system("curl https://raw.githubusercontent.com/TurquoiseTNT/ARM-Store-Installers/main/" + appname + "/install || bash")
    return "APP INSTALLED"
    
@app.route("/removeapp/<appname>")
def installapp(appname):
    os.system("curl https://raw.githubusercontent.com/TurquoiseTNT/ARM-Store-Installers/main/" + appname + "/uninstall || bash")
    return "APP UNINSTALLED"
