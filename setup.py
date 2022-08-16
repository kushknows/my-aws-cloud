import setuptools

with open("README.md", "r") as fh:
	description = fh.read()

setuptools.setup(
	name="my_aws_cloud",
	version="0.0.1",
	author="kush",
	author_email="kushagraagarwal9@gmail.com",
	packages=["my_aws_cloud"],
	description="A sample test package",
	long_description=description,
	long_description_content_type="text/markdown",
	url="https://github.com/kushknows/my-aws-cloud",
	license='MIT',
	python_requires='>=3.8',
	install_requires=[]
)
