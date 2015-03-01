#!/usr/bin/python

import requests
import json

class jsonobject:
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class wrapper:
  def __init__(self,url):
    self.url = url
    self.nodes = {}

  def get_token(self,username,password):
    payload = {'username': username, 'password': password}
    r = requests.post(self.url + '/api-token-auth/',data=payload)
    token =  json.loads(r.content)['token']
    if token is not None:
      self.token = token
      print self.token
  def get_nodes(self):
    r = requests.get(self.url+'/api/nodes/')
    jcontent = json.loads(r.content)
    for node in jcontent:
      name = node['name']
      id = str(node['id'])
      self.nodes[id] = name

  def print_nodes(self):
    print self.nodes
 
  def add_node(self,name):
    jsonc = jsonobject()
    jsonc.properties = ""
    jsonc.arch = "i686"
    jsonc.direct_ifaces = ['eth1','eth2']
    jsonc.local_iface = 'eth0'
    jsonc.sliver_pub_ipv6 = 'none'
    jsonc.sliver_pub_ipv4 = "dhcp"
    jsonc.sliver_pub_ipv4_range = '#8'
    jsonc.name = name
    jsonc.description = name + " created by a script"
    jsonc.silver_mac_prefix = "null"
    jsonc.silver_ipv4_prefix = "null"
    jsonc.group = {'uri':'http://178.62.226.189/api/groups/1'}
    jsonc.token = self.token
    json_to_send = jsonc.to_JSON() 
    header = {'Authentication': ' Token '+self.token}
    r = requests.post(self.url+'/api/nodes/',data=json_to_send,headers=header)
    print r.content
        
w = wrapper('http://178.62.226.189')
w.get_nodes()
w.print_nodes()
w.get_token('admin','admin')
w.add_node("wqeq")
