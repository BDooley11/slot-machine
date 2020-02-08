from setuptools import setup

requirements = [emoji,random]

setup(name="slotMachine",
      version="0.1",
      description="Basic slot machine",
      url="",
      author="Barry Dooley",
      author_email="barry.dooley@ucd.ie",
      licence="GPL3",
      packages=['slotMachine'],
      install_requires=requirements,
      entry_points={
        'console_scripts':['run_slotMachine=slotMachine.main:main']
        }
      )
