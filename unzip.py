import os

print('Script name')
print('starting...')
try:
    os.system('tar zxvf secret.tgz')
    os.system('openssl pkeyutl -decrypt -inkey HiddenRoad.pem -in key.enc -out key')
    os.system('openssl aes-256-cbc -pbkdf2 -d -in keys.yaml.enc -out keys.yaml -pass file:key')
    print('script has run succesfully')
except Exception as e:
    print('ERROR!!!!'+str(e))
