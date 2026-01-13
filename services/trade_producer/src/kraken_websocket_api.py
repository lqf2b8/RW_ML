from typing import List
from websocket import create_connection
from loguru import logger

class KrakenWebSocketAPI:
    URL = "wss://ws.kraken.com/"


    """
    Class for reading trade data from Kraken via WebSocket API.
    """

    def __init__(self, product_id: str):
        self.product_id = product_id
        # Initialize WebSocket connection here
        self.ws = create_connection(self.URL)
        logger.info(f"Connected to Kraken WebSocket API at {self.URL}") 

        self._subscribe(product_id=self.product_id)

    def get_trades(self) -> List[dict]:
        """
        Docstring for get_trades
        
        :param self: Description
        :return: Description
        :rtype: List[dict]
        """
        event = [{
                "product_id": "ETH/USD",
                "price": 1000,
                "qty": 1,
                "timestamp_ms": 163000000000,
            }]
        from time import sleep
        sleep(1)
        
        return event

    
    def is_done(self) -> bool:
        """
        Docstring for is_done
        
        :param self: Description
        :return: Description
        :rtype: bool
        """
        return False