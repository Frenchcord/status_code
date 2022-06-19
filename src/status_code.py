'''
Making a discord api wrapper too?
Here's something that might help you
200 : valid
401 : invalidtoken
429 : rates limits
400 : invalid requests
'''
def status(st: int):
  if st == 200: 
    return
  elif st == 401: 
    raise InvalidToken('The token is invalid')
  elif st == 400: 
    raise InvalidCharacter('Erreur de contenu')
  elif st == 429:
    raise RateLimits('Veuillez ne pas raid/nuke avec frenchcord.\nDe Discord \nYou are being blocked from accessing our API temporarily due to exceeding our rate limits frequently. Please read our docs at https://discord.com/developers/docs/topics/rate-limits to prevent this moving forward.\nTraduction : Tu es blocké(e) de notre api pour le moment car tu as dépasser nos rate limits s\'il te plait lis cela https://discord.com/developers/docs/topics/rate-limits pour que cela ne se reproduise pas.')
  else:
    raise UnknownError('Erreur inconnue')
