# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

# Do not edit these constants. They will be updated automatically
# by scripts/update-client.sh.
CLIENT_VERSION = "32.3.2.dev2"
PACKAGE_NAME = "kubernetes-asyncio-kubit"
DEVELOPMENT_STATUS = "4 - Beta"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

with open('requirements.txt') as f:
    REQUIRES = f.readlines()

with open('test-requirements.txt') as f:
    TESTS_REQUIRES = f.readlines()

setup(
    name=PACKAGE_NAME,
    version=CLIENT_VERSION,
    description="Kubernetes asynchronous python client",
    author_email="",
    author="Kubernetes",
    license="Apache License Version 2.0",
    url="https://github.com/tomplus/kubernetes_asyncio",
    keywords=[
        "Swagger",
        "OpenAPI",
        "Kubernetes"],
    install_requires=REQUIRES,
    tests_require=TESTS_REQUIRES,
    packages=[
        'kubernetes_asyncio',
        'kubernetes_asyncio.client',
        'kubernetes_asyncio.config',
        'kubernetes_asyncio.dynamic',
        'kubernetes_asyncio.watch',
        'kubernetes_asyncio.client.api',
        'kubernetes_asyncio.stream',
        'kubernetes_asyncio.client.models',
        'kubernetes_asyncio.utils',
        'kubernetes_asyncio.leaderelection',
        'kubernetes_asyncio.leaderelection.resourcelock'],
    include_package_data=True,
    long_description="""\
    Python client for kubernetes http://kubernetes.io/
    """,
    classifiers=[
        "Development Status :: %s" %
        DEVELOPMENT_STATUS,
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
