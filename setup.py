import setuptools

install_requires = ['i3ipc']

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="i3ipct",
    version="0.2",
    author="Benjamin Schnitzler",
    author_email="regenbogenbauer@web.de",
    description="Tools build up on i3ipc (focus, find in tree, execute)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bschnitz/i3ipc-python-tools",
    packages=['i3ipct'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires = install_requires
)
