completionTimes = [1285, 1410, 1700]

def printFlag(num, time):
  
  if num == 0:
    msg = f"You beat the game!                       Here's flag #{num+2}:"
  else:
    msg = f"You beat the game in under {time:>5} frames! Here's flag #{num+2}:"
  
  filename = '../flags/flag%d.txt' % num
  try:  
    with open(filename, 'r') as file:
      print(f"{msg} {file.read().strip()}")
  except:
    print(f"{msg} Error: No flag file {filename}")


def printFlags(time):
  print("Your time: %d frames" % time)
  i = 0
  printFlag(0, 0)
  for t in completionTimes[::-1]:
    i += 1
    if time < t:
      printFlag(i, t)
    else:
      print("Now try completing it under %d frames!" % t)
      break