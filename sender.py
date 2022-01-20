print("""\n
      
╦═╗┬┌─┐┬ ┬  ┌─┐┌─┐┌┐┌┌─┐┬ ┬┌─┐┌─┐  ╔╦╗┬ ┬┬┌┬┐┌┬┐┌─┐┬─┐
╠╦╝││  ├─┤  └─┐├─┤││││  ├─┤├┤ ┌─┘   ║ ││││ │  │ ├┤ ├┬┘
╩╚═┴└─┘┴ ┴  └─┘┴ ┴┘└┘└─┘┴ ┴└─┘└─┘   ╩ └┴┘┴ ┴  ┴ └─┘┴└─
\n\n
      """)

# Packages
from apscheduler.schedulers.blocking import BlockingScheduler
from twython import Twython

# Starting the twitter API
APP_KEY = ''
APP_SECRET = ''
twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
print (auth['auth_url'])
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
FINAL_OAUTH_TOKEN = ''
FINAL_OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET,FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)


# The job function
def some_job():
    count = 1
    twitter.update_status(status=f"Wubba Lubba Dub Dub HOOOOOOOOOOOOOOOO, day {count}")
    print(f"day {count}")
    count += 1

# the scheduler
scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', hour=24, minute=10)
scheduler.start()