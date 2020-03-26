
# Creating a class  and identifiying the needs  :

class Jobs:
    def __init__(self, job_name, job_location, job_url):
        self.job_name = job_name
        self.job_location = job_location
        self.job_url = job_url

    def serialize(self):
        return {
            'job_name': self.job_name,
            'job_location': self.job_location,
            'job_url': self.job_url
        }

    def from_json(self, json_):
        self.job_name = json_["job_name"]
        self.job_location = json_["job_location"]
        self.job_url = json_["job_url"]
