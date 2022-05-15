from flask import flash
class Survey():

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey) < 5:
            flash('Name must be at least 5 characters')
            is_valid = False
        return is_valid
        
        