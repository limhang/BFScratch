import os
import shutil

currentPath = os.getcwd()

egg_info_path = currentPath + '/' +'BFScratch.egg-info'

dist_path = currentPath + '/' +'dist'

# remove egg_info
if os.path.exists('BFScratch.egg-info'):
	shutil.rmtree(egg_info_path)
# # remove dist
if os.path.exists('dist'):
	shutil.rmtree(dist_path)

os.system('python setup.py sdist')

os.system('twine upload dist/*')

