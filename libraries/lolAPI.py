
from pantheon import pantheon
import asyncio

class retrieveDataLOL:
    def __init__(self):
        self.server = ""
        self.api_key = ""
        self.name = ""
        self.debug = False
        self.loop = asyncio.get_event_loop()
        
    def __requestsLog(self, url, status, headers):
        print(url)
        print(status)
        print(headers)
    
    def startServerConnection(self):
        if self.debug:
            self.panth = pantheon.Pantheon(self.server, 
                                            self.api_key, 
                                            errorHandling=True, 
                                            requestsLoggingFunction=self.__requestsLog, 
                                            debug=self.debug)
        else:
            self.panth = pantheon.Pantheon(self.server, 
                                            self.api_key, 
                                            errorHandling=True, 
                                            debug=self.debug)
                                            
        (self.summonerId, self.accountId) = self.loop.run_until_complete(self.__getSummonerId())
        
    def setServerConfig(self, config):
        self.server = config['server']
        self.api_key = config['api_key']
        self.name = config['name']
    
    def getDataLatestMatches(self, matches):
        return self.loop.run_until_complete(self.__getRecentMatches(matches))
        
    def getTimelinesMatches(self, matches):        
        return self.loop.run_until_complete(self.__getMatchTimeLine(matches))
        
    async def __getSummonerId(self):
        try:
            data = await self.panth.getSummonerByName(self.name)
            return (data['id'],data['accountId'])
        except Exception as e:
            print(e)
            
    async def __getRecentMatchlist(self, endIndex):
        try:
            data = await self.panth.getMatchlist(self.accountId, params={"endIndex":endIndex})
            return data
        except Exception as e:
            print(e)
            
    async def __getRecentMatches(self, endIndex):
        try:
            matchlist = await self.__getRecentMatchlist(endIndex)
            tasks = [self.panth.getMatch(match['gameId']) for match in matchlist['matches']]
            return await asyncio.gather(*tasks)
        except Exception as e:
            print(e)
            
    async def __getMatchTimeLine(self, endIndex):
        try:
            matchlist = await self.__getRecentMatchlist(endIndex)
            tasks = [self.panth.getTimeline(match['gameId']) for match in matchlist['matches']]
            return await asyncio.gather(*tasks)
        except Exception as e:
            print(e)