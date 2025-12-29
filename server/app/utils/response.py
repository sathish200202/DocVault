from flask import jsonify

def format_response(data=None, message="", success=True, error=None, token=None):
    response = {
        "data": data,
        "message": message,
        "success": success,
        "error": error
    }
    if token is not None:
        response["token"] = token
    return jsonify(response)