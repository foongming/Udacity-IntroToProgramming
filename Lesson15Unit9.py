def get_page(url):
  # try block
  try:
    import urllib
    return urllin.urlopen(url).read()
  # if something fails, execution will jump to the except block
  except:
    return ""
