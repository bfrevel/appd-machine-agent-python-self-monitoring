import asyncio


class ApplicationApi:
    def __init__(self, config):
        self.config = config
        
    async def applications(self, session):
        url = f"{self.config['controller_url']}/rest/applications?output=json"
        async with session.get(url) as resp:
            applications = await resp.json()
            print(f"name={self.config['metric_path']}|Applications|Count, value={len(applications)}")
            return applications

    async def business_transactions(self, session, application):
        url = f"{self.config['controller_url']}/rest/applications/{application['id']}/business-transactions?output=json"
        async with session.get(url) as resp:
            business_transactions = await resp.json()
            print(f"name={self.config['metric_path']}|Applications|{application['name']}|Business Transactions|Count, value={len(business_transactions)}")
            return business_transactions

    async def tiers_and_nodes(self, session, application):
        url = f"{self.config['controller_url']}/rest/applications/{application['id']}/tiers?output=json"
        async with session.get(url) as resp:
            tiers = await resp.json()
            print(f"name={self.config['metric_path']}|Applications|{application['name']}|Tiers|Count, value={len(tiers)}")
            
            node_tasks = []
            for tier in tiers:
                node_tasks.append(asyncio.ensure_future(self.nodes_by_tier(session, application, tier)))
            await asyncio.gather(*node_tasks)

            return tiers

    async def nodes_by_tier(self, session, application, tier):
        url = f"{self.config['controller_url']}/rest/applications/{application['id']}/tiers/{tier['id']}/nodes?output=json"
        async with session.get(url) as resp:
            nodes = await resp.json()
            print(f"name={self.config['metric_path']}|Applications|{application['name']}|Tiers|{tier['name']}|Nodes|Count, value={len(nodes)}")
            return nodes

    async def backends(self, session, application):
        url = f"{self.config['controller_url']}/rest/applications/{application['id']}/backends?output=json"
        async with session.get(url) as resp:
            backends = await resp.json()
            print(f"name={self.config['metric_path']}|Applications|{application['name']}|Backends|Count, value={len(backends)}")
            return backends
