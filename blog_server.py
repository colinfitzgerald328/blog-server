from flask import Flask

# EB looks for an 'application' callable by default.
blog_server = Flask(__name__)

@blog_server.route('/', methods=['GET'])
def get_athlete_history():
    return {"operation": "success",
            "server_status": "operational"
            }

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    blog_server.debug = True
    blog_server.run()