class DataValidationError(Exception):
    ...
    
    
class ContentValidate:

    valid_inputs = {
        "title": str,
        "module": str,
        "students": int,
        'description': str,
        "is_active": bool
    }

    valid_keys = [
        "title",
        "module",
        "students",
        'description',
        "is_active"
    ]
    
    
    def __init__(self, *args, **kwargs: dict):
        self.data = kwargs
        self.errors = {}
        
    def is_valid(self):
        
        self.clean_data()
        try:
            self.validate_required_keys()
            self.validate_data_types()

            return True
        except (KeyError, DataValidationError):
            return False
            
    def clean_data(self):
        data_keys = list(self.data.keys())

        for key in data_keys:
            if key not in self.valid_keys:
                self.data.pop(key)

    def validate_required_keys(self):
        for valid_key in self.valid_keys:
            if valid_key not in self.data.keys():
                self.errors[valid_key] = "missing key"

        if self.errors:
            raise KeyError

    def validate_data_types(self):

        for valid_key, expected_type in self.valid_inputs.items():
            if type(self.data[valid_key]) is not expected_type:

                message = f"{valid_key} must be a {expected_type.__name__}"
                #se não põem esse __name__ vem uma classe estranha
                self.errors[valid_key] = message

        if self.errors:

            raise DataValidationError   
