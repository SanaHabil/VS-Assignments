from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.language = data['language']
        self.location = data['location']
        self.comment = data['comment']
        self.favorit_language = data['favlang']
        self.cohort = data['cohort']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']        


    @staticmethod
    def validate_survey(survey):
        is_valid = True # we assume this is true
        if  len(survey['name']) < 3:
            flash(" Name must be at least 2 characters.")
            is_valid = False
        if  len(survey['language']) < 1:
            flash("Please choose Language")
            is_valid = False
        if  len(survey['location']) < 1:
            flash("PLease choose Location")
            is_valid = False
        if  len(survey['favlang']) < 1:
            flash("Please choose Favorit Languages")
            is_valid = False
        if len(survey['cohort']) < 1:
            flash("Please Choose Cohort")
            is_valid = False   
        return is_valid

    @classmethod    
    def add_survey(cls, data):
            query = "INSERT INTO surveys ( name , language, location, comment, favlang, cohort, created_at , updated_at ) VALUES (%(name)s, %(language)s,%(location)s,%(comment)s,%(favlang)s,%(cohort)s,NOW(),NOW());"
            result = connectToMySQL('dojo_survey_schema').query_db(query,data)
            return result      