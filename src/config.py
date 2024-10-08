import json
import os

class Config:
    def __init__(self):
        self.load_config()
    
    def load_config(self):
        self.github_token = os.environ.get('GITHUB_TOKEN')

        with open('config.json', 'r') as f:
            config = json.load(f)
            self.notification_settings = config.get('notification_settings')
            self.subscriptions_file = config.get('subscriptions_file')
            self.update_interval = config.get('update_interval', 24 * 60 * 60)  # Default to 24 hours
