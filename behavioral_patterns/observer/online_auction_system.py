class AuctionItem:
    """Subject: Auction Item being bid on."""

    def __init__(self, name):
        self._name = name
        self._bidders = []
        self._highest_bid = 0

    def attach(self, bidder):
        self._bidders.append(bidder)

    def detach(self, bidder):
        self._bidders.remove(bidder)

    def notify(self):
        for bidder in self._bidders:
            bidder.update(self)

    def receive_bid(self, bid_amount):
        if bid_amount > self._highest_bid:
            self._highest_bid = bid_amount
            self.notify()

    def get_highest_bid(self):
        return self._highest_bid


class Bidder:
    """Observer: Bidders watching the auction item."""

    def __init__(self, name):
        self._name = name

    def update(self, auction_item):
        print(f"{self._name} has been notified. New highest bid: {auction_item.get_highest_bid()} on item {auction_item._name}")


# Client code
item = AuctionItem("Vintage Vase")

bidder1 = Bidder("Alice")
bidder2 = Bidder("Bob")
bidder3 = Bidder("Charlie")

item.attach(bidder1)
item.attach(bidder2)
item.attach(bidder3)

# Bids are received
item.receive_bid(100)  # Updates all bidders
item.receive_bid(150)  # Updates all bidders
