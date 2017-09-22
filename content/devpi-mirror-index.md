Title: Devpi Mirror Index
Status: draft
Tags: python
Date: 2016-9-6

pip install devpi-web
devpi use http://localhost:3141/root/pypi/
devpi login root
sudo supervisorctl status devpi-server
sudo supervisorctl restart devpi-server
devpi index
devpi index -c zonza type=mirror volatile=True mirror_url=http://pypi-zonza.company.prv/company/unstable/+simple/ title=Zonza
