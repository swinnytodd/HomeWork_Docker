from setuptools import setup

setup(
    name='hello',
    version='0.1.0',
    description='Simple project to display Hello message',
    author='Amantur Dzhamankulov',
    author_email='swinnytodd225@gmail.com',
    license='Proprietary License',
    py_modules=['hello'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'say_hello = hello:main'
        ]
    }
)
