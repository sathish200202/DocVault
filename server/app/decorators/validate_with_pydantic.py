from functools import wraps
from typing import Type, Callable
from flask import request, jsonify
from pydantic import BaseModel, ValidationError

def validate_with_pydantic(model_class: Type[BaseModel]) -> Callable:
     """
    Decorator to validate incoming JSON requests using a Pydantic model class.
    
    Args:
        model_class (Type[BaseModel]): The Pydantic model class for request validation.
    
    Returns:
        Callable: The decorated route function with validated data passed as `validated_data`.
    """
     def decorator(func: Callable) -> Callable:
          @wraps(func)
          def wrapper(*args, **kwargs):
                content_type = request.content_type or ""
                try:
                    if content_type.startswith("application/json"):
                         data = request.get_json(force=True)
                    elif content_type.startswith("multipart/form-data"):
                         data = request.form_to_dict()
                    else:
                        return jsonify({"error": "Unsupported content type"}), 400
                    validated_data = model_class(**data)

                except ValidationError as ve:
                    return jsonify({"errors": ve.errors()}), 400
                except Exception as e:
                    return jsonify({"error": "Invalid request body"}), 400
            
                return func(*args, validated_data=validated_data, **kwargs)
          return wrapper
     return decorator