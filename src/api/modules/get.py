from config.libs import *
from api import app


@app.route("/get-user/<user_id>", methods=['GET'])
@cross_origin()
def get_user_wrapper(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    response = app.response_class(
        response=json.dumps(user_data),
        status=200,
        mimetype='application/json'
    )

    return response
