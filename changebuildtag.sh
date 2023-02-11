# Replacing the tagVersion with the value passed in the parameter.
#!/bin/bash
sed "s/tagVersion/$1/g" deploy.yml > deploy-pythonapp.yml