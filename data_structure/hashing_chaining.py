key_num = 11 #소수로 하는 게 좋음
hash_table = list(None for i in range(key_num))
#[None, None, None ...]

def get_key(data):
  return hash(data)
  # or
  # honor = 37 #호너
  # ordsum = 0
  # for letter in data:
  #   ordsum = ordsum * honor + ord(letter)
  # return ordsum

def hash_function(key):
  return key % len(hash_table)

def save_value(data, value):
  # hash_table[hash_addr] = value
  # 밑은 Open Hashing: chaining
  index_key = get_key(data)
  hash_addr = hash_function(index_key)

  
  if hash_table[hash_addr] != None:
    for index in range(len(hash_table[hash_addr])):
      if hash_table[hash_addr][index][0] == index_key:
        hash_table[hash_addr][index][1] = value
        return
      hash_table[hash_addr].append([index_key, value])
  else:
    hash_table[hash_addr] = [[index_key, value]]

def get_value(data):
  # return hash_table[hash_addr]
  # 밑은 Open Hashing: chaining
  index_key = get_key(data)
  hash_addr = hash_function(index_key)
  
  for index in range(len(hash_table)):
    if hash_table[hash_addr][index][0] == index_key:
      return hash_table[hash_addr][index][1]
    return None
  return None


save_value("Dave", '01011112222')
save_value("Jane", '01012345678')
save_value("Ben", '01056781234')
print(get_value("Ben"))
