import requests
import json

class OPAClient:
    def __init__(self, opa_url):
        self.opa_url = opa_url

    def evaluate_policy(self, input_data):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f"{self.opa_url}/v1/data/agent_policy", headers=headers, data=json.dumps(input_data))
        if response.status_code == 200:
            result = response.json()
            return result.get('result', {}).get('allow', False)
        else:
            print(f"Failed to evaluate policy: {response.status_code}, {response.text}")
            return False