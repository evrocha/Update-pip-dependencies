import subprocess

with open('requirements.txt', 'r') as file:
    lines = file.readlines()

# Atualize cada pacote
for line in lines:
    package = line.split('==')[0]
    subprocess.call(['pip', 'install', '--upgrade', package])