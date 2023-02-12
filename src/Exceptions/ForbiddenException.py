from Exceptions.CapsuleFarmerEvolvedException import CapsuleFarmerEvolvedException


class ForbiddenException(CapsuleFarmerEvolvedException):
    def __init__(self):
        super().__init__(f"Riot servers are overloaded or your IP is blocked by them. Did you leave your VPN on?")