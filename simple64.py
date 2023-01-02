'''

░██████╗██╗███╗░░░███╗██████╗░██╗░░░░░███████╗░█████╗░░░██╗██╗
██╔════╝██║████╗░████║██╔══██╗██║░░░░░██╔════╝██╔═══╝░░██╔╝██║
╚█████╗░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░██████╗░██╔╝░██║
░╚═══██╗██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░██╔══██╗███████║
██████╔╝██║██║░╚═╝░██║██║░░░░░███████╗███████╗╚█████╔╝╚════██║
╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░╚════╝░░░░░░╚═╝

Adds easy to use base64 encoding and decoding functions to python
By Daniel4-Scratch
'''

import base64

def encode64(message):
  base64_bytes = message.encode('ascii')
  message_bytes = base64.b64encode(base64_bytes)
  message = message_bytes.decode('ascii')
  return(message)

def decode64(message):
  base64_bytes = message.encode('ascii')
  message_bytes = base64.b64decode(base64_bytes)
  message = message_bytes.decode('ascii')
  return(message)