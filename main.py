stream_of_message = [[],[1,'foo'],[2,'bar'],[3,'foo'],[8,'bar'],[10,'foo'],[11,'foo']]
# ouptut_expected = [null,true,true,false,false,false,true]
output = []

class Logger:

  def __init__(self):
    self.dict_message = {}
    
  def should_print_message(self, timestamp: int, message: str)->bool:
    if timestamp is None or message is None:
      return None
    
    if message not in self.dict_message:
      self.dict_message[message] = timestamp
      return True

    if timestamp - self.dict_message[message] >= 10:
      self.dict_message[message] = timestamp
      return True
    else:
      return False

logger = Logger()
for message in stream_of_message:
  if len(message) == 0:
    output.append(logger.should_print_message(None,None))
  else:
    timestamp = message[0]
    message = message[1]
    output.append(logger.should_print_message(timestamp,message))


print(output)