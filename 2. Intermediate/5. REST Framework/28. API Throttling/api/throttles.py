from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class BurstRateThrottle(UserRateThrottle):
    scope = "burst"


class SustainedRateThrottle(UserRateThrottle):
    scope = "sustained"
    

class AnonProductsRateThrottle(AnonRateThrottle):
    scope = "products"
    
class AnonOrdersRateThrottle(AnonRateThrottle):
    scope = "orders"
