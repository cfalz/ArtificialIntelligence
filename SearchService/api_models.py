from flask_restplus import fields

class ApiModel(object):
    def __init__(self, api):
        self.api = api


    def item_format(self):
        return self.api.model('Item Format',{
            "Puzzle":fields.List(description="Puzzel To Solve"),
        })

    def item_list_response_format(self):
        return  self.api.model('List of Items', {
            "Solution": fields.List()
        })

    def item_failure_response(self):
        return self.api.model('Item Failure response',{
            "Failure":fields.String(description="Reason for failure", required=False),
        })

