from flask import Flask

application = Flask(__name__)

@application.route('/')
def say_hello():
    return 'Hello World'

# EB looks for an 'application' callable by default.



# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    say_hello()
    application.run()