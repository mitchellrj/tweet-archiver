import datetime
import getpass
try:
    import json
except ImportError:
    import simplejson as json
import time
import sys

import tweepy


@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status


def main():
    tweepy.models.Status.first_parse = tweepy.models.Status.parse
    tweepy.models.Status.parse = parse

    username = raw_input("Twitter username: ")
    password = getpass.getpass("Twitter password: ")
    auth = tweepy.auth.BasicAuthHandler(username, password)
    api = tweepy.API(auth)

    in_filename = sys.argv[1]
    out_filename = sys.argv[2]

    myfile = open(in_filename, 'r') # this is a list of tweet IDs
    jsoncontents = open(out_filename, 'a') # blank file

    status_ids = [l.split(':')[1].strip() for l in myfile.readlines() if l.startswith('status_id')]
    myfile.close()
    print 'Read %d status IDs. This will take approx. %.1f hours to complete.' % (len(status_ids), len(status_ids) / 150.0)
    i = 0

    for line in status_ids:
        line = line.strip()
        try:
            status = tweepy.api.get_status(line)
        except tweepy.error.TweepError, e:
            if 'Rate limit exceeded' not in e.message:
                print line, e.message
        else:
            jsoncontents.write(status.json + "\n")
            i += 1
            if int((float(i) / float(len(status_ids)) * 100.0)) > int((float(i - 1) / float(len(status_ids)) * 100.0)):
                print '%d%% complete' % (int((float(i) / float(len(status_ids)) * 100.0)), )
        time.sleep(25) # 150 an hour
   
    jsoncontents.close() 


if __name__ == '__main__':
    main()
