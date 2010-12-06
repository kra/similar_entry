import datetime

def log(msg):
    print '%s %s' % (datetime.datetime.now().isoformat(),
                     msg.encode('ascii', 'replace'))
