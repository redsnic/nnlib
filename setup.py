import setuptools

setuptools.setup(
   name='nnlib',
   version='0.99',
   description='A library for basic nn stuff',
   author='Nicolò Rossi',
   author_email='olocin.issor@gmail.com',
   install_requires=['wheel', 'pandas', 'numpy', 'tensorflow', 'matplotlib', 'opencv-python'],
   packages=setuptools.find_packages()
)



