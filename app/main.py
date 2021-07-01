#!/usr/local/bin/python3.8


from flask import Flask, render_template, request,json, jsonify,Response,make_response
import sqlite3
import json
from sqlwrap import *
#from mkpdf import make_pdf
import subprocess
import os

class CustomFlask(Flask):
  jinja_options = Flask.jinja_options.copy()
  jinja_options.update(dict(
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',  ))


app = CustomFlask(__name__)

dbname = 'rem.db'

#------ python pth ------
#py = '/usr/local/bin/python3.8'
py = 'python'



#------各処理ページの基本的なルーティング-------


@app.route('/')
def rootn():
    return 'Hello Rem'

@app.route('/rem')
def rem():
    return render_template('rem.html',config='conf/rem_conf.js')

@app.route('/rem/<conf>')
def rem_with_config(conf):
    return render_template('rem.html',config=f'/conf/{conf}.js')

@app.route('/t/<f>')
def tpl_route(f):
    return render_template(f)


@app.route('/<f>')
def proc(f):
    return app.send_static_file('./'+f)

@app.route('/<dirname>/<f>')
def dir_file(dirname,f):
    return app.send_static_file(f'./{dirname}/{f}')

'''
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
'''

#--------印刷 ブロック -------------

@app.route('/print/<conf>/<ID>')
def print(conf,ID):
    try:
#        cmd = "/usr/local/bin/python3.8 ./pdf_ryomou.py "+conf+" "+ID
        pfile = f"static/pdf/output_{ID}.pdf"
        cmd = f"{py} ./{conf}.py {ID}"
        out = os.popen(cmd).read()
        response = make_response()
        response.data = open(pfile, "rb").read()
        os.remove(pfile)
        
        response.mimetype = "application/pdf"
        return response
#        return app.send_static_file('./pdf/output.pdf')
    except Exception as e:
        return f"Print Error: {e}"


@app.route('/printest')
def printest():
    try:
        pdfdata = open("output.pdf", "rb").read()
        response = make_response(pdfdata)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filenam=export.pdf'
        #response.mimetype = "application/pdf"
        return response
    except Exception as e:
        return f"Print Error: {e}"


#--------REM API ブロック -------------
@app.route('/remapi/<table>',methods=['GET'])
def remapi_get_all(table):
    conn = sqlite3.connect(dbname)
    res = json_select_all(conn,table)
    conn.close()
    return res

@app.route('/remapi/<table>/<pkey>',methods=['GET'])
def remapi_get_one(table,pkey):
    conn = sqlite3.connect(dbname)
    sel_key = {'ID':pkey}
    res = json_select_one(conn,table,sel_key,'ID')
    conn.close()
    return res

@app.route('/remapi/<table>/<item>/<key>',methods=['GET'])
def remapi_get_byKey(table,item,key):
    conn = sqlite3.connect(dbname)

    sel_key = {item:key}


    if request.args.getlist('key_name_from_to[]'):

      k_n_f = request.args.getlist('key_name_from_to[]')
      try:
        sel_key[k_n_f[0]] = k_n_f[1:]

      except:
        return []

      res = json_select_all_key(conn,table,sel_key,item,key_name_from_to=k_n_f[0])
    else:
      res = json_select_all_key(conn,table,sel_key,item,key_name_from_to='')


    conn.close()
    return res

@app.route('/remapi/<table>',methods=['POST'])
def remapi_get_post(table):
    conn = sqlite3.connect(dbname)
    res = dict_insert(conn,table,request.json)
    conn.commit()
    conn.close()
    return res

@app.route('/remapi/<table>',methods=['PUT'])
def remapi_put(table):
    conn = sqlite3.connect(dbname)
    res = dict_update(conn,table,request.json,'ID')
    conn.commit()
    conn.close()
    return res

@app.route('/remapi/<table>/<key_name>/<key>',methods=['PUT'])
def remapi_put_key(table,key_name,key):
    conn = sqlite3.connect(dbname)
    res = dict_update(conn,table,request.json,key_name)
    conn.commit()
    conn.close()
    return res

@app.route('/remapi/<table>/<pkey>',methods=['DELETE'])
def remapi_del(table,pkey):
    conn = sqlite3.connect(dbname)

    del_key = {'ID':pkey }
    res = dict_delete(conn,table,del_key,'ID')
    conn.commit()
    conn.close()
    return res

@app.route('/remapi/<table>/<key_name>/<key>',methods=['DELETE'])
def remapi_del_key(table,key_name,key):
    conn = sqlite3.connect(dbname)

    del_key = {key_name:key }
    res = dict_delete(conn,table,del_key,key_name)
    conn.commit()
    conn.close()
    return res

@app.errorhandler(Exception)
def error_except(e):
    #print('メッセージ:{}'.format(e.args))
    return jsonify({'message': 'Exception', 'action': 'call me'}), 500
#------Main-----
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)
