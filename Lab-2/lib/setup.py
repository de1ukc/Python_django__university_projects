from setuptools import setup, find_packages

setup(
    name="Serizlizers",
    description="my own JSON TOML YAML Serializer",
    version="3.0.0",
    author="de1ukc",
    packages=find_packages(),
    #packages=["Serializers",],
    install_requires=["PyToml", "dill", "PyYaml"]
)