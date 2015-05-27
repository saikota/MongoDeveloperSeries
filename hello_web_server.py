
import bottle
import pymongo

# this is the handler for the default path of the web server

@bottle.route('/')
def index():
    
    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    # attach to test database
    db = connection.test


    # get handle for names collection
    name = db.persons

    # find a single document
    item = name.find_one()
    displayTxt = '<b>Hello %s</b>, <b> %s!</b>' % (item['first'], item['last'])
    return displayTxt


bottle.run(host='localhost', port=8095)
