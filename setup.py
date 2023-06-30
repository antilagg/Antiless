from setuptools import setup

setup(name='Antiless',
      version="1.0b5",
      packages=['Antiless', 'Antiless.GeoIP', 'Antiless.Tools', 'Antiless.Exceptions'],
      url='https://github.com/MHProDev/Antiless',
      license='MIT',
      author="Antiless",
      install_requires=[
          "maxminddb>=2.2.0", "requests>=2.27.1", "yarl>=1.7.2",
          "pysocks>=1.7.1"
      ],
      include_package_data=True,
      package_data={
          'Antiless.GeoIP': ['Sqlite/*.txt', "Sqlite/GeoLite2-Country.mmdb"],
          '': ["LICENSE.md"]
      })
