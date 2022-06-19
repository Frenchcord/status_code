class TokenError(Exception):
  pass
class HumainToken(TokenError):
  pass
class InvalidToken(TokenError):
  pass
class InvalidCharacter(Exception):
  pass
class RateLimits(Exception):
  pass
class InvalidChannelName(Exception):
  pass
class UnknownError(Exception):
  pass
class CommandDoesNotExist(Exception):
  pass
