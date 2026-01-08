from typing import List

class KrakenWebSocketAPI:
    


    """
    Class for reading trade data from Kraken via WebSocket API.
    """

    def __init__(self, product_id: str):
        self.product_id = product_id
        # Initialize WebSocket connection here

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
        return event

    
    def is_done(self) -> bool:
        """
        Docstring for is_done
        
        :param self: Description
        :return: Description
        :rtype: bool
        """
        False