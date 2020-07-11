from setuptools import find_packages, setup


setup(
    name='roadchange',
    version='0.0.1',
    author="Paul Norman",
    author_email="osm@paulnorman.ca",
    url="https://github.com/pnorman/roadchange",
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'Click',
        'fs'
    ],
    setup_requires=[
        'pytest-runner',
        'flake8'
    ],
    tests_require=['pytest'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: GIS"
    ],
    python_requires="~=3.6"
)
