from setuptools import setup, find_packages

setup(
    name="cracksql",
    version="0.0.0-alpha",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        # Flask related
        "flask==2.2.5",
        "flask-sqlalchemy==3.0.2",
        "flask-migrate==3.1.0",
        "flask-cors==3.0.10",
        "Flask-APScheduler==1.12.3",
        "flask_caching==1.10.1",
        "gunicorn",
        
        # Database
        "pymysql==1.0.2",
        
        # Utils
        "PyJWT==2.3.0",
        "PyYAML==6.0",
        "aliyun-python-sdk-core==2.13.36",
        
        # Document processing
        "tiktoken>=0.3.3",
        
        # LLM related
        "langchain-community>=0.3.13",
        "langchain>=0.1.0",
        "langchain-openai>=0.2.14",
        "openai>=1.3.0",
        "aiohttp>=3.8.0",
        "tenacity>=8.2.0",
        "sentence-transformers>=2.2.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.0.0",
        "chromadb>=0.4.15",
        
        # SQL parsing related
        "sqlglot==26.6.0",
        "antlr4-python3-runtime==4.13.2",
        
        # ML frameworks
        "transformers>=4.47.1",
        "torch==2.1.0",
        "torchvision",
        "torchaudio",
        "accelerate>=0.26.0",
    ],
    author="code4DB",
    author_email="weizhoudb@gmail.com",
    description="Seamless translation over multiple dialect by large language model (LLM).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/code4DB/CrackSQL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3.10",
    include_package_data=True,
    package_data={
        "cracksql": ["config/*", "config/*.*", "templates/*", "static/*"],
    },
    exclude_package_data={
        '': ['*.pyc', '*.pyo', '*.pyd', '__pycache__', '*.so', '*.egg', '*.egg-info', '*.DS_Store'],
        'cracksql': [
            'local_models/*',
            'migrations/*',
            'instance/*',
            'logs/*',
            'sources/*',
            '.venv/*',
            '.git/*',
            '.idea/*',
            '__pycache__/*',
            'tests/*',
            'docs/*',
        ],
    },
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'flake8>=6.0.0',
            'black>=23.0.0',
            'isort>=5.0.0',
            'mypy>=1.0.0',
            'pre-commit>=3.0.0',
            'twine>=4.0.0',
            'build>=1.0.0',
        ]
    }
) 