from setuptools import setup


setup(
    description="Easy peasy wrapper for HipChat's v1 API",
    name='python-simple-hipchat',
    url='https://github.com/kurttheviking/simple-hipchat-py',
    version='0.4.0',
    packages=['hipchat'],
    author='Kurt Ericson',
    author_email='kurttheviking@outlook.com',
    license='MIT',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
