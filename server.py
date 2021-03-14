#define 2 routes:
#1 - execute network scanner and return list of ip addresses
#2 - scan ports on specific ip address and return details (ip address, mac address, ports, etc...)

import json
from flask import Flask, jsonify, render_template
from subprocess import check_output
app=Flask(__name__)

#METHODS
def scanNetwork():
    raw_output=check_output(['./ip_sweep.sh']).decode('utf-8')  #invoke script and decode output to UTF-8
    ip_list=list(raw_output.split('\n'))                        #separate each address to form a list
    json_ips=[]
    for addr in ip_list:                                        #create list of json objects
        if len(addr):                                           #ignores new line from initial script output
            ip={'ip':addr}
            json_ips.append(ip)
    return json_ips

#--------------------------------------------------------------------

#ROUTES
@app.route('/')
def hello_world():                              #test server response
    return 'server works!'

@app.route('/file_test')
def file_test():                                #test file-reading capabilities
    addresses=open('ip_list.txt', 'r').read()
    return addresses.replace('\n', '<br/>')

@app.route('/ips')
def ip_list_test():
    json_ips=scanNetwork()                  #call network-scanning method
    print(json_ips)
    with open('ip_list.json', 'w') as f:    #save results as json objects to file
        json.dump(json_ips, f)
    print('ips saved to file!')
    with open('ip_list.json', 'r') as f:    #read from file and return list of json objects
        return jsonify(json.load(f))


@app.route('/ip_list')
def ip_list():
    return render_template("ip_list.html") #test for displaying content in html page
    
