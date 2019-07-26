from pip._vendor.distlib.compat import raw_input

quote = raw_input('What is the quote? These aren\'t the droids you\'re looking for. Who said it?')
if quote == 'Obi-Wan Kenobi':
    print('Obi-Wan Kenobi says, "These aren\'t the droids you\'re looking for."')
else:
    print('error')
