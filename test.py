# from configparser import ConfigParser
# import os

# # config = configparser.ConfigParser()
# # config['DEFAULT'] = {'ServerAliveInterval': '45',
# #                      'Compression': 'yes',
# #                      'CompressionLevel': '9'}
# # config['bitbucket.org'] = {}
# # config['bitbucket.org']['User'] = 'hg'
# # config['topsecret.server.com'] = {}
# # topsecret = config['topsecret.server.com']
# # topsecret['Port'] = '50022'     # mutates the parser
# # topsecret['ForwardX11'] = 'no'  # same here
# # config['DEFAULT']['ForwardX11'] = 'yes'
# # with open('example.ini', 'w') as configfile:
# #   config.write(configfile)

# wd = os.path.relpath(os.getcwd()) #working directory
# cd = os.path.relpath(os.path.dirname(__file__)) #current directory
# # tf = os.path.join(a, b) #target file
# print(os.path.split(__file__)[1])
# print()
# print()
# # c = ConfigParser()
# # c.read(os.path.relpath(os.path.dirname(__file__)))

# # c.read(os.path.dirname(__file__))

a = [1,2,3,4]
b = ['q1','q2','q3','q4']
testDic = {}
j = testDic.fromkeys(b)
print(j)