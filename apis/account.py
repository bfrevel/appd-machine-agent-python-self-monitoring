class AccountApi:
    def __init__(self, config):
        self.config = config
        
    async def access_token(self, session):
        url = f"{self.config['controller_url']}/api/oauth/access_token"
        data = f"grant_type=client_credentials&client_id={self.config['controller_client_id']}&client_secret={self.config['controller_client_secret']}"
        async with session.post(url, data=data) as resp:
            response = await resp.json()
            return response['access_token']