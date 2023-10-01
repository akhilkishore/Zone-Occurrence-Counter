from flask import jsonify, request
from flask.views import View
import pandas as pd
import traceback


class ZoneOccurrence(View):
    # allows POST only
    methods = ['POST']
    
    def __init__(self):
        self.status = False
        self.message = "Invalid Request"
        self.data = {}
        self.mandatory_fields = ['zone']
        self.response = { "status": self.status, "message": self.message, "data": self.data }
        
    def update_response_dict(self):
        """
        - update and return response dict
        """
        print((self.response))
        self.response = { "status": self.status, "message": self.message, "data": self.data }
        print(self.response)
        return self.response
    
    
    def count_zone_occurrence(self, df, validate_zone=False):
        """
        - count zone occurrence
        - update response data field
        """
        zone_count_dict = df['zone'].value_counts().to_dict()
        self.data = zone_count_dict
    
    
    def mandatory_field_check(self, df):
        """
        - check mandatory fields present or not
        - if not update response message
        """
        df_cols_ = df.columns.tolist()
        for k_ in self.mandatory_fields:
            if k_ not in df_cols_:
                self.message = "Mandatory fields missing from csv!"
                return False
        return True


    def read_as_dataframe(self, file_obj):
        """
        - try reading csv using pandas (without saving)
        - else update response message
        """
        try:
            df = pd.read_csv(file_obj)
            return df, True
        except Exception:
            self.message = "Invalid CSV found!"
            print(traceback.format_exc())
            return None, False
            

    def dispatch_request(self):
        """ STEPS :
        - fetch csv file
        - read (without saving) and validate csv file
        - count zone occurrence
        - return JSON response
        """
        # validate incoming request
        if not request.files or 'csv_file' not in request.files.keys():
            self.message = "Invalid File-Part!"
            return jsonify(self.update_response_dict())
        
        
        # fetch file-part object
        file_ = request.files['csv_file']
        file_df, is_file = self.read_as_dataframe(file_)
    
    
        if not is_file or not self.mandatory_field_check(file_df):
            # failed to parse csv (or) mandatory fields missing
            return jsonify(self.update_response_dict())
    
        
        # count zone occurrence
        self.count_zone_occurrence(file_df)
        # update response values
        self.status, self.message = True, "Success"
        return jsonify(self.update_response_dict())
    

