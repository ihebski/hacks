import binascii

data = open('usbdata', 'r').read().split('\n')

keys = {"4":"A","5":"B","6":"C","7":"D","8":"E","9":"F","10":"G","11":"H","12":"I","13":"J","14":"K","15":"L","16":"M","17":"N","18":"O","19":"P","20":"Q","21":"R","22":"S","23":"T","24":"U","25":"V","26":"W","27":"X","28":"Y","29":"Z","30":"1","31":"2","32":"3","33":"4","34":"5","35":"6","36":"7","37":"8","38":"9","39":"0","40":"ENTER","41":"ESC","42":"BACKSPACE","43":"TAB","44":"SPACE","45":"MINUS","46":"EQUAL","47":"LEFT_BRACE","48":"RIGHT_BRACE","49":"BACKSLASH","50":"NUMBER","51":"SEMICOLON","52":"QUOTE","53":"TILDE","54":"COMMA","55":"PERIOD","56":"SLASH","57":"CAPS_LOCK","58":"F1","59":"F2","60":"F3","61":"F4","62":"F5","63":"F6","64":"F7","65":"F8","66":"F9","67":"F10","68":"F11","69":"F12","70":"PRINTSCREEN","71":"SCROLL_LOCK","72":"PAUSE","73":"INSERT","74":"HOME","75":"PAGE_UP","76":"DELETE","77":"END","78":"PAGE_DOWN","79":"RIGHT","80":"LEFT","81":"DOWN","82":"UP","83":"NUM_LOCK","84":"EYPAD_SLASH","85":"EYPAD_ASTERIX","86":"EYPAD_MINUS","87":"EYPAD_PLUS","88":"EYPAD_ENTER","89":"EYPAD_1","90":"EYPAD_2","91":"EYPAD_3","92":"EYPAD_4","93":"EYPAD_5","94":"EYPAD_6","95":"EYPAD_7","96":"EYPAD_8","97":"EYPAD_9","98":"EYPAD_0","99":"EYPAD_PERIOD","0":"00"}

bob = ''
counter = 0
for line in data:
 if ':' in line:
  counter += 1
  l_bytes = line.split(':')
  breakout = True
  for i in l_bytes:
   if not i == '00':
    breakout = False
  if not breakout: 
   print l_bytes
   if l_bytes[0] == '02':
    print 'SHIFT'
    val=int(l_bytes[2],16)
    print keys[str(val)]
