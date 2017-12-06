# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/framew$# Author: Kevin Mikus
# Author: Eugene Matavitski
# Date Developed: 2017-11-10
# Last Date Changed: 2017-12-01
# Rev: 0.4

import ianSftp, eugenePyro, ianEmail, ianHmac, teamFourMongolog
from threading import Thread
""" class that is responsible for actions of the bottom node"""
def threaded_function(PyroObject):
   """method to run pyro as separate thred"""
   PyroObject.startPyro()

if __name__ == "__main__":
   try:
      log = teamFourMongolog.Logger()
      log.insertRecord("Bottom node start", None)
   except Exception as e:
      print(e)
   pyro_object = eugenePyro.Sender()
   thread = Thread(target = threaded_function, args = (pyro_object,))
   thread.start()

   # pull file from sftp server
   fname = "payloadTeam4.json"
   try:
      payload = ianSftp.Client().get(fname)
      payload = ianHmac.Hmac().unwrap().encode("utf-8")
   except Exception as e:
      print(e)
      print("Something is wrong with a file")
   print(payload)
   log.insertRecord("Bottom node receive", payload)

   # sending email
   try:
      emailSender = ianEmail.Email("Test subject", "kzm5599@psu.edu", "kzm5599@psu.edu")
      emailSender.sendMail(payload.decode("utf-8"))
   catch Excteption as e:
      print(e)
      print("Couldn't send email")
   # updating payload data with payload recieved in Sftp
   try:
      pyro_object.set_data(payload)
   except Exception as e:
      print(e)
   # promting user to start left node
   print('Please run leftNode.py')

   # waiting for client to read payload
   try:
      while(pyro_object.get_iteration()==0):
         pass
      pyro_object.kill_pyro()
      log.insertRecord("Bottom node send", payload)
   except Exception as e:
      print(e)
