MAX_DEPTH = 10  # maximum click depth
MIN_DEPTH = 3 # minimum click depth
MAX_WAIT = 10  # maximum amount of time to wait between HTTP requests
MIN_WAIT = 5  # minimum amount of time allowed between HTTP requests
DEBUG = True  # set to True to enable useful console output

# use this single item list to test how a site responds to this crawler
# be sure to comment out the list below it.
#ROOT_URLS = ["https:///digg.com/"]

ROOT_URLS = [
	"https://aternosafk.gtheripper.repl.co",
	"https://https://dino-th.pages.dev"
	]
	  

# must use a valid user agent or sites will hate you
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) ' \
	'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
