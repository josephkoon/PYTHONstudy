import subprocess

fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()

subprocess.Popen(['open', '/Applications/Calculator.app/'])

