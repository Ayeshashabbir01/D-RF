from rest_framework.throttling import UserRateThrottle

class JackRateThrottle(UserRateThrottle):
    """
    Custom throttle class that allows 5 requests per minute for authenticated users.
    """
    scope = 'jack'