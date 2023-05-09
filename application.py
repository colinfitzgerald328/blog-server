from flask import Flask

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/', methods=['GET'])
def get_athlete_history():
    return {"operation": "success",
            "server_status": "operational"
            }

# run the app.
if __name__ == "__main__":
    application.run()