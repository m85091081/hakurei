#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 0muMDAU Server
from muMDAU_app import app
import logging, setting
from muMDAU_app.index import main
from muMDAU_app.editor import peditor
from muMDAU_app.editor import markdown
# muMDAU_app setting 

app.jinja_env.auto_reload = True
app.secret_key = setting.yourkey
app.register_blueprint(peditor, url_prefix='/edit')
app.register_blueprint(markdown, url_prefix='/md')
app.register_blueprint(main)
app.config['DEBUG'] = setting.debug

# Main function of MDAUServer
if __name__ == '__main__':
    # log writeing
    print('0MuMDAU Server Run on ' + str(setting.host) + ':' + str(setting.port))
    app.run(host=setting.host,port=setting.port)
