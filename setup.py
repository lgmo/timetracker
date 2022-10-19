from importlib.metadata import entry_points
import setuptools

setuptools.setup(
    include_package_data=True,
    name='timetracker',
    version='1.0.0',
    description='Simple time tracker.',
    author='Leonardo Moreira',
    packages=setuptools.find_packages(),
    install_requires=['pytest', 'click', 'click_default_group'],
    entry_points={
        'console_scripts': [
            'ttracker = ttracker.scripts.timetracker:cli'
        ]
    },
    classifiers=[
        "Programming language :: Python :: 3",
        "Operating system :: Linux",
    ]
)