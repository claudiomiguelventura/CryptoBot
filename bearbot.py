#Python modules imports
import tweepy

#Own modules import
import keychain

class BearBot():
  def __init__(self):
    self.auth = tweepy.OAuthHandler(keychain.api_key, keychain.api_secret_key)
    self.auth.set_access_token(keychain.access_token, keychain.access_token_secret)
    self.api = tweepy.API(self.auth)
    self.auth_ok = False
    try:
      self.api.verify_credentials()
      self.auth_ok = True
    except:
      self.auth_ok = False
      print("[ERROR]BearBot: authentication failed.")
  
  def tweet(self, message=""):
    if self.auth_ok:
      if message != "":
        self.api.update_status(message)
        return 0
      else:
        return 1